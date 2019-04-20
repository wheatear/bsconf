from django.db import models,connection

# Create your models here.
class Sequence(object):
    def __init__(self, sSql):
        self.sSql = sSql

    def nextVal(self):
        with connection.cursor() as cur:
            cur.execute(self.sSql)
            raw = cur.fetchone()
        if raw:
            return raw[0]

smsId = Sequence("select '40' || lpad(4300, 8, '0') || lpad(base.bs_DEF_SMS_TEMPLATE$SEQ.nextval,6, '0') from dual")

class PromoId(models.Model):
    id = models.BigIntegerField(primary_key=True,db_column='promo_id')

    class Meta:
        managed = False
        app_label = 'base'
        db_table = 'BS_BOOK_SCHEME_PROMO'
        ordering = ['-id']
