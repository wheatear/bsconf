-- BOSS-FSC-2019-04-231-zhuyuanzheng-crmϵͳ��Ʊ����������Ʊ��Ŀ-�������ŷ���ѡ���[����ֵ���ŷ���ѡ�
-- RECEIPT 1
insert into base.bs_busi_receipt_type (receipt_type, receipt_type_name, receipt_class, receipt_class_name, receipt_flag, tax_format, sts) values ('1031', 'רƱ����', '5', 'ҵ���վ�', '1', '1', '1');
insert into base.bs_busi_receipt_item (receipt_type, receipt_item, receipt_item_name, unit, item_seq, sts, tax_rate, valid_date, expire_date) values ('1031', '1415', '�������ŷ���', '��', '0', '1', '0', to_date('01-06-2014', 'dd-mm-yyyy'), to_date('01-01-2099', 'dd-mm-yyyy'));
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('03011003', '�������ŷ���', '1');
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('03011003 ', '1415', '1');
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('09011003', '�������ŷ���', '1');
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('09011003 ', '1415', '1');
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('10A268', '�������ŷ���', '1');
insert into base.bs_bill_item_mis_grp (MIS_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE, TAX_RATE1, TAX_RATE1_PERCENT, TAX_RATE2, TAX_RATE2_PERCENT, TAX_RATE3, TAX_RATE3_PERCENT, TAX_RATE) values ('10A268', '1031', '1415', null, null, null, null, null, null, null, null);
insert into inter.acc_def_bill_item_audit (AUDIT_GROUP_NO, AUDIT_GROUP_NAME, STS) values ('A268', '�������ŷ���', '1');
insert into inter.acc_bill_item_audit_grp (AUDIT_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE) values ('A268', '1031', '1415', null);
insert into base.bs_busi_receipt_item (receipt_type, receipt_item, receipt_item_name, unit, item_seq, sts, tax_rate, valid_date, expire_date) values ('1031', '1416', '��ֵ���ŷ���', '��', '0', '1', '0', to_date('01-06-2014', 'dd-mm-yyyy'), to_date('01-01-2099', 'dd-mm-yyyy'));
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('03011004', '��ֵ���ŷ���', '1');
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('03011004 ', '1416', '1');
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('09011004', '��ֵ���ŷ���', '1');
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('09011004 ', '1416', '1');
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('10A268', '��ֵ���ŷ���', '1');
insert into base.bs_bill_item_mis_grp (MIS_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE, TAX_RATE1, TAX_RATE1_PERCENT, TAX_RATE2, TAX_RATE2_PERCENT, TAX_RATE3, TAX_RATE3_PERCENT, TAX_RATE) values ('10A268', '1031', '1416', null, null, null, null, null, null, null, null);
insert into inter.acc_def_bill_item_audit (AUDIT_GROUP_NO, AUDIT_GROUP_NAME, STS) values ('A268', '��ֵ���ŷ���', '1');
insert into inter.acc_bill_item_audit_grp (AUDIT_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE) values ('A268', '1031', '1416', null);

commit;
