from xml.dom.minidom import parseString

dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')
print(dom3.toprettyxml())
# res = format_xml("<xml><service><![CDATA[vmj]]></service><sign><![CDATA[8B3FF79A9AB17FCEA39F78519465817CFB2F9FFAEAEAC8181903E42775F76DD5]]></sign></xml>")
# print(res)
