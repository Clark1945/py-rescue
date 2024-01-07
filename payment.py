from flask import Flask,request
from flask import render_template
app = Flask(__name__)

@app.route("/AC_payment",methods=["POST"])
def tx():
    print("開始交易")
    domain = request.values["Domain"]  # 取得POST 表單的值
    behavior = request.values['Behavior']
    tx_type = request.values['Type']

    pay_mode = request.values['PayMode']
    pay_type = request.values['PayType']
    auto_settle = request.values['Auto-Settle']
    merchant_no = request.values['merchantNo']
    order_no = request.values['orderNo']
    transaction_id = request.values['transactionId']
    total_fee = request.values['totalFee']
    settle_fee = request.values['settleFee']
    pan = request.values['pan']
    expire_month = request.values['expireMonth']
    expire_year = request.values['expireYear']
    cvv = request.values['cvv']

    reqxml = """<xml>
    <service><![CDATA[vmj]]></service>
    <version><![CDATA[2.0]]></version>
    <charset><![CDATA[UTF-8]]></charset>
    <sign_type><![CDATA[SHA-256]]></sign_type>
    <merchant_no><![CDATA[""" + merchant_no + """]]></merchant_no>
    <out_trade_no><![CDATA[""" + order_no + """]]></out_trade_no>
    <body><![CDATA[Test Exchange Yee]]></body>
    <attach><![CDATA[測試交Yee]]></attach>
    <mch_create_ip><![CDATA[128.0.0.1]]></mch_create_ip>
    <trade_mode><![CDATA[""" + pay_mode + """]]></trade_mode>
    <total_fee><![CDATA[""" + total_fee + """]]></total_fee>
    <auto_settle><![CDATA[""" + auto_settle + """]]></auto_settle>
    <nonce_str><![CDATA[5K8264ILTGCH16CQ2502SI8ZNMTM67VS]]></nonce_str>
    <txtPAN><![CDATA[""" + pan + """]]></txtPAN>
    <ddlExpYear><![CDATA[""" + expire_year + """]]></ddlExpYear>
    <ddlExpMonth><![CDATA[""" + expire_month + """]]></ddlExpMonth>
    <txtCVV2><![CDATA[""" + cvv + """]]></txtCVV2>
    <fill_email><![CDATA[clark.liu@acpay.com.tw]]></fill_email>
    <sign><![CDATA[76BBCFD8F77EC150028C5B1B973305D9570539E9081B2C5BA0B1B360186A71D6]]></sign>
    </xml>"""

    return "NULL"

@app.route("/TxPage")
def txPage():
    return render_template("TransactionPage.html")


if __name__ == '__main__':
    app.run(debug=True,port=5002)
