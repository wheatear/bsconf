from django.shortcuts import render
from boss import settings
import os,logging
import json

# Create your views here.
def makeSql(data, template):
    tplFile = os.path.join(settings.BASE_DIR, 'bsconf', 'data', 'template', template)
    inFile = os.path.join(settings.BASE_DIR, 'bsconf', 'data', 'template', data)
    with open(tplFile,encoding='utf-8') as fp:
        dSql = json.load(fp,encoding='utf-8')
    with open(inFile,encoding='utf-8') as fData:
        dIn = json.load(fData)
    dFields = {}
    ss = parseJson('root', dIn, dFields, dSql)
    return dSql,dIn

def getSql(table, dFields, dSql):
    if table not in dSql:
        return None
    sql = dSql[table]
    for f in dFields:
        pat = '^<%s^>' % f
        sql = sql.replace(pat, str(dFields[f]))
    return sql

def parseJson(name, content, fields, dSql):
    children = []
    for key in content:
        val = content[key]
        if type(val) is list:
            for it in val:
                children.append({key: it})
        elif type(val) is dict:
            children.append({key: val})
        else:
            fields[key] = val
    sql = getSql(name,fields, dSql)
    if sql:
        print(sql)
    for ch in children:
        for key in ch:
            parseJson(key, ch[key], fields, dSql)


