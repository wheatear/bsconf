-- DB配置-BOSS-KS-2019-05-181-wangting1-AM快速配置-快响需求-每日优鲜月会员开发需求-王新田
-- FEE_ITEM 1
-- 新增费用科目税率配置 ITEM_CODE,TAX_RATE
INSERT INTO BASE.ACCP_ITEM_TAX_RATE (ITEM_CODE, TAX_RATE, VALID_DATE, EXPIRE_DATE) VALUES ('88002511', '600', TO_DATE('01-11-2017', 'dd-mm-yyyy'), TO_DATE('31-12-2030', 'dd-mm-yyyy'));
-- 费用项科目市场类型表 ：FEE_ITEM_ID,ITEM_NAME,MARKET_TYPE_ID,MARKET_TYPE_NAME 个人010，家庭：020，集客：030，缺省：000
INSERT INTO ZG.ACC_DEF_FEE_ITEM_EX (FEE_ITEM_ID, ITEM_NAME, MARKET_TYPE_ID, MARKET_TYPE_NAME, BUSINESS_MANAGER, DEVELOPMENT_MANAGER) VALUES ('88002511', 'AM每日优鲜月会员', '010', '个人', NULL, NULL);
-- 新增科目销账优先级 acct_item_type_id,acct_item_type_name,bill_priority
INSERT INTO BASE.BS_ACCT_ITEM_TYPE (ACCT_ITEM_TYPE_ID, ACCT_ITEM_TYPE_NAME, ACCT_ITEM_TYPE_KIND, BILL_PRIORITY, STATE, STATE_DATE) VALUES ('88002511', 'AM每日优鲜月会员', '0', '143', '1',SYSDATE);
-- 新增发票配置 bill_format_id, bill_item_id, fee_item_id 话费/转讫发票 1和999， 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('1', '238', '88002511', '1', TRUNC(SYSDATE,'MM'));
-- 新增发票配置 bill_format_id, bill_item_id, fee_item_id 话费/转讫发票 1和999， 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('999', '238', '88002511', '1', TRUNC(SYSDATE,'MM'));
-- 新增发票配置 bill_format_id, bill_item_id, fee_item_id  托收转讫998，
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('998', '319', '88002511', '1', TRUNC(SYSDATE,'MM'));
-- 新增发票配置 bill_format_id, bill_item_id, fee_item_id 转讫发票走哪个格式组：66666666：代表6%，11111111：代表10%，88888888：代表16%   
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('888', '66666666', '88002511', '1',TRUNC(SYSDATE,'MM'));
-- 新增发票配置 bill_format_id, bill_item_id, fee_item_id   配置21和997，固定配成239和196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('21', '239', '88002511', '1', TRUNC(SYSDATE,'MM'));
-- 新增发票配置 bill_format_id, bill_item_id, fee_item_id   配置21和997，固定配成239和196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('997', '196', '88002511', '1',TRUNC(SYSDATE,'MM'));
-- 增加配置：副二82950、副三82951账户不可以冲销上述费用项  sts:1(默认可冲销) 2代表这这几个科目不可冲销，其他的都可冲销
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82950', '88002511', '5000000000', '1', '0', '2');
-- 增加配置：副二82950、副三82951账户不可以冲销上述费用项  sts:1(默认可冲销) 2代表这这几个科目不可冲销，其他的都可冲销
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82951', '88002511', '5000000000', '1', '0', '2');
-- 增加配置：副二82950、副三82951账户不可以冲销上述费用项  sts:1(默认可冲销) 2代表这这几个科目不可冲销，其他的都可冲销
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('98006', '88002511', '5000000000', '1', '0', '2');

commit;
