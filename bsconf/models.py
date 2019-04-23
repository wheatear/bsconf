from django.db import models,connection

# Create your models here.
class RawSql(object):
    def __init__(self, sSql):
        self.sSql = sSql

    def nextVal(self):
        with connection.cursor() as cur:
            cur.execute(self.sSql)
            raw = cur.fetchone()
        if raw:
            return raw[0]

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




class IdIncr(models.Model):
    pId = models.BigIntegerField(primary_key=True,db_column='promo_id')
