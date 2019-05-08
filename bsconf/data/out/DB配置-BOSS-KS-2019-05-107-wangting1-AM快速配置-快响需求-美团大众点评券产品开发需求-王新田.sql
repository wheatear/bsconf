-- DB����-BOSS-KS-2019-05-107-wangting1-AM��������-��������-���Ŵ��ڵ���ȯ��Ʒ��������-������
-- FEE_ITEM 1
-- �������ÿ�Ŀ˰������ ITEM_CODE,TAX_RATE
INSERT INTO BASE.ACCP_ITEM_TAX_RATE (ITEM_CODE, TAX_RATE, VALID_DATE, EXPIRE_DATE) VALUES ('88002507', '600', TO_DATE('01-11-2017', 'dd-mm-yyyy'), TO_DATE('31-12-2030', 'dd-mm-yyyy'));
-- �������Ŀ�г����ͱ� ��FEE_ITEM_ID,ITEM_NAME,MARKET_TYPE_ID,MARKET_TYPE_NAME ����010����ͥ��020�����ͣ�030��ȱʡ��000
INSERT INTO ZG.ACC_DEF_FEE_ITEM_EX (FEE_ITEM_ID, ITEM_NAME, MARKET_TYPE_ID, MARKET_TYPE_NAME, BUSINESS_MANAGER, DEVELOPMENT_MANAGER) VALUES ('88002507', 'AM����10Ԫ����ȯ', '010', '����', NULL, NULL);
-- ������Ŀ�������ȼ� acct_item_type_id,acct_item_type_name,bill_priority
INSERT INTO BASE.BS_ACCT_ITEM_TYPE (ACCT_ITEM_TYPE_ID, ACCT_ITEM_TYPE_NAME, ACCT_ITEM_TYPE_KIND, BILL_PRIORITY, STATE, STATE_DATE) VALUES ('88002507', 'AM����10Ԫ����ȯ', '0', '143', '1',SYSDATE);
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('1', '238', '88002507', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('999', '238', '88002507', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id  ����ת��998��
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('998', '319', '88002507', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ת����Ʊ���ĸ���ʽ�飺66666666������6%��11111111������10%��88888888������16%   
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('888', '66666666', '88002507', '1',TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('21', '239', '88002507', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('997', '196', '88002507', '1',TRUNC(SYSDATE,'MM'));
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82950', '88002507', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82951', '88002507', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('98006', '88002507', '5000000000', '1', '0', '2');
-- FEE_ITEM 2
-- �������ÿ�Ŀ˰������ ITEM_CODE,TAX_RATE
INSERT INTO BASE.ACCP_ITEM_TAX_RATE (ITEM_CODE, TAX_RATE, VALID_DATE, EXPIRE_DATE) VALUES ('88002508', '600', TO_DATE('01-11-2017', 'dd-mm-yyyy'), TO_DATE('31-12-2030', 'dd-mm-yyyy'));
-- �������Ŀ�г����ͱ� ��FEE_ITEM_ID,ITEM_NAME,MARKET_TYPE_ID,MARKET_TYPE_NAME ����010����ͥ��020�����ͣ�030��ȱʡ��000
INSERT INTO ZG.ACC_DEF_FEE_ITEM_EX (FEE_ITEM_ID, ITEM_NAME, MARKET_TYPE_ID, MARKET_TYPE_NAME, BUSINESS_MANAGER, DEVELOPMENT_MANAGER) VALUES ('88002508', 'AM����20Ԫ����ȯ', '010', '����', NULL, NULL);
-- ������Ŀ�������ȼ� acct_item_type_id,acct_item_type_name,bill_priority
INSERT INTO BASE.BS_ACCT_ITEM_TYPE (ACCT_ITEM_TYPE_ID, ACCT_ITEM_TYPE_NAME, ACCT_ITEM_TYPE_KIND, BILL_PRIORITY, STATE, STATE_DATE) VALUES ('88002508', 'AM����20Ԫ����ȯ', '0', '143', '1',SYSDATE);
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('1', '238', '88002508', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('999', '238', '88002508', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id  ����ת��998��
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('998', '319', '88002508', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ת����Ʊ���ĸ���ʽ�飺66666666������6%��11111111������10%��88888888������16%   
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('888', '66666666', '88002508', '1',TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('21', '239', '88002508', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('997', '196', '88002508', '1',TRUNC(SYSDATE,'MM'));
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82950', '88002508', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82951', '88002508', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('98006', '88002508', '5000000000', '1', '0', '2');
-- FEE_ITEM 3
-- �������ÿ�Ŀ˰������ ITEM_CODE,TAX_RATE
INSERT INTO BASE.ACCP_ITEM_TAX_RATE (ITEM_CODE, TAX_RATE, VALID_DATE, EXPIRE_DATE) VALUES ('88002509', '600', TO_DATE('01-11-2017', 'dd-mm-yyyy'), TO_DATE('31-12-2030', 'dd-mm-yyyy'));
-- �������Ŀ�г����ͱ� ��FEE_ITEM_ID,ITEM_NAME,MARKET_TYPE_ID,MARKET_TYPE_NAME ����010����ͥ��020�����ͣ�030��ȱʡ��000
INSERT INTO ZG.ACC_DEF_FEE_ITEM_EX (FEE_ITEM_ID, ITEM_NAME, MARKET_TYPE_ID, MARKET_TYPE_NAME, BUSINESS_MANAGER, DEVELOPMENT_MANAGER) VALUES ('88002509', 'AM���ڵ���10Ԫ����ȯ', '010', '����', NULL, NULL);
-- ������Ŀ�������ȼ� acct_item_type_id,acct_item_type_name,bill_priority
INSERT INTO BASE.BS_ACCT_ITEM_TYPE (ACCT_ITEM_TYPE_ID, ACCT_ITEM_TYPE_NAME, ACCT_ITEM_TYPE_KIND, BILL_PRIORITY, STATE, STATE_DATE) VALUES ('88002509', 'AM���ڵ���10Ԫ����ȯ', '0', '143', '1',SYSDATE);
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('1', '238', '88002509', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('999', '238', '88002509', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id  ����ת��998��
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('998', '319', '88002509', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ת����Ʊ���ĸ���ʽ�飺66666666������6%��11111111������10%��88888888������16%   
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('888', '66666666', '88002509', '1',TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('21', '239', '88002509', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('997', '196', '88002509', '1',TRUNC(SYSDATE,'MM'));
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82950', '88002509', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82951', '88002509', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('98006', '88002509', '5000000000', '1', '0', '2');
-- FEE_ITEM 4
-- �������ÿ�Ŀ˰������ ITEM_CODE,TAX_RATE
INSERT INTO BASE.ACCP_ITEM_TAX_RATE (ITEM_CODE, TAX_RATE, VALID_DATE, EXPIRE_DATE) VALUES ('88002510', '600', TO_DATE('01-11-2017', 'dd-mm-yyyy'), TO_DATE('31-12-2030', 'dd-mm-yyyy'));
-- �������Ŀ�г����ͱ� ��FEE_ITEM_ID,ITEM_NAME,MARKET_TYPE_ID,MARKET_TYPE_NAME ����010����ͥ��020�����ͣ�030��ȱʡ��000
INSERT INTO ZG.ACC_DEF_FEE_ITEM_EX (FEE_ITEM_ID, ITEM_NAME, MARKET_TYPE_ID, MARKET_TYPE_NAME, BUSINESS_MANAGER, DEVELOPMENT_MANAGER) VALUES ('88002510', 'AM���ڵ���20Ԫ����ȯ', '010', '����', NULL, NULL);
-- ������Ŀ�������ȼ� acct_item_type_id,acct_item_type_name,bill_priority
INSERT INTO BASE.BS_ACCT_ITEM_TYPE (ACCT_ITEM_TYPE_ID, ACCT_ITEM_TYPE_NAME, ACCT_ITEM_TYPE_KIND, BILL_PRIORITY, STATE, STATE_DATE) VALUES ('88002510', 'AM���ڵ���20Ԫ����ȯ', '0', '143', '1',SYSDATE);
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('1', '238', '88002510', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ����/ת����Ʊ 1��999�� 
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('999', '238', '88002510', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id  ����ת��998��
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('998', '319', '88002510', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id ת����Ʊ���ĸ���ʽ�飺66666666������6%��11111111������10%��88888888������16%   
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('888', '66666666', '88002510', '1',TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('21', '239', '88002510', '1', TRUNC(SYSDATE,'MM'));
-- ������Ʊ���� bill_format_id, bill_item_id, fee_item_id   ����21��997���̶����239��196
INSERT INTO BASE.BS_FEE_ITEM_BILL_ITEM (BILL_FORMAT_ID, BILL_ITEM_ID, FEE_ITEM_ID, STS, STS_TIME) VALUES ('997', '196', '88002510', '1',TRUNC(SYSDATE,'MM'));
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82950', '88002510', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('82951', '88002510', '5000000000', '1', '0', '2');
-- �������ã�����82950������82951�˻������Գ�������������  sts:1(Ĭ�Ͽɳ���) 2�������⼸����Ŀ���ɳ����������Ķ��ɳ���
INSERT INTO BASE.BS_ACCT_ITEM_TYPE_BALANCE_TYPE (BALANCE_TYPE_ID, ACCT_ITEM_TYPE_ID, BALANCE_MAX_VALUE, RELA_PRIORITY, OVERFLOW_RULE, STS) VALUES ('98006', '88002510', '5000000000', '1', '0', '2');

commit;
