from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import FileResponse

import time, re
import datetime
from boss import settings
import os,logging
import json
import copy
import glob
from bsconf.models import *
from django.db.models import Max

# Create your views here.

logger = logging.getLogger('django')
errlog = logging.getLogger('error')


def index(request):
    # request.session['ip'] = ip
    # extra = getExtra(request)
    # logger = LoggerAdapter(initLogger,extra)

    # logger.info('access',extra)
    aMonth = getMonthes()
    context = {'aMonth': aMonth}
    return render(request, 'bsconf/index.html', context)

def getMonthes():
    # tNow = time.localtime()
    month = time.strftime('%Y%m', time.localtime())
    # tNow = datetime.datetime.now()
    aMonth = []
    for i in range(6):
        newTime = str(int(month) - i)
        if newTime.endswith('00'):
            month = str(int(newTime[:4]) - 1) + str(int(month[-2:]) + 12)
            newTime = str(int(month) - i)
        aMonth.append(newTime)
    return aMonth

def configer(request):
    aMonth = getMonthes()
    dJsonTpl = loadJsonTpl()
    context = {'aMonth': aMonth,
               'aBlockName': dJsonTpl.keys()}
    return render(request, 'bsconf/bsqEditer.html', context)

def getDataTpl(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        logger.debug(request.POST)
        aBlockName =request.POST.getlist("blockName[]", [])
        logger.debug("request block tpl: %s", aBlockName)
        dJsonTpl = loadJsonTpl()
        dDataTpl = {}
        for block in aBlockName:
            if block in dJsonTpl:
                dDataTpl[block] = dJsonTpl[block]
        logger.debug("resp: %s", dDataTpl)
        return JsonResponse(dDataTpl)

def loadJsonTpl():
    dJsonTpl = {}
    tplFile = os.path.join(settings.TPL_DIR, 'tpldata*.json')
    for file in glob.glob(tplFile):
        logger.debug('load file %s', file)
        with open(file) as jf:
            jsonBlock = json.load(jf)
        logger.debug(jsonBlock)
        for req in jsonBlock:
            dJsonTpl.update(jsonBlock[req])
    logger.info(dJsonTpl)
    return dJsonTpl

def uploadMakeSql(request):
    logger.info('upload json')
    bsf = _uploadJson(request)
    logger.info('upload %s ok.',bsf.inFile)
    logger.info('make sql for %s', bsf.inFile)
    sqlFile = _makeSql(bsf)
    downPath = 'static/bsconf/out/%s' % bsf.month
    result = {
        "sqlFile": bsf.outFile,
        "downPath": downPath,
        "errCode": bsf.bsReq.state,
        "errDesc": bsf.getReqErrDesc()
    }
    logger.info('make sql %s %s result: errCode: %s; errDesc: %s', downPath, sqlFile, bsf.chkSts, bsf.chkDesc)
    return JsonResponse(result)
        # return bsf.downLoad()
        # return JsonResponse(bsf.dInData)
        # bsf.start()
        # return HttpResponse("upload %s over!" % jsonName)

def saveJson(request):
    logger.info('upload json')
    jsonName = _uploadJson(request)
    logger.info('upload %s ok.', jsonName)
    return JsonResponse({"rep": 'ok'})

def _uploadJson(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        jsonFile =request.FILES.get("jsonFile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not jsonFile:
            return HttpResponse("no files for upload!")
        jsonName = jsonFile.name
        month = request.POST.get("month", None)
        if not month:
            month = time.strftime('%Y%m', time.localtime())
        reqType = request.POST.get("type",'ZG')
        author = request.POST.get("author", '王新田')

        if not jsonName.startswith(reqType):
            jsonName = '%s-%s' % (reqType, jsonName)
        bsf = BsConfiger(jsonName, reqType, author, month)
        bsf.saveReqSts('0')

        # destination = open(os.path.join(settings.IN_DIR, month, jsonName),'wb+')    # 打开特定的文件进行二进制的写操作
        jsonDir = os.path.join(settings.IN_DIR, month)
        if not os.path.exists(jsonDir):
            os.makedirs(jsonDir)
        with open(os.path.join(jsonDir, jsonName),'wb+') as destination:
            for chunk in jsonFile.chunks():      # 分块写入文件
                destination.write(chunk)
        # destination.close()
        bsf.saveReqSts('1')
        return bsf

def openReqConf(request):
    logger.info('open req conf')
    if request.method == "POST":    # 请求方法为POST时，进行处理
        reqName = request.POST.get("reqName", None)
        reqType = request.POST.get("type", 'ZG')
        author = request.POST.get("author", '王新田')
        month = request.POST.get("month", None)

        if not month:
            month = time.strftime('%Y%m', time.localtime())
        reqJson = reqName.replace('BOSS需求解决方案-', '')
        reqJson = reqJson.replace('需求解决方案-', '')
        jsonName = '%s-%s-%s.json' % (reqType, reqJson, author)
        # if not reqName.startswith(reqType):
        #     jsonName = '%s-%s-%s.json' % (reqType, reqJson, author)

        # destination = open(os.path.join(settings.IN_DIR, month, jsonName),'wb+')    # 打开特定的文件进行二进制的写操作
        jsonDir = os.path.join(settings.IN_DIR, month)
        jFile = os.path.join(jsonDir, jsonName)
        logger.debug('open json: %s', jFile)
        if not os.path.exists(jsonDir):
            os.makedirs(jsonDir)
        # destination.close()
        jsonCont = {reqName: {}}
        if os.path.exists(jFile):
            with open(jFile) as fData:  # ,encoding='utf-8'
                jsonCont = json.load(fData)
        return JsonResponse(jsonCont)

def _makeSql(bsf):
    # bsf = BsConfiger(bsReq, type=bsReq.conf_type)
    return bsf.start()
    # return JsonResponse({"rep": "ok"})

def makeBsSql(request):
    logger.info('request: %s %s from', request.method, request.path)
    if request.method == "POST":    # 请求方法为POST时，进行处理
        logger.debug(request.POST)
        jsonStr = request.POST.get("reqJson", None)
        reqJson = json.loads(jsonStr)
        reqName = request.POST.get("reqName", None)
        month = request.POST.get("month", None)
        if not month:
            month = time.strftime('%Y%m', time.localtime())
        reqType = request.POST.get("type",'ZG')
        author = request.POST.get("author", '王新田')
        logger.debug("json: %s", json.dumps(reqJson))
        reqName = reqName.replace('BOSS需求解决方案-', '')
        reqName = reqName.replace('需求解决方案-', '')
        jsonName = '%s-%s-%s.json' % (reqType, reqName, author)
        bsf = BsConfiger(jsonName, reqType, author, month)
        bsf.saveReqSts('0')

        jsonDir = os.path.join(settings.IN_DIR, month)
        if not os.path.exists(jsonDir):
            os.makedirs(jsonDir)
        with open(os.path.join(jsonDir, jsonName), 'w') as jf:
            jf.write(jsonStr)
        # destination.close()
        bsf.saveReqSts('1')

        logger.info('upload %s ok.', bsf.inFile)
        logger.info('make sql for %s', bsf.inFile)
        sqlFile = _makeSql(bsf)
        downPath = 'static/bsconf/out/%s' % bsf.month
        result = {
            "sqlFile": bsf.outFile,
            "downPath": downPath,
            "errCode": bsf.bsReq.state,
            "errDesc": bsf.getReqErrDesc()
        }
        logger.info('make sql %s %s result: errCode: %s; errDesc: %s', downPath, sqlFile, bsf.chkSts, bsf.chkDesc)
        return JsonResponse(result)

    if request.method == "GET":    # 请求方法为POST时，进行处理
        jsonName = request.GET['jsonName']
        bsf = BsConfiger(jsonName)
        bsf.start()
        return JsonResponse( {"rep": "ok"})

def qryJsonFile(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        logger.debug(request.POST)
        reqName = request.POST.get("reqName", None)
        month = request.POST.get("month", None)
        if not month:
            month = time.strftime('%Y%m', time.localtime())
        reqType = request.POST.get("type",'ZG')
        author = request.POST.get("author", '王新田')

        reqName = reqName.replace('BOSS需求解决方案-', '')
        reqName = reqName.replace('需求解决方案-', '')
        jsonName = '%s-%s-%s.json' % (reqType, reqName, author)
        logger.debug("query request: %s")
        jsonDir = os.path.join(settings.IN_DIR, month)
        jsonFile = os.path.join(jsonDir, jsonName)
        if os.path.exists(jsonFile):
            with open(jsonFile) as fData:  # ,encoding='utf-8'
                jsonCont = json.load(fData)
            dResp = {"jsonFile": jsonFile,
                     "jsonData": jsonCont}
            return JsonResponse(dResp)
        else:
            return JsonResponse({"jsonFile": None})

def qryRequirement(request):
    logger.info('query requirement')
    jsonMonth = None
    jsonType = None
    if request.method == 'GET':
        jsonType = request.GET.get('type','ZG')
        jsonMonth = request.GET.get('month',None)
        jsonAuthor = request.GET.get('author', None)
    if not jsonMonth:
        jsonMonth = time.strftime('%Y%m', time.localtime())
    bsReq = BsconfRequirement.objects.filter(conf_type=jsonType, req_month=jsonMonth, author=jsonAuthor).values()
    aReq = []
    for r in bsReq:
        aReq.append(r)
    return JsonResponse({'bsReq': aReq})

def download(request):
  file=open('crm/models.py','rb')
  response =FileResponse(file)
  response['Content-Type']='application/octet-stream'
  response['Content-Disposition']='attachment;filename="models.py"'
  return response


class BsConfiger(object):
    tplSqlFile = "tplsql_promo.json"
    dTplSql = {}
    # jsonName, reqType, author, month
    def __init__(self, inFile, type='ZG', author='王新田', month=None):
        self.bsReq = BsconfRequirement.create(inFile, type, author, month)
        self.inFile = inFile
        # logger.debug('json file: %s', self.inFile)
        if not month:
            month = time.strftime('%Y%m', time.localtime())
        self.month = month
        self.type = type
        self.author = author
        logger.info('in data file %s' % inFile)
        self.outFile = None
        self.outFull = None
        self.dInData = {}
        self.fOut = None
        self.chkSts = ''
        self.chkDesc = ''

    def saveReqSts(self, sts='0'):
        self.bsReq.state = sts
        self.bsReq.save()

    def getReqErrDesc(self):
        aSts = self.bsReq.state.split(',')
        errDesc = ''
        for s in aSts:
            errDesc = "%s%s" % (errDesc, dBsReqState[s])
        return errDesc

    def checkReq(self):
        pass

    def start(self):
        # self.bsReq.state = 1
        self.bsReq.save()
        logger.info('load sql template')
        self.loadTplSql()
        logger.info('load data')
        self.loadData()
        # self.openOutFile()
        logger.info('parse in file')
        self.parseDoc()
        # self.bsReq.sql_file = self.outFile
        # self.bsReq.state = 8
        # self.bsReq.save()
        return self.outFull

    def loadTplSql(self):
        if len(BsConfiger.dTplSql) > 0:
            return
        logger.info('load template sql %s', self.tplSqlFile)
        file = os.path.join(settings.TPL_DIR, self.tplSqlFile)
        with open(file) as fp:
            BsConfiger.dTplSql = json.load(fp)

    def loadData(self):
        # IN_DIR = os.path.join(BASE_DIR, 'bsconf', 'data', 'in')
        file = os.path.join(settings.IN_DIR, self.month, self.inFile)
        with open(file) as fData:  # ,encoding='utf-8'
            self.dInData = json.load(fData)
        # confReq = BsconfRequirement.create(self.inFile, self.type)
        # confReq.save()

    def parseDoc(self):
        logger.info('parse json file %s', self.inFile)
        aSql = []

        for req in self.dInData:
            logger.info('parse requirement %s' % req)
            # self.openOutFile()
            # self.fOut.write('-- %s%s' % (req, os.linesep))
            reqData = self.dInData[req]
            reqParser = ReqParser(self, req, reqData)
            reqParser.parseDocName()
            self.outFile = reqParser.outName
            self.bsReq.sql_file = reqParser.outName
            reqParser.parse('sts')
            self.chkSts = reqParser.chkSts
            self.chkDesc = reqParser.chkDesc
            if len(reqParser.chkSts) > 0:
                self.chkSts = ','.join(reqParser.chkSts)
                self.bsReq.state = self.chkSts
                self.bsReq.remark = reqParser.chkDesc
                self.bsReq.save()
                return self.chkSts
            self.bsReq.state = '2'
            self.bsReq.save()

            reqParser.parse('sql')
            self.bsReq.state = '7'
            self.bsReq.save()
            # self.outFull = os.path.join(settings.OUT_DIR, self.month, self.outFile)
            # reqSet = BsconfRequirement.objects.filter(json_file=self.inFile, conf_type=self.type, req_month=self.month)
            # for bsReq in reqSet:
            #     bsReq.sql_file = confReq.outName
            #     bsReq.state = 8
            #     bsReq.save()

    def downLoad(self):
        logger.info('download file %s', self.outFile)
        fileName = os.path.join(settings.OUT_DIR, self.month, self.outFile)
        file = open(fileName, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="models.py"'
        return response

    # def closeOut(self):
    #     self.fOut.close()


class ReqParser(object):
    def __init__(self, configer, reqName, reqData):
        self.configer = configer
        self.reqName = reqName
        self.reqData = reqData
        self.reqId = None
        # self.reqName = None
        self.outName = None
        self.fOut = None
        self.chkSts = []
        self.chkDesc = ''

    def parseDocName(self):
        docBase = os.path.splitext(os.path.basename(self.reqName))[0]
        docBase = docBase.replace('BOSS需求解决方案-','')
        self.reqName = docBase.replace('需求解决方案-', '')
        self.outName = '%s-%s-%s.sql' % (self.configer.type, self.reqName, self.configer.author)

    def openOut(self):
        if self.fOut:
            return self.fOut
        print('open out file %s' % self.outName)
        sqlDir = os.path.join(settings.OUT_DIR, self.configer.month)
        if not os.path.exists(sqlDir):
            os.makedirs(sqlDir)
        file = os.path.join(sqlDir, self.outName)
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

    # def checkReq(self):
    #     chkResult = {}
    #
    #     for block in self.reqData:
    #         if block not in self.configer.dTplSql:
    #             print('%s no sql template' % block)
    #             continue
    #         dBlockSql = self.configer.dTplSql[block]
    #         dBlockData = self.reqData[block]
    #         for i in range(len(dBlockData)):
    #             logger.info('check %s %d' % (block, i+1))
    #             blockData = dBlockData[i]
    #             # dFields = {}
    #             block = TableBlock(block, blockData)
    #             block.parse()
    #             self.writeBlockSql(block, i + 1)
    #

    def parse(self, type='sts'):
        if type == 'sql':
            self.openOut()
            self.fOut.write('-- %s%s' % (self.reqName, os.linesep))
        for blockGrp in self.reqData:
            logger.info('parse block group %s ...' % blockGrp)
            if blockGrp not in self.configer.dTplSql:
                logger.info('%s no sql template' % blockGrp)
                break
            dBlockSql = self.configer.dTplSql[blockGrp]
            blockGrpData = self.reqData[blockGrp]
            for i in range(len(blockGrpData)):
                logger.info('%s %d' % (blockGrp, i+1))
                blockData = blockGrpData[i]
                # dFields = {}
                block = TableBlock(blockGrp, blockData)
                block.parse(type)
                if type == 'sts':
                    self.setChkSts(block)
                elif type == 'sql':
                    self.writeBlockSql(block, i + 1)
                # ss = self.parseBlock(tpl, dFields, dTplSql)
            logger.info('block group %s of %d completed' % (blockGrp, len(blockGrpData)))
        if type == 'sql':
            self.fOut.write('%scommit;%s' % (os.linesep, os.linesep))
            self.closeOut()

    def setChkSts(self, block):
        aChk = block.getCheck()
        logger.info('chkSts: %s', aChk[0])
        logger.info('chkDesc: %s', aChk[1])
        for s in aChk[0]:
            if s not in self.chkSts:
                self.chkSts.append(s)
        self.chkDesc = aChk[1]

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
        self.chkSts = []
        self.chkDesc = ''

    def parse(self, ptype='sql'):
        logger.info('parse table of %s' % self.tabName)
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

        if ptype == 'sql':
            logger.debug('make sql of table %s' % self.tabName)
            sql = self.makeSql()
            # print(sql)
            self.sql = sql
        elif ptype == 'sts':
            logger.debug('check status of table %s' % self.tabName)
            self.checkSts()

        for subTab in self.children:
            subTab.parse(ptype)
        logger.info('parse table %s complate' % self.tabName)

    def checkSts(self):
        if self.tabName == self.blockName:
            return
        if self.tabName not in self.dBlockTmpl:
            logger.error('%s not in block template %s' % (self.tabName, self.blockName))
            self.chkSts.append('-1')
            self.chkDesc = '%s%s; ' % (self.chkDesc, self.tabName)
        allChkVal = dCheckTabSts['ALL']['ALL'][0]
        allChkSts = dCheckTabSts['ALL']['ALL'][1]
        for f in self.dFields:
            if type(self.dFields[f]) is not str:
                continue
            if self.dFields[f].find(allChkVal) > -1:
                if allChkSts not in self.chkSts:
                    self.chkSts.append(allChkSts)
        if self.tabName not in dCheckTabSts:
            return
        dChkField = dCheckTabSts[self.tabName]
        for f in self.dFields:
            if f in dChkField:
                if type(self.dFields[f]) is not str:
                    continue
                if self.dFields[f].find(dChkField[f][0]) > -1:
                    sts = dChkField[f][1]
                    if sts not in self.chkSts:
                        self.chkSts.append(sts)
        logger.info('check status %s complete.', self.tabName)

    def makeSql(self):#, self.dFields, self.dTplSql
        if self.tabName == self.blockName:
            return
        if self.tabName not in self.dBlockTmpl:
            logger.info('%s not in block template %s' % (self.tabName, self.blockName))
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

    def getCheck(self):
        aChk = self.chkSts
        chkDesc =self.chkDesc
        # if self.chkSts:
        #     aChk.extend(self.chkSts)
        for ch in self.children:
            chk = ch.getCheck()
            subSts = chk[0]
            chkDesc = '%s,%s' % (chkDesc, chk[1])
            for s in subSts:
                if s not in aChk:
                    aChk.append(s)
        return (aChk, chkDesc)


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
            logger.debug('get field: %s' % field)
            val = None
            if field == 'MIS_GROUP_NO_PAT':
                logger.debug('get MIS_GROUP_NO by %s' % self.table.getField(field))
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
        idT1 = 0
        idT2 = 0
        idT3 = 0
        t1 = RawSql(self.sqlDev).fetchVal()
        if t1:
            idT1 = int(t1)
        t2 = RawSql(self.sqlDev, 'test2').fetchVal()
        if t1:
            idT2 = int(t2)
        # idT3 = RawSql(self.sqlPrd,'prod').fetchVal()
        idT3 = 0
        logger.debug('item name: %s' % self.itemName)
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
        if self.sqlDev:
            self.sqlDev = self.sqlDev % self.promoId
        if self.sqlPrd:
            self.sqlPrd = self.sqlPrd % self.promoId
        logger.debug('%s : %s', self.fieldName, self.sqlDev)

    def getVal(self):
        idT1 = 0
        idT2 = 0
        idT3 = 0
        t1 = RawSql(self.sqlDev).fetchVal()
        if t1:
            idT1 = int(t1)
        t2 = RawSql(self.sqlDev, 'test2').fetchVal()
        if t1:
            idT2 = int(t2)
        # idT3 = RawSql(self.sqlPrd,'prod').fetchVal()
        idT3 = 0
        idT4 = BsItemId.objects.filter(item_name=self.fieldName, item_id__startswith=self.promoId).aggregate(Max('item_id'))['item_id__max']
        if not idT4:
            idT4 = int('%s00' % self.promoId)
        self.curVal = max(idT1, idT2, idT3, idT4)


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

