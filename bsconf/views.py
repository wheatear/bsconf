from django.shortcuts import render
from boss import settings
import os,logging
import json
import copy

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
            table = self.blockData[tName]
            if table not in self.dTplSql:
                print('%s no sql tamplate' % table)
                break
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
        sql = copy.deepcopy(dTabSql['SQL'])
        for f in self.dFields:
            pat = '^<%s^>' % f
            sql = sql.replace(pat, str(self.dFields[f]))
        return sql


class BsSql(object):
    def __init__(self, dTabSql):
        self.dTabSql = dTabSql

    def makeSql(self):
        # sql = self.dTabSql['SQL']
        sql = copy.deepcopy(self.dTabSql['SQL'])
        dFields = None
        if 'FIELDS' in self.dTabSql:
            dFields = self.dTabSql['FIELDS']
        if not dFields:
            return sql
        for field in dFields:
            val = None
            if field == 'PROMO_ID':
                speField = PromoId(field, dFields[field])
                val = speField.getVal()
            pat = '^<%s^>' % field
            sql = sql.replace(pat, str(self.dFields[f]))


class SpecialField(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def getVal(self):
        pass

class PromoId(SpecialField):
    def __init__(self):
        pass


class ContId(SpecialField):
    def __init__(self):
        pass


class SmsId(SpecialField):
    def __init__(self):
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

