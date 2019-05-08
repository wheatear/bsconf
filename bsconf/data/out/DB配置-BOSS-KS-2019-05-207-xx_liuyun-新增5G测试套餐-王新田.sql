-- DB配置-BOSS-KS-2019-05-207-xx_liuyun-新增5G测试套餐-王新田
-- ALARM_PROD 1
-- 新增余量提醒  ALARM_TYPE 1-全球通  4-动感  5-神州行  15-其它
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G测试套餐', '1', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- 新增余量提醒  ALARM_TYPE 1-全球通  4-动感  5-神州行  15-其它
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G测试套餐', '4', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- 新增余量提醒  ALARM_TYPE 1-全球通  4-动感  5-神州行  15-其它
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G测试套餐', '5', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- 新增余量提醒  ALARM_TYPE 1-全球通  4-动感  5-神州行  15-其它
INSERT INTO ZG.PACKAGE_ALARM_PROD (PROD_ID, PROD_NAME, ALARM_TYPE, VALID_DATE, EXPIRE_DATE, REMARK) VALUES ('54001738', '5G测试套餐', '15', to_date('01-01-2001', 'dd-mm-yyyy'), to_date('01-01-2030', 'dd-mm-yyyy'), null);
-- RECEIPT 1
-- 新增发票配置 receipt_type, receipt_type_name, receipt_class(5-预存（收据）；8－发票（通票，业务发票), receipt_class_name
insert into base.bs_busi_receipt_type (receipt_type, receipt_type_name, receipt_class, receipt_class_name, receipt_flag, tax_format, sts) values ('1040', '5G测试卡', '8', '业务发票', '1', '1', '1');
-- 配置税率  receipt_type, receipt_item, receipt_item_name,tax_rate,valid_date, expire_date
insert into base.bs_busi_receipt_item (receipt_type, receipt_item, receipt_item_name, unit, item_seq, sts, tax_rate, valid_date, expire_date) values ('1040', '1423', '5G测试卡SIM卡费', '张', '0', '1', '1300', to_date('01-06-2014', 'dd-mm-yyyy'), to_date('31-12-2015', 'dd-mm-yyyy'));
-- 配置CRM费用项编码映射 busi_item_code,fee_item_id,fee_item_name, receipt_type, receipt_item
insert into base.bs_busi_item_map (busi_item_code, busi_item_type, fee_item_id, fee_item_name, sts, receipt_type, receipt_item) values ('69804', '3', '69804', '5G测试卡SIM卡费', '1', '1040', '1423');
-- 厅台统计，财务统计定义，只要有mis码如A226，配置成10A226  厅台码（01 卡类收入 02 话费收入 09 其它收入  03  调整类MIS  ） 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('03011005', '5G测试卡SIM卡费', '1');
-- 厅台码和发票科目的映射 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('03011005', '1423', '1');
-- 厅台统计，财务统计定义，只要有mis码如A226，配置成10A226  厅台码（01 卡类收入 02 话费收入 09 其它收入  03  调整类MIS  ） 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('01011002', '5G测试卡SIM卡费', '1');
-- 厅台码和发票科目的映射 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('01011002', '1423', '1');
-- 配置统计和发票科目的映射关系,税率拆分
insert into base.bs_bill_item_mis_grp (MIS_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE, TAX_RATE1, TAX_RATE1_PERCENT, TAX_RATE2, TAX_RATE2_PERCENT, TAX_RATE3, TAX_RATE3_PERCENT, TAX_RATE) values ('10A01', '1040', '1423', null, null, null, null, null, null, null, null);
-- 财务mis码和发票类型发票科目映射表
insert into inter.acc_bill_item_audit_grp (AUDIT_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE) values ('A01', '1040', '1423', null);
-- 配置税率  receipt_type, receipt_item, receipt_item_name,tax_rate,valid_date, expire_date
insert into base.bs_busi_receipt_item (receipt_type, receipt_item, receipt_item_name, unit, item_seq, sts, tax_rate, valid_date, expire_date) values ('1040', '1424', '5G测试卡SIM卡费折扣', '张', '0', '1', '1300', to_date('01-06-2014', 'dd-mm-yyyy'), to_date('31-12-2015', 'dd-mm-yyyy'));
-- 配置CRM费用项编码映射 busi_item_code,fee_item_id,fee_item_name, receipt_type, receipt_item
insert into base.bs_busi_item_map (busi_item_code, busi_item_type, fee_item_id, fee_item_name, sts, receipt_type, receipt_item) values ('69805', '3', '69805', '5G测试卡SIM卡费折扣', '1', '1040', '1424');
-- 厅台统计，财务统计定义，只要有mis码如A226，配置成10A226  厅台码（01 卡类收入 02 话费收入 09 其它收入  03  调整类MIS  ） 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('03011006', '5G测试卡SIM卡费折扣', '1');
-- 厅台码和发票科目的映射 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('03011006', '1424', '1');
-- 厅台统计，财务统计定义，只要有mis码如A226，配置成10A226  厅台码（01 卡类收入 02 话费收入 09 其它收入  03  调整类MIS  ） 
insert into base.bs_def_bill_item_mis (MIS_GROUP_NO, MIS_GROUP_NAME, STS) values ('01011003', '5G测试卡SIM卡费折扣', '1');
-- 厅台码和发票科目的映射 
insert into base.bs_bill_item_grp (MIS_GROUP_NO, BILL_ITEM_ID, STS) values ('01011003', '1424', '1');
-- 配置统计和发票科目的映射关系,税率拆分
insert into base.bs_bill_item_mis_grp (MIS_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE, TAX_RATE1, TAX_RATE1_PERCENT, TAX_RATE2, TAX_RATE2_PERCENT, TAX_RATE3, TAX_RATE3_PERCENT, TAX_RATE) values ('10A54', '1040', '1424', null, null, null, null, null, null, null, null);
-- 财务mis码和发票类型发票科目映射表
insert into inter.acc_bill_item_audit_grp (AUDIT_GROUP_NO, BUSI_TYPE, BILL_ITEM_ID, STA_TYPE) values ('A54', '1040', '1424', null);

commit;
