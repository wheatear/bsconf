-- DB����-BOSS-KS-2019-05-207-xx_liuyun-����5G�����ײ�-������
-- ALARM_PROD 1
-- ������������  ALARM_TYPE 1-ȫ��ͨ  4-����  5-������  15-����
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G�����ײ�', '1', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- ������������  ALARM_TYPE 1-ȫ��ͨ  4-����  5-������  15-����
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G�����ײ�', '4', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- ������������  ALARM_TYPE 1-ȫ��ͨ  4-����  5-������  15-����
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G�����ײ�', '5', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- ������������  ALARM_TYPE 1-ȫ��ͨ  4-����  5-������  15-����
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G�����ײ�', '15', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- RECEIPT 1
-- ������Ʊ���� receipt_type, receipt_type_name, receipt_class(5-Ԥ�棨�վݣ���8����Ʊ��ͨƱ��ҵ��Ʊ), receipt_class_name
insert into base.bs_busi_receipt_type (receipt_type, receipt_type_name, receipt_class, receipt_class_name, receipt_flag, tax_format, sts) values ('1040', '5G���Կ�', '8', 'ҵ��Ʊ', '1', '1', '1');
-- ����˰��  receipt_type, receipt_item, receipt_item_name,tax_rate,valid_date, expire_date
insert into base.bs_busi_receipt_item (receipt_type, receipt_item, receipt_item_name, unit, item_seq, sts, tax_rate, valid_date, expire_date) values ('1040', '1423', '5G���Կ�SIM����', '��', '0', '1', '1300', to_date('01-06-2014', 'dd-mm-yyyy'), to_date('31-12-2015', 'dd-mm-yyyy'));
-- ����CRM���������ӳ�� busi_item_code,fee_item_id,fee_item_name, receipt_type, receipt_item
insert into base.bs_busi_item_map (busi_item_code, busi_item_type, fee_item_id, fee_item_name, sts, receipt_type, receipt_item) values ('69804', '3', '69804', '5G���Կ�SIM����', '1', '1040', '1423');
-- ��̨ͳ�ƣ�����ͳ�ƶ��壬ֻҪ��mis����A226�����ó�10A226  ��̨�루01 �������� 02 �������� 09 ��������  03  ������MIS  �� 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('03011005', '5G���Կ�SIM����', '1');
-- ��̨��ͷ�Ʊ��Ŀ��ӳ�� 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('03011005', '1423', '1');
-- ��̨ͳ�ƣ�����ͳ�ƶ��壬ֻҪ��mis����A226�����ó�10A226  ��̨�루01 �������� 02 �������� 09 ��������  03  ������MIS  �� 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('01011002', '5G���Կ�SIM����', '1');
-- ��̨��ͷ�Ʊ��Ŀ��ӳ�� 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('01011002', '1423', '1');
-- ����ͳ�ƺͷ�Ʊ��Ŀ��ӳ���ϵ,˰�ʲ��
insert into base.bs_bill_item_mis_grp (MIS_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE, TAX_RATE1, TAX_RATE1_PERCENT, TAX_RATE2, TAX_RATE2_PERCENT, TAX_RATE3, TAX_RATE3_PERCENT, TAX_RATE) values ('10A01', '1040', '1423', null, null, null, null, null, null, null, null);
-- ����mis��ͷ�Ʊ���ͷ�Ʊ��Ŀӳ���
insert into inter.acc_bill_item_audit_grp (AUDIT_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE) values ('A01', '1040', '1423', null);
-- ����˰��  receipt_type, receipt_item, receipt_item_name,tax_rate,valid_date, expire_date
insert into base.bs_busi_receipt_item (receipt_type, receipt_item, receipt_item_name, unit, item_seq, sts, tax_rate, valid_date, expire_date) values ('1040', '1424', '5G���Կ�SIM�����ۿ�', '��', '0', '1', '1300', to_date('01-06-2014', 'dd-mm-yyyy'), to_date('31-12-2015', 'dd-mm-yyyy'));
-- ����CRM���������ӳ�� busi_item_code,fee_item_id,fee_item_name, receipt_type, receipt_item
insert into base.bs_busi_item_map (busi_item_code, busi_item_type, fee_item_id, fee_item_name, sts, receipt_type, receipt_item) values ('69805', '3', '69805', '5G���Կ�SIM�����ۿ�', '1', '1040', '1424');
-- ��̨ͳ�ƣ�����ͳ�ƶ��壬ֻҪ��mis����A226�����ó�10A226  ��̨�루01 �������� 02 �������� 09 ��������  03  ������MIS  �� 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('03011006', '5G���Կ�SIM�����ۿ�', '1');
-- ��̨��ͷ�Ʊ��Ŀ��ӳ�� 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('03011006', '1424', '1');
-- ��̨ͳ�ƣ�����ͳ�ƶ��壬ֻҪ��mis����A226�����ó�10A226  ��̨�루01 �������� 02 �������� 09 ��������  03  ������MIS  �� 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('01011003', '5G���Կ�SIM�����ۿ�', '1');
-- ��̨��ͷ�Ʊ��Ŀ��ӳ�� 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('01011003', '1424', '1');
-- ����ͳ�ƺͷ�Ʊ��Ŀ��ӳ���ϵ,˰�ʲ��
insert into base.bs_bill_item_mis_grp (MIS_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE, TAX_RATE1, TAX_RATE1_PERCENT, TAX_RATE2, TAX_RATE2_PERCENT, TAX_RATE3, TAX_RATE3_PERCENT, TAX_RATE) values ('10A54', '1040', '1424', null, null, null, null, null, null, null, null);
-- ����mis��ͷ�Ʊ���ͷ�Ʊ��Ŀӳ���
insert into inter.acc_bill_item_audit_grp (AUDIT_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE) values ('A54', '1040', '1424', null);

commit;
