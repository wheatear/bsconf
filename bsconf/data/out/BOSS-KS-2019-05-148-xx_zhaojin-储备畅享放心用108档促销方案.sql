-- BOSS-KS-2019-05-148-xx_zhaojin-储备畅享放心用108档促销方案
-- PROMO_UNIFIED 1
insert into base.BS_BOOK_SCHEME_PROMO (PROMO_ID, PROMO_NAME, BUSI_TYPE_CODE, REGION_CODE, PROMO_TYPE, COUNTY_CODE, ORG_ID, PROMO_GROUP) values ('203025', '88元畅享放心用套餐首充优惠首月-赠送', '4300', '0', '1', '0', '0', '0');
insert into base.BS_BOOK_SCHEME_COND (PROMO_ID, COND_ID, COND_NAME, COND_TYPE, RES_HOLD_MONTH, RELATE_CODE,RELATE_NAME, PRE_TYPE, ALLOW_PRE_MORE, PRE_FEE, HIGH_PRE_FEE, SCHEME_TYPE, SCHEME_FEE, LOW_COST, VALID_DATE, EXPIRE_DATE, PRIV_ENTITY, RENT_PACK_ID, RES_PACK_ID, COND_ACCEPT_DESC, REMARK, COIN_RET_TYPE, COND_BONUS_ID, COND_HOLD_MONTH, COND_ENGAGE_TYPE, COND_CREDIT, COND_COST_STAT, COND_GROUP, ALLOW_BIND_IMEI, RES_VICE_MONTH, COND_UPLOAD_MODE, RELATE_HOLD_MONTH, ALLOW_CEASE_COND, CALL_CNT, SP_PACK_ID, COND_ATTR, RELATE_PROD_ID, SLOGAN, UNBIND_IMEI_MONTH, RELATE_PROMO_INFO, GIFT_INFO, RET_DAY) values ('203025', '20302501', '88元畅享放心用套餐首充优惠首月-赠送', '11', '0', '0', null, '0', '0', '-1', '-1', '1', '0', '0', to_date('01-04-2010', 'dd-mm-yyyy'), to_date('30-11-2030', 'dd-mm-yyyy'), '0', '0', '0', '88元畅享放心用套餐首充优惠首月-赠送', '88元畅享放心用套餐首充优惠首月-赠送', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, '-1', null, null,  '0');
insert into base.BS_BOOK_SCHEME_ALLOT (PROMO_ID, COND_ID, BOOK_ITEM_ID, BOOK_TYPE, ALLOT_AMOUNT, ALLOT_MONTH, ALLOT_TYPE, ALLOT_SCALE, EXPLICIT_MONTH, ALLOT_BEGIN_MONTH, ALLOT_BOOK_LIMIT, ALLOT_BOOK_BEGIN, ALLOT_BONUS_ID, ALLOT_BOOK_END, ALLOT_BOOK_LIMIT_TYPE, ALLOT_ATTR, EXTEND_MONTH, CANCEL_BOOK_ITEM_ID) values ('203025', '20302501', '82951', '1', '-1', '-1', '1', '-1', '0', '0', '0', '-24', '0', '0', '0', '00000000000000000010', '0', '0');
insert into base.BS_BOOK_SCHEME_SAP_MAP (SAP_ID, SAP_FEE_TYPE, SAP_FEE_VALUE, SAP_OTHER_VALUE, PROMO_ID, COND_ID, STS, SAP_FEE_MONTH, SAP_NAME) values ('SAP1167', '1', '-1', '-1', '203025', '20302501', '1', '-1', '88元畅享放心用套餐首充优惠首月-赠送');
insert into base.BS_BOOK_SCHEME_SMS_FORM (PROMO_ID, COND_ID, APPLY_TYPE, SMS_TEMPLET_ID, NEW_SMS_TEMPLET_ID) values ('203025', '20302501', '1', '20302501', '4000004300117001');
insert into base.bs_sms_rule (RULE_ID, RULE_CODE, RULE_EXP, RULE_ORDER, BUSINESS_ID, AC_SMS_TEMPLATE_ID, SMS_TEMPLATE_ID, STATE, CREATE_DATE) values (base.bs_sms_rule$seq.nextval, '4000004300117001', '', '1', '4300', '4000004300117001', '4000004300103372', 'U', sysdate);
insert into base.bs_book_scheme_SAP_type (SAP_ID, SAP_TYPE, SAP_TYPE_NAME, REMARK1, REMARK2, REMARK3, REMARK4) values ('SAP1167', 1, '88元畅享放心用套餐首充优惠首月-赠送', 'BOSS-KS-2019-05-148-xx_zhaojin', '申小帆', null, null);
-- PROMO_UNIFIED 2
insert into base.BS_BOOK_SCHEME_PROMO (PROMO_ID, PROMO_NAME, BUSI_TYPE_CODE, REGION_CODE, PROMO_TYPE, COUNTY_CODE, ORG_ID, PROMO_GROUP) values ('203026', '88元畅享放心用套餐首充优惠非首月-赠送', '4300', '0', '1', '0', '0', '0');
insert into base.BS_BOOK_SCHEME_COND (PROMO_ID, COND_ID, COND_NAME, COND_TYPE, RES_HOLD_MONTH, RELATE_CODE,RELATE_NAME, PRE_TYPE, ALLOW_PRE_MORE, PRE_FEE, HIGH_PRE_FEE, SCHEME_TYPE, SCHEME_FEE, LOW_COST, VALID_DATE, EXPIRE_DATE, PRIV_ENTITY, RENT_PACK_ID, RES_PACK_ID, COND_ACCEPT_DESC, REMARK, COIN_RET_TYPE, COND_BONUS_ID, COND_HOLD_MONTH, COND_ENGAGE_TYPE, COND_CREDIT, COND_COST_STAT, COND_GROUP, ALLOW_BIND_IMEI, RES_VICE_MONTH, COND_UPLOAD_MODE, RELATE_HOLD_MONTH, ALLOW_CEASE_COND, CALL_CNT, SP_PACK_ID, COND_ATTR, RELATE_PROD_ID, SLOGAN, UNBIND_IMEI_MONTH, RELATE_PROMO_INFO, GIFT_INFO, RET_DAY) values ('203026', '20302601', '88元畅享放心用套餐首充优惠非首月-赠送', '11', '0', '0', null, '0', '0', '-1', '-1', '1', '0', '0', to_date('01-04-2010', 'dd-mm-yyyy'), to_date('30-11-2030', 'dd-mm-yyyy'), '0', '0', '0', '88元畅享放心用套餐首充优惠非首月-赠送', '88元畅享放心用套餐首充优惠非首月-赠送', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', null, '-1', null, null,  '0');
insert into base.BS_BOOK_SCHEME_ALLOT (PROMO_ID, COND_ID, BOOK_ITEM_ID, BOOK_TYPE, ALLOT_AMOUNT, ALLOT_MONTH, ALLOT_TYPE, ALLOT_SCALE, EXPLICIT_MONTH, ALLOT_BEGIN_MONTH, ALLOT_BOOK_LIMIT, ALLOT_BOOK_BEGIN, ALLOT_BONUS_ID, ALLOT_BOOK_END, ALLOT_BOOK_LIMIT_TYPE, ALLOT_ATTR, EXTEND_MONTH, CANCEL_BOOK_ITEM_ID) values ('203026', '20302601', '82951', '1', '-1', '-1', '1', '-1', '0', '0', '0', '-24', '0', '0', '0', '00000000020000000010', '0', '0');
insert into base.BS_BOOK_SCHEME_SAP_MAP (SAP_ID, SAP_FEE_TYPE, SAP_FEE_VALUE, SAP_OTHER_VALUE, PROMO_ID, COND_ID, STS, SAP_FEE_MONTH, SAP_NAME) values ('SAP1168', '1', '-1', '-1', '203026', '20302601', '1', '-1', '88元畅享放心用套餐首充优惠非首月-赠送');
insert into base.BS_BOOK_SCHEME_SMS_FORM (PROMO_ID, COND_ID, APPLY_TYPE, SMS_TEMPLET_ID, NEW_SMS_TEMPLET_ID) values ('203026', '20302601', '1', '20302601', '4000004300117002');
insert into base.bs_sms_rule (RULE_ID, RULE_CODE, RULE_EXP, RULE_ORDER, BUSINESS_ID, AC_SMS_TEMPLATE_ID, SMS_TEMPLATE_ID, STATE, CREATE_DATE) values (base.bs_sms_rule$seq.nextval, '4000004300117002', '', '1', '4300', '4000004300117002', '4000004300103373', 'U', sysdate);
insert into base.bs_book_scheme_SAP_type (SAP_ID, SAP_TYPE, SAP_TYPE_NAME, REMARK1, REMARK2, REMARK3, REMARK4) values ('SAP1168', 1, '88元畅享放心用套餐首充优惠非首月-赠送', 'BOSS-KS-2019-05-148-xx_zhaojin', '申小帆', null, null);

commit;
