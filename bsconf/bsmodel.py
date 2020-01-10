from django.db import models,connection,connections
import time, logging
# import bsconf.oraorm as orm
import oradb
import oraorm as orm

class BS_PROD_INFO(orm.Model):
    __table__ = 'BASE.BS_PROD_INFO'
    PROD_ID = orm.IntegerField(ddl='NUMBER(15)', primary_key=True)
    PROD_NAME = orm.StringField(ddl='VARCHAR2(64)')
    BASE_VALUE = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_TYPE = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_ID = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_COUNT = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_UNIT = orm.StringField(ddl='VARCHAR2(4000)')




if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    # oradb.create_engine('www-data', 'www-data', 'test')
    # oradb.update('drop table if exists user')
    # oradb.update('create table user (id int primary key, name text, email text, passwd text, last_modified real)')
    # import doctest
    # doctest.testmod()

    dbConf = {'user': 'kt4', 'password': 'kt4', 'host': '10.7.5.164', 'port': 1521, 'sid': 'ngtst02', 'service_name': ''}
    ktdb = oradb.Db(dbConf)

    BS_PROD_INFO.db = ktdb

    prod = BS_PROD_INFO(PROD_ID='50002379', PROD_NAME='经济版', BASE_VALUE='588', FREEBIE_TYPE='0',FREEBIE_ID='66660000', FREEBIE_COUNT='3000', FREEBIE_UNIT='01')
    sql = prod.get_insert_sql()
    print(sql)

    # orm.Tmp_ps.db = ktdb
    # sql = 'select sysdate from dual'
    # with ktdb:
    #     sysdate = ktdb.select_one('select sysdate from dual')
    #     logging.info(sysdate)
    #
    #     pk = {'ps_id': 103258}
    #     tmp_ps = orm.Tmp_ps.get(pk)
    #     logging.info('type: %s' % type(tmp_ps))
    #     print(tmp_ps)
    #     print('ps_id: %d, bill_id: %s, ps_param: %s' % (tmp_ps.ps_id, tmp_ps.bill_id, tmp_ps.ps_param))
    #     tmp_ps.ps_param += ' test;'
    #     tmp_ps.update()
    #     tmp_ps.ps_id -= 1
    #     tmp_ps.insert()
    #     sql = tmp_ps.get_insert_sql()
    #     print('insert sql: %s' % sql)

        # time.sleep(1)
        # with _CursorCtx(sql, ktdb.db_ctx) as curCtx:
        #     sysdate1 = curCtx.select_one(None)
        #     print('date1: %s' % sysdate1)
        #     sysdate2 = curCtx.select_one(None)
        #     print('date2: %s' % sysdate2)
        #
        # time.sleep(2)
        # with ktdb.open_cursor(sql) as curCtx:
        #     sysdate3 = curCtx.select_one(None)
        #     print('date3: %s' % sysdate3)
        #     sysdate4 = curCtx.select_one(None)
        #     print('date4: %s' % sysdate4)
        #
        # time.sleep(1)
        # with ktdb.open_curgrp() as curGrp:
        #     curGrp.get_cur('sysdate', sql)
        #     sysdate5 = curGrp.select_one('sysdate')
        #     print('date5: %s' % sysdate5)
        #     sysdate6 = curGrp.select_one('sysdate')
        #     print('date6: %s' % sysdate6)
