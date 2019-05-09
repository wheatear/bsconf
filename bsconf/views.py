from django.shortcuts import render
from django.http import HttpResponse
import time, re
from boss import settings
import os,logging
import json
import copy
from bsconf.models import *
from django.db.models import Max

# Create your views here.
def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        month = time.strftime('%Y%m', time.localtime())
        jsonFile =request.FILES.get("jsonFile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not jsonFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join(settings.IN_DIR, month, jsonFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in jsonFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")

class BsConfiger(object):
    tplSqlFile = "tplsql_promo.json"
    dTplSql = {}
    def __init__(self, inFile, month=None, type='ZG'):
        self.inFile = inFile
        if not month:
            month = time.strftime('%Y%m', time.localtime())
        self.month = month
        self.type = type
        self.userName = '王新田'
        print('in data file %s' % inFile)
        # self.outFile = 'DB配置-%s-王新田.sql' % inFile
        self.outFile = '%s.sql' % os.path.splitext(os.path.basename(inFile))[0]
        self.dInData = {}
        self.fOut = None

    def start(self):
        print('load sql template')
        self.loadTplSql()
        print('load data')
        self.loadData()
        # self.openOutFile()
        print('parse in file')
        self.parseDoc()
        # self.writeSql()
        # self.closeOut()

    def loadTplSql(self):
        if len(BsConfiger.dTplSql) > 0:
            return
        file = os.path.join(settings.TPL_DIR, self.tplSqlFile)
        with open(file) as fp:
            BsConfiger.dTplSql = json.load(fp)


    def loadData(self):
        # IN_DIR = os.path.join(BASE_DIR, 'bsconf', 'data', 'in')
        file = os.path.join(settings.IN_DIR, self.month, self.inFile)
        with open(file) as fData:  # ,encoding='utf-8'
            self.dInData = json.load(fData)
        confReq = BsconfRequirement.create(self.inFile, self.type)
        confReq.save()

    def parseDoc(self):
        aSql = []

        for req in self.dInData:
            print('parse requirement %s' % req)
            self.outFile = '%s.sql' % os.path.splitext(os.path.basename(req))[0]
            # self.openOutFile()
            # self.fOut.write('-- %s%s' % (req, os.linesep))
            reqData = self.dInData[req]
            confReq = ConfReq(self, req, reqData)
            confReq.parseDocName()
            confReq.parse()

    def closeOut(self):
        self.fOut.close()


class ConfReq(object):
    def __init__(self, configer, docName, reqData):
        self.configer = configer
        self.docName = docName
        self.reqData = reqData
        self.reqId = None
        self.reqName = None
        self.outName = None
        self.fOut = None

    def parseDocName(self):
        docBase = os.path.splitext(os.path.basename(self.docName))[0]
        docBase = docBase.replace('BOSS需求解决方案-','')
        self.reqName = docBase.replace('需求解决方案-', '')
        self.outName = '%s-%s-%s.sql' % (self.configer.type, self.reqName, self.configer.userName)

    def openOut(self):
        if self.fOut:
            return self.fOut
        print('open out file %s' % self.outName)
        file = os.path.join(settings.OUT_DIR, self.configer.month, self.outName)
        print('open out file: %s' % file)
        try:
            self.fOut = open(file, 'w')
        except IOError as e:
            print("can't open file %s. %s" % (file, e))

    def closeOut(self):
        self.fOut.close()

    def writeBlockSql(self, block, num):
        self.fOut.write('-- %s %d%s' % (block.blockName, num, os.linesep))
        for sql in block.getSql():
            self.fOut.write('-- %s%s' % (sql[0], os.linesep))
            self.fOut.write('%s%s' % (sql[1], os.linesep))

    def parse(self):
        self.openOut()
        self.fOut.write('-- %s%s' % (self.reqName, os.linesep))
        for blockGrp in self.reqData:
            print('parse block group %s ...' % blockGrp)
            if blockGrp not in self.configer.dTplSql:
                print('%s no sql template' % blockGrp)
                break
            dBlockSql = self.configer.dTplSql[blockGrp]
            blockGrpData = self.reqData[blockGrp]
            for i in range(len(blockGrpData)):
                print('%s %d' % (blockGrp, i+1))
                blockData = blockGrpData[i]
                # dFields = {}
                block = TableBlock(blockGrp, blockData)
                block.parse()
                self.writeBlockSql(block, i + 1)
                # ss = self.parseBlock(tpl, dFields, dTplSql)
            print('block group %s of %d completed' % (blockGrp, len(blockGrpData)))
        self.fOut.write('%scommit;%s' % (os.linesep, os.linesep))
        self.closeOut()


class TableComp(object):
    def __init__(self, name, data, blockName, parent=None):
        self.tabName = name
        self.dData = data
        self.blockName = blockName
        self.dBlockTmpl = BsConfiger.dTplSql[blockName]
        self.parent = parent

        self.children = []
        self.dFields = {}
        self.sql = None

    def parse(self):
        print('parse table of %s' % self.tabName)
        aSubTable = []
        for field in self.dData:
            val = self.dData[field]
            if type(val) is list:
                for sub in val:
                    self.children.append(Table(field, sub, self))
            elif type(val) is dict:
                self.children.append(Table(field, val, self))
            else:
                self.dFields[field] = val
        print('make sql of table %s' % self.tabName)
        # if len(self.dFields) > 0:
        sql = self.makeSql()
        print(sql)
        # self.aSql.append(sql)
        self.sql = sql
        # if sql:
        #     self.aSql.append(sql)
        for subTab in self.children:
            subTab.parse()
            # for subName in sub:
            #     print('process subtab %s : %s' % (tName, subName))
            #     tab = sub[subName]
            #     self.parseTab(subName, tab)
        print('table %s complate' % self.tabName)

    def makeSql(self):#, self.dFields, self.dTplSql
        if self.tabName not in self.dBlockTmpl:
            print('%s not in block template %s' % (self.tabName, self.blockName))
            return None
        if self.dBlockTmpl[self.tabName] == "None":
            return None
        if self.tabName in dTabCheck:
            if self.checkExist():
                return None
        dTabSql = self.dBlockTmpl[self.tabName]
        # sql = dTabSql['SQL']
        # dTabFields = copy.deepcopy(self.dFields)
        bsSql = BsSql(dTabSql, self)
        bsSql.getField()
        sql = self.sqlReplaceValue(dTabSql['SQL'])
        # sql = copy.deepcopy(dTabSql['SQL'])
        # for f in self.dFields:
        #     pat = '^<%s^>' % f
        #     sql = sql.replace(pat, str(self.dFields[f]))
        confSql = [dTabSql['COMMENT'], sql]
        return confSql

    def sqlReplaceValue(self, sql):
        sqlDest = copy.deepcopy(sql)
        patt = re.compile(r'\^<(.+?)\^>')
        aMatch = patt.findall(sqlDest)
        print('replace sql: %s' % sql)
        print('fields: %s' % self.dFields)
        print(aMatch)
        for m in aMatch:
            pat = '^<%s^>' % m
            val = self.getField(m)
            print('replace field: %s with %s' % (m, val))
            sqlDest = sqlDest.replace(pat, str(val))
        # print('check sql: %s' % sqlDest)
        return sqlDest

    def checkExist(self):
        sql = self.sqlReplaceValue(dTabCheck[self.tabName])
        print('check sql: %s' % sql)
        val = RawSql(sql).fetchVal()
        if val:
            print('%s exist.' % val)
            return val
        return None

    def getField(self, fieldName):
        if fieldName in self.dFields:
            return self.dFields[fieldName]
        if self.parent:
            return self.parent.getField(fieldName)
        return None

    def getSql(self):
        aSql = []
        if self.sql:
            aSql.append(self.sql)
        for ch in self.children:
            subSql = ch.getSql()
            if subSql:
                aSql.extend(subSql)
        if len(aSql) == 0:
            return None
        return aSql


class Table(TableComp):
    def __init__(self, name, data, parent):
        super().__init__(name, data, parent.blockName, parent)


class TableBlock(TableComp):
    def __init__(self, name, data):
        super().__init__(name, data, name)


class BsSql(object):
    def __init__(self, dTabSql, table):
        self.dTabSql = dTabSql
        self.table = table

    def getField(self):
        # sql = self.dTabSql['SQL']
        # sql = copy.deepcopy(self.dTabSql['SQL'])
        if 'FIELDS' not in self.dTabSql:
            # self.dTabSql['FIELDS'] = None
            print('dTabSql no FIELDS')
            return self.dTabSql
        dTplFields = self.dTabSql['FIELDS']
        for field in dTplFields:
            # fValue = self.table.getField(field)
            # if fValue:
            #     continue
            print('get field: %s' % field)
            val = None
            if field == 'MIS_GROUP_NO_PAT':
                print('get MIS_GROUP_NO by %s' % self.table.getField(field))
                speField = MisGroupNo(field, self.table.getField(field))
                # val = speField.getVal()
            elif field == 'COND_ID':
                print('get cond_id of promo_id %s' % self.table.getField('PROMO_ID'))
                speField = CondId(field, self.table.getField('PROMO_ID'))
                # val = speField.getVal()
            elif field == 'NEW_SMS_TEMPLET_ID':
                speField = SmsId(field)
            else:
                # print('common special field: %s' % field)
                speField = SpecialField(field)
            val = speField.getNext()

            if field == 'MIS_GROUP_NO_PAT':
                print('get %s %08d' % ('MIS_GROUP_NO', int(val)))
                self.table.dFields[field] = val
            else:
                print('get %s %d' % (field, val))
                self.table.dFields[field] = val


class SpecialField(object):
    def __init__(self, fieldName):
        self.fieldName = fieldName
        self.itemName = fieldName
        # self.type = type
        self.sqlDev = None
        self.sqlPrd = None
        self.curVal = None
        if fieldName in dFieldSql:
            self.sqlDev = dFieldSql[fieldName][0]
            self.sqlPrd = dFieldSql[fieldName][1]
        print('%s : %s' % (self.fieldName, self.sqlDev))

    def getVal(self):
        # idT1 = PromoIdExist.objects.using('').filter(id__startswith='203').first().id
        idT1 = int(RawSql(self.sqlDev).fetchVal())
        idT2 = int(RawSql(self.sqlDev, 'test2').fetchVal())
        # idT3 = RawSql(self.sqlPrd,'prod').fetchVal()
        idT3 = 0
        print('item name: %s' % self.itemName)
        idT4 = BsItemId.objects.filter(item_name=self.itemName).aggregate(Max('item_id'))['item_id__max']
        if not idT4:
            idT4 = 0
        self.curVal = max(idT1, idT2, idT3, idT4)

    def getNext(self):
        self.getVal()
        if not self.curVal:
            return None
        nextVal = self.curVal + 1
        itemId = BsItemId.create(self.itemName, nextVal)
        itemId.save()
        return nextVal

# class PromoId(SpecialField):
#     def getVal(self):
#         # idT1 = PromoIdExist.objects.using('').filter(id__startswith='203').first().id
#         idT1 = RawSql(promoSql).fetchVal()
#         idT2 = RawSql(promoSql,'test2').fetchVal()
#         # idT3 = RawSql(promoSqlProd,'prod').fetchVal()
#         idT3 = 0
#         idT4 = BsItemId.objects.filter(item_name=self.name).aggregate(Max('item_id'))['item_id__max']
#         if not idT4:
#             idT4 = 0
#         self.curVal = max(idT1, idT2, idT3, idT4)

class CondId(SpecialField):
    def __init__(self, fieldName, promoId):
        super().__init__(fieldName)
        self.promoId = promoId

    def getVal(self):
        idT4 = BsItemId.objects.filter(item_name=self.fieldName, item_id__startswith=self.promoId).aggregate(Max('item_id'))['item_id__max']
        if not idT4:
            idT4 = int('%s00' % self.promoId)
        self.curVal = idT4


class SmsId(SpecialField):
    def getVal(self):
        super().getVal()
        # nextVal = self.curVal + 1
        # print('smsid nextVal:%d' % nextVal)
        # idSeq = int(RawSql(smsSeqSql).fetchVal())
        # print('smsid seq: %d' % idSeq)
        # if nextVal > idSeq:
        #     step = nextVal - idSeq
        #     seqJump = SequenceJump('base.bs_DEF_SMS_TEMPLATE$SEQ', step)
        #     seqJump.jump()
        # else:
        #     self.curVal = idSeq - 1


class MisGroupNo(SpecialField):
    def __init__(self, fieldName, misGroupNoPat):
        super().__init__(fieldName)
        self.itemName = '%s%s' % (fieldName, misGroupNoPat[:2])
        self.misGroupNoPat = misGroupNoPat
        if self.sqlDev:
            self.sqlDev = self.sqlDev % self.misGroupNoPat
        if self.sqlPrd:
            self.sqlPrd = self.sqlPrd % self.misGroupNoPat
        print('%s : %s' % (self.fieldName, self.sqlDev))

    def getVal(self):
        super().getVal()
        if self.curVal == 0:
            self.curVal = int('%s011000' % self.misGroupNoPat[:2])

    def getNext(self):
        self.getVal()
        if not self.curVal:
            return None
        nextVal = self.curVal + 1

        itemId = BsItemId.create(self.itemName, nextVal)
        itemId.save()
        rtVal = '%08d' % nextVal
        return rtVal


class ReceiptType(SpecialField):
    def getVal(self):
        pass



def getSql(table, dFields, dSql):
    if table not in dSql:
        return None
    dTab = dSql[table]
    sql = dTab['SQL']
    for f in dFields:
        pat = '^<%s^>' % f
        sql = sql.replace(pat, str(dFields[f]))
    return sql

def parseTpl(content, dFields, dSql):
    for tName in content:
        table = content[tName]
        parseTab(tName,table,dFields, dSql)


def parseTab(name, content, dFields, dSql):
    aSubTable = []
    for field in content:
        val = content[field]
        if type(val) is list:
            for it in val:
                aSubTable.append({field: it})
        elif type(val) is dict:
            aSubTable.append({field: val})
        else:
            dFields[field] = val
    sql = getSql(name,dFields, dSql)
    if sql:
        print(sql)
    for sub in aSubTable:
        for tName in sub:
            tab = sub[tName]
            parseTab(tName, tab, dFields, dSql)

def makeSql(data, template):
    tplFile = os.path.join(settings.BASE_DIR, 'bsconf', 'data', 'template', template)
    inFile = os.path.join(settings.BASE_DIR, 'bsconf', 'data', 'template', data)
    # , encoding = 'utf-8'
    with open(tplFile) as fp:
        dSql = json.load(fp)
    with open(inFile) as fData:  #,encoding='utf-8'
        dIn = json.load(fData)

    aSql = []
    for req in dIn:
        reqData = dIn[req]
        for tplGrp in reqData:
            if tplGrp not in dSql:
                print('%s no sql' % tplGrp)
                break
            dTplSql = dSql[tplGrp]
            tplGrpData = reqData[tplGrp]
            for i in range(len(tplGrpData)):
                tpl = tplGrpData[i]
                dFields = {}
                ss = parseTpl(tpl, dFields, dTplSql)
    return dSql,dIn

