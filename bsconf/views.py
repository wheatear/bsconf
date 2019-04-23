from django.shortcuts import render
from boss import settings
import os,logging
import json
import copy
from bsconf.models import *
from django.db.models import Max

# Create your views here.

class BsConfiger(object):
    tplSqlFile = "tplsql_promo.json"
    dTplSql = {}
    def __init__(self, inFile):
        self.inFile = inFile
        # self.outFile = 'DB配置-%s-王新田.sql' % inFile
        self.outFile = '%s.sql' % os.path.splitext(os.path.basename(inFile))[1]
        self.dInData = {}
        self.fOut = None

    def loadTplSql(self):
        file = os.path.join(settings.TPL_DIR, self.tplSqlFile)
        with open(file) as fp:
            BsConfiger.dTplSql = json.load(fp)

    def loadData(self):
        file = os.path.join(settings.IN_DIR, self.inFile)
        with open(file) as fData:  # ,encoding='utf-8'
            self.dInData = json.load(fData)

    def openOutFile(self):
        if self.fOut:
            return self.fOut
        file = os.path.join(settings.OUT_DIR, self.outFile)
        try:
            self.fOut = open(file, 'w')
        except IOError as e:
            print("can't open file %s." % file)

    def parseDoc(self):
        aSql = []
        self.openOutFile()
        for req in self.dInData:
            reqData = self.dInData[req]
            for blockGrp in reqData:
                if blockGrp not in self.dTplSql:
                    print('%s no sql' % blockGrp)
                    break
                dBlockSql = self.dTplSql[blockGrp]
                blockGrpData = reqData[blockGrp]
                for i in range(len(blockGrpData)):
                    blockData = blockGrpData[i]
                    # dFields = {}
                    block = BsBlock(blockGrp, blockData, dBlockSql)
                    aSql = block.parse()
                    # ss = self.parseBlock(tpl, dFields, dTplSql)
        self.closeOut()

    def writeSql(self, block):
        self.fOut.write('-- %s%s' % (block.blockName, os.linesep))
        for sql in block.aSql:
            self.fOut.write('%s%s' % (sql, os.linesep))

    def closeOut(self):
        self.fOut.close()

class BsBlock(object):
    def __init__(self, blockName, blockData, dTplSql):
        self.blockName = blockName
        self.blockData = blockData
        self.dFields = {}
        self.dTplSql = dTplSql
        self.aSql = []

    def parse(self):
        for tName in self.blockData:
            if tName not in self.dTplSql:
                print('%s no sql tamplate' % tName)
                break
            table = self.blockData[tName]
            self.parseTab(tName, table) #, self.dFields, self.dTplSql

    def parseTab(self, tName, table):
        aSubTable = []
        for field in table:
            val = table[field]
            if type(val) is list:
                for it in val:
                    aSubTable.append({field: it})
            elif type(val) is dict:
                aSubTable.append({field: val})
            else:
                self.dFields[field] = val
        sql = self.getSql(tName)
        if sql:
            self.aSql.append(sql)
        for sub in aSubTable:
            for tName in sub:
                tab = sub[tName]
                parseTab(tName, tab)

    def getSql(self, table):#, self.dFields, self.dTplSql
        if table not in self.dTplSql:
            return None
        dTabSql = self.dTplSql[table]
        # sql = dTabSql['SQL']
        bsSql = BsSql(dTabSql, self.dFields)
        bsSql.makeSql()
        sql = copy.deepcopy(dTabSql['SQL'])
        for f in self.dFields:
            pat = '^<%s^>' % f
            sql = sql.replace(pat, str(self.dFields[f]))
        return sql


class BsSql(object):
    def __init__(self, dTabSql, dTabData):
        self.dTabSql = dTabSql
        self.dTabData = dTabData

    def makeSql(self):
        # sql = self.dTabSql['SQL']
        # sql = copy.deepcopy(self.dTabSql['SQL'])
        if 'FIELDS' not in self.dTabSql:
            self.dTabSql['FIELDS'] = None
            return self.dTabSql
        dFields = self.dTabSql['FIELDS']
        for field in dFields:
            if field in self.dTabData:
                continue
            val = None
            if field == 'PROMO_ID':
                speField = PromoId(field)
                # val = speField.getVal()
            elif field == 'COND_ID':
                speField = ContId(field, self.dTabData['PROMO_ID'])
                # val = speField.getVal()
            elif field == 'NEW_SMS_TEMPLET_ID':
                speField = SmsId(field)
            val = speField.getNext()
            self.dTabData[field] = val


class SpecialField(object):
    def __init__(self, name):
        self.name = name
        # self.type = type
        self.curVal = None

    def getVal(self):
        pass

    def getNext(self):
        self.getVal()
        if not self.curVal:
            return None
        nextVal = self.curVal + 1
        itemId = BsItemId.create(self.name, nextVal)
        itemId.save()
        return nextVal

class PromoId(SpecialField):
    def getVal(self):
        # idT1 = PromoIdExist.objects.using('').filter(id__startswith='203').first().id
        idT1 = RawSql(promoSql).fetchVal()
        idT2 = RawSql(promoSql,'test2').fetchVal()
        idT3 = RawSql(promoSqlProd,'prod').fetchVal()
        idT4 = BsItemId.objects.filter(item_name=self.name).aggregate(Max('item_id')).item_id
        self.curVal = max(idT1, idT2, idT3, idT4)

class ContId(SpecialField):
    def __init__(self, name, promoId):
        super().__init__(name)
        self.promoId = promoId

    def getVal(self):
        idT4 = BsItemId.objects.filter(item_name=self.name, item_id__startswith=self.promoId).aggregate(Max('item_id')).item_id
        self.curVal = idT4


class SmsId(SpecialField):
    def getVal(self):
        idSeq = RawSql(smsSeqSql).fetchVal()
        idT1 = RawSql(promoSql).fetchVal()
        idT2 = RawSql(promoSql, 'test2').fetchVal()
        idT3 = RawSql(promoSqlProd, 'prod').fetchVal()
        idT4 = BsItemId.objects.filter(item_name=self.name).aggregate(Max('item_id')).item_id
        curVal = max(idT1, idT2, idT3, idT4)
        nextVal = curVal + 1
        if nextVal > idSeq:
            step = nextVal - idSeq
            seqJump = SequenceJump('base.bs_DEF_SMS_TEMPLATE$SEQ', step)
            seqJump.jump()
        self.curVal = idSeq - 1

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

