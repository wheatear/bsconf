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

    def execute(self):
        with self.conn.cursor() as cur:
            cur.execute(self.sSql)

#PROMO
dFieldSql = {}
dFieldSql['PROMO_ID'] = ("select max(promo_id) from base.BS_BOOK_SCHEME_PROMO where promo_id like '203%'",
                         "select max(promo_id) from base.BS_BOOK_SCHEME_PROMO@scdb_to_srvzw1 where promo_id like '203%'")
dFieldSql['COND_ID'] = ("select max(COND_ID) from base.BS_BOOK_SCHEME_COND where PROMO_ID = ''",
                         None)
dFieldSql['NEW_SMS_TEMPLET_ID'] = ("select max(NEW_SMS_TEMPLET_ID) from base.BS_BOOK_SCHEME_SMS_FORM",
                                   "select max(NEW_SMS_TEMPLET_ID) from base.BS_BOOK_SCHEME_SMS_FORM@scdb_to_srvzw1")
dFieldSql['NEW_SMS_TEMPLET_ID_SEQ'] = ("select '40' || lpad(4300, 8, '0') || lpad(base.bs_DEF_SMS_TEMPLATE$SEQ.nextval,6, '0') from dual"
                                       , None)

promoSql = "select max(promo_id) from base.BS_BOOK_SCHEME_PROMO where promo_id like '203%'"
promoSqlProd = "select max(promo_id) from base.BS_BOOK_SCHEME_PROMO@scdb_to_srvzw1 where promo_id like '203%'"

condSql = "select max(COND_ID) from base.BS_BOOK_SCHEME_COND where PROMO_ID = ''"

smsSql = "select max(NEW_SMS_TEMPLET_ID) from base.BS_BOOK_SCHEME_SMS_FORM"
smsSqlProd = "select max(NEW_SMS_TEMPLET_ID) from base.BS_BOOK_SCHEME_SMS_FORM@scdb_to_srvzw1"

smsSeqSql = "select '40' || lpad(4300, 8, '0') || lpad(base.bs_DEF_SMS_TEMPLATE$SEQ.nextval,6, '0') from dual"
# smsId = RawSql("select '40' || lpad(4300, 8, '0') || lpad(base.bs_DEF_SMS_TEMPLATE$SEQ.nextval,6, '0') from dual")

#RECEIPT
dFieldSql['RECEIPT_TYPE'] = ("select max(receipt_type) from  base.bs_busi_receipt_type t where t.receipt_type  >1000 AND  t.receipt_type<2000 ",
                             None)
dFieldSql['RECEIPT_ITEM'] = ("select max(receipt_item) from base.bs_busi_receipt_item t where t.receipt_item >1400 AND t.receipt_item<2000",
                             None)
dFieldSql['MIS_GROUP_NO_PAT'] = ("select nvl(max(MIS_GROUP_NO),0) from base.bs_def_bill_item_mis where MIS_GROUP_NO like '%s'",
                                   None)
dFieldSql['MIS_GROUP_NO_PAT02'] = ("select max(MIS_GROUP_NO) from base.bs_def_bill_item_mis where MIS_GROUP_NO like '%s'",
                                   None)
dFieldSql['MIS_GROUP_NO_PAT03'] = ("select max(MIS_GROUP_NO) from base.bs_def_bill_item_mis where MIS_GROUP_NO like '%s'",
                                   None)
dFieldSql['MIS_GROUP_NO_PAT09'] = ("select max(MIS_GROUP_NO) from base.bs_def_bill_item_mis where MIS_GROUP_NO like '%s'",
                                   None)

RECEIPT_TYPE = "select max(receipt_type) from  base.bs_busi_receipt_type t where t.receipt_type  >1000 AND  t.receipt_type<2000 "
RECEIPT_ITEM = "select max(receipt_item) from base.bs_busi_receipt_item t where t.receipt_item >1400 AND t.receipt_item<2000c"
MIS_GROUP_NO = "select max(MIS_GROUP_NO) from base.bs_def_bill_item_mis where MIS_GROUP_NO like '%s'"

dTabCheck = {}
dTabCheck['MIS_BS_DEF_BILL_ITEM_MIS'] = "select MIS_GROUP_NO from base.bs_def_bill_item_mis where MIS_GROUP_NO='^<MIS_GROUP_NO^>'"
dTabCheck['ACC_DEF_BILL_ITEM_AUDIT'] = "select AUDIT_GROUP_NO from inter.acc_def_bill_item_audit where AUDIT_GROUP_NO='^<AUDIT_GROUP_NO^>'"


class SequenceJump(object):
    stepMany = "ALTER SEQUENCE %s INCREMENT BY %d"
    nextVal = "SELECT %s.NEXTVAL FROM DUAL"
    stepOne = "ALTER SEQUENCE %s INCREMENT BY 1"
    def __init__(self, sequence, step):
        self.sequence = sequence
        self.step = step
        self.stepMany = SequenceJump.stepMany % (self.sequence, self.step)
        self.nextVal = SequenceJump.nextVal % self.sequence
        self.stepOne = SequenceJump.stepOne % self.sequence

    def jump(self):
        seq = RawSql(self.stepMany)
        seq.execute()
        seq = RawSql(self.nextVal)
        seq.execute()
        seq = RawSql(self.stepOne)
        seq.execute()


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
    item_name = models.CharField(max_length=126,db_column='item_name')
    item_id = models.BigIntegerField(primary_key=True,db_column='item_id')

    class Meta:
        managed = False
        db_table = 'BSCONF_ITEM_ID'

    @classmethod
    def create(cls, name, id):
        bsItem = cls(item_name=name, item_id=id)
        return bsItem



class IdIncr(models.Model):
    pId = models.BigIntegerField(primary_key=True,db_column='promo_id')
