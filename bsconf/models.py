from django.db import models,connection,connections

# Create your models here.
class RawSql(object):
    def __init__(self, sSql, db=None):
        self.sSql = sSql
        if db:
            self.conn = connections[db]
        else:
            self.conn = connection

    def fetchVal(self):
        with self.conn.cursor() as cur:
            cur.execute(self.sSql)
            raw = cur.fetchone()
        if raw:
            return raw[0]
        else:
            return None

promoSql = "select max(promo_id) from base.BS_BOOK_SCHEME_PROMO where promo_id like '203%'"
promoSqlProd = "select max(promo_id) from base.BS_BOOK_SCHEME_PROMO@scdb_to_srvzw1 where promo_id like '203%'"

condSql = "select max(COND_ID) from base.BS_BOOK_SCHEME_COND where PROMO_ID = ''"

smsSql = "select max(NEW_SMS_TEMPLET_ID) from base.BS_BOOK_SCHEME_SMS_FORM"
smsSqlProd = "select max(NEW_SMS_TEMPLET_ID) from base.BS_BOOK_SCHEME_SMS_FORM@scdb_to_srvzw1"

smsId = RawSql("select '40' || lpad(4300, 8, '0') || lpad(base.bs_DEF_SMS_TEMPLATE$SEQ.nextval,6, '0') from dual")

class PromoIdExist(models.Model):
    id = models.BigIntegerField(primary_key=True,db_column='promo_id')

    class Meta:
        managed = False
        app_label = 'base'
        db_table = 'BS_BOOK_SCHEME_PROMO'
        ordering = ['-id']


class PromoNextId(object):
    def __init__(self):
        self.lastId = PromoIdExist.objects.filter(id__startswith='203').first().id
        self.NextId = self.lastId + 1


class BsItemId(models.Model):
    item_name = models.CharField(max_length=126)
    item_id = models.BigIntegerField

    class Meta:
        managed = False
        db_table = 'BSCONF_ITEM_ID'

    @classmethod
    def create(cls, name, id):
        bsItem = cls(item_name=name, item_id=id)
        return bsItem



class IdIncr(models.Model):
    pId = models.BigIntegerField(primary_key=True,db_column='promo_id')
