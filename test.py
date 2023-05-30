import json
A='{"sign_text_1":"<xml><service><![CDATA[vmj]]></service><version><![CDATA[2.0]]></version><charset><![CDATA[UTF-8]]></charset><sign_type><![CDATA[SHA-256]]></sign_type><merchant_no><![CDATA[100000001000008]]></merchant_no><out_trade_no><![CDATA[CJKrk111BA]]></out_trade_no><body><![CDATA[IntegrationTest]]></body><attach><![CDATA[這是attach]]></attach><mch_create_ip><![CDATA[127.0.0.1]]></mch_create_ip><trade_mode><![CDATA[0]]></trade_mode><total_fee><![CDATA[3]]></total_fee><auto_settle><![CDATA[Y]]></auto_settle><nonce_str><![CDATA[5K8264ILTGCH16CQ2502SI8ZNMTM67VS]]></nonce_str><txtPAN><![CDATA[3566703399930071]]></txtPAN><ddlExpYear><![CDATA[27]]></ddlExpYear><ddlExpMonth><![CDATA[12]]></ddlExpMonth><txtCVV2><![CDATA[703]]></txtCVV2><fill_email><![CDATA[clark.liu@acpay.com.tw]]></fill_email><sign><![CDATA[978D6C80C0DA725814008AB4DDEDB1F79CBC02B52722867F7A6D6B28CCD9AB52]]></sign></xml>"}'
# A=A.replace("\\n","")
# A=A.replace(" ","")
# print(A)
# A="{'A':'B','C':'D'}"
# A='{"A":"B","C":"D"}'
# B=json.loads(A)

# some JSON:
x =  '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(A)
# print(y["name"],y["age"],y["city"])