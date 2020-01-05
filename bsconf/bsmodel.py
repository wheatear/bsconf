from django.db import models,connection,connections
import time
import bsconf.oraorm as orm


class BS_PROD_INFO(orm.Model):
    __table__ = 'BASE.BS_PROD_INFO'
    PROD_ID = orm.IntegerField(ddl='NUMBER(15)', primary_key=True)
    PROD_NAME = orm.StringField(ddl='VARCHAR2(64)')
    BASE_VALUE = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_TYPE = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_ID = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_COUNT = orm.StringField(ddl='VARCHAR2(4000)')
    FREEBIE_UNIT = orm.StringField(ddl='VARCHAR2(4000)')

