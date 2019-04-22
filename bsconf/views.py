from django.shortcuts import render
from boss import settings
import os,logging
import json

# Create your views here.
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

