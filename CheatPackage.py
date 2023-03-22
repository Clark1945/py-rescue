import hashlib
import tkinter as tk
from tkinter import ttk
import json
import xml.etree.ElementTree as ET
from ttkbootstrap import Style
import requests
requests.packages.urllib3.disable_warnings()

class JSONFormatter:
    def __init__(self, master):
        self.master = master
        master.title("Py工具包")
        
        # self.create_widgets()

        # 設置初始視窗大小
        master.geometry("700x625")  

        # 設置分頁
        notebook = ttk.Notebook(master,bootstyle="success")
        notebook.pack(expand=True, fill='both')

        page1 = ttk.Frame(notebook)
        notebook.add(page1, text='Json Formatter')
        
        page2 = ttk.Frame(notebook)
        notebook.add(page2, text='Sign')
        
        page3 = ttk.Frame(notebook)
        notebook.add(page3, text='GetKey')

        page4 = ttk.Frame(notebook)
        notebook.add(page4, text='Post')
        
        # page1 的版面
        self.json_label_1 = ttk.Label(page1, text="請輸入JSON字串")
        self.json_label_1.pack()

        self.json_text_1 = tk.Text(page1, height=15, width=80)
        self.json_text_1.pack()

        self.json_label_2 = tk.Label(page1, text="結果")
        self.json_label_2.pack()

        self.json_text_2 = tk.Text(page1, height=15, width=80)
        self.json_text_2.pack()

        self.json_button_1 = ttk.Button(page1, text="Format", command=self.format_json,style="success.OutLine.TButton")
        self.json_button_1.pack()

        # 創建標籤和輸入框
        self.sign_label_1 = tk.Label(page2, text="請輸入要簽名的字符串：")
        self.sign_label_1.pack()

        self.sign_text_1 = tk.Text(page2, height=14,width=80)
        self.sign_text_1.pack()

        self.sign_label_2 = ttk.Label(page2, text="輸入Key")
        self.sign_label_2.pack()

        self.sign_text_2 = tk.Text(page2, height=1,width=80)
        self.sign_text_2.pack()

        self.sign_label_3 = ttk.Label(page2, text="簽名結果：")
        self.sign_label_3.pack()

        self.sign_text_3 = tk.Text(page2, height=14,width=80)
        self.sign_text_3.pack()
        
        # 創建按鈕和標籤
        self.sign_button_1 = ttk.Button(page2, text="SHA-256", command=self.convert_xml_sha256,style="success.OutLine.TButton")
        self.sign_button_1.pack()
        
        # 創建按鈕和標籤
        self.sign_button_2 = ttk.Button(page2, text="MD5", command=self.convert_xml_md5,style="success.OutLine.TButton")
        self.sign_button_2.pack()


        self.getKey_label_1 = ttk.Label(page3,text="輸入merchant_no")
        self.getKey_label_1.pack()

        self.getKey_text_1 = tk.Text(page3, height=1,width=80)
        self.getKey_text_1.pack()

        self.getKey_label_2 = ttk.Label(page3,text="結果")
        self.getKey_label_2.pack()
        
        self.getKey_text_2 = tk.Text(page3, height=1,width=80)
        self.getKey_text_2.pack()

        self.getKey_button_1 = ttk.Button(page3, text="GenerateKey", command=self.send_get,style="success.OutLine.TButton")
        self.getKey_button_1.pack()
        

        self.post_label_1 = ttk.Label(page4,text="Request Content")
        self.post_label_1.pack()

        self.post_text_1 = tk.Text(page4, height=15,width=80)
        self.post_text_1.pack()

        self.post_label_2 = ttk.Label(page4,text="URL")
        self.post_label_2.pack()

        self.def_url = tk.StringVar(page4)

        self.drop = ttk.OptionMenu(page4,self.def_url,"https://aiodir.payloop.com.tw/","https://aio.payloop.com.tw/Capture","https://aio.payloop.com.tw/Reverse","取消請款","https://aio.payloop.com.tw/Refund","取消退貨","https://aio.payloop.com.tw/Query","https://aiodir.payloop.com.tw/")
        self.drop.pack()


        self.post_label_3 = ttk.Label(page4,text="Response Content")
        self.post_label_3.pack()

        self.post_text_3 = tk.Text(page4, height=15,width=80)
        self.post_text_3.pack()

        self.post_button = ttk.Button(page4, text="Post", command=self.post,style="success.OutLine.TButton")
        self.post_button.pack()


    def format_json(self):
        try:
            input_data = json.loads(self.json_text_1.get("1.0", "end-1c"))
            output_data = json.dumps(input_data, indent=4)
            self.json_text_2.delete("1.0", tk.END)
            self.json_text_2.insert(tk.END, output_data)
        except json.decoder.JSONDecodeError:
            self.json_text_2.delete("1.0", tk.END)
            self.json_text_2.insert(tk.END, "Invalid JSON input")
            
    def convert_xml_sha256(self):
        xml_str = self.sign_text_1.get("1.0", "end-1c")
        key_str = self.sign_text_2.get("1.0", "end-1c")

        # 簽章加入XML
        try :
            start_point = xml_str.index("<sign>")
            end_point = xml_str.index("</sign>") 
            xml_str=xml_str[0:start_point-1]+xml_str[end_point+7:]
        except:
            print("No Sign")   
        # Parse XML string into a dictionary
        xml_dict = {}
        root = ET.fromstring(xml_str)

        for child in root:
            xml_dict[child.tag] = child.text
        sorted_xml = sorted(xml_dict.items())
        
        # Construct query string
        query = ""
        for item in sorted_xml:
            query += f"{item[0]}={item[1]}&"
        query += f"key={key_str}"
        
        hash_object = hashlib.sha256(query.encode())

        # 獲取散列值並轉換為十六進制字符串
        sign="<sign><![CDATA["+hash_object.hexdigest().upper()+"]]></sign>\n"

        xml_str_index = xml_str.index("</xml>")
        ans_xml = xml_str[0:xml_str_index]+sign+xml_str[xml_str_index:]
        self.sign_text_3.delete("1.0", tk.END)
        self.sign_text_3.insert(tk.END, ans_xml)
        self.post_text_1.delete("1.0", tk.END)
        self.post_text_1.insert(tk.END, ans_xml)

    def convert_xml_md5(self):
        xml_str = self.sign_text_1.get("1.0", "end-1c")
        key_str = self.sign_text_2.get("1.0", "end-1c")

        # 簽章加入XML
        try :
            start_point = xml_str.index("<sign>")
            end_point = xml_str.index("</sign>") 
            xml_str=xml_str[0:start_point-1]+xml_str[end_point+7:]
        except:
            print("No Sign")   

        # Parse XML string into a dictionary
        xml_dict = {}
        root = ET.fromstring(xml_str)
        for child in root:
            xml_dict[child.tag] = child.text
        sorted_xml = sorted(xml_dict.items())
        # Construct query string
        query = ""
        for item in sorted_xml:
            query += f"{item[0]}={item[1]}&"
        query += f"key={key_str}"
        sign_value = hashlib.md5()
        sign_value.update(query.encode(encoding='utf-8'))
        # self.signature_text.config(text=sign_value.hexdigest().upper())
        sign="<sign><![CDATA["+sign_value.hexdigest().upper()+"]]></sign>\n"

        xml_str_index = xml_str.index("</xml>")
        ans_xml = xml_str[0:xml_str_index]+sign+xml_str[xml_str_index:]
        self.sign_text_3.delete("1.0", tk.END)
        self.sign_text_3.insert(tk.END, ans_xml)
        self.post_text_1.delete("1.0", tk.END)
        self.post_text_1.insert(tk.END, ans_xml)

    def send_get(self):
        # 獲取輸入文本框中的內容
        merchant_no = self.getKey_text_1.get("1.0", "end-1c")
        cdeRelayUrl = "https://cde-relay.payloop.com.tw/"
        request=cdeRelayUrl+"api/merchant/default/term"+"?"+"merchantNo="+str(merchant_no)

        header = {"Content-Type": "application/json; charset=utf-8"}
        req = requests.get(request,headers=header,allow_redirects=False, verify=False, timeout=30)
        temp_text = req.text
        
        json_text = json.loads(temp_text)
        json_key = json_text["kword"]
        
        # 在回傳值文本框中顯示回傳值
        self.getKey_text_2.delete("1.0", tk.END)
        self.getKey_text_2.insert(tk.END, json_key)
        self.sign_text_2.delete("1.0", tk.END)
        self.sign_text_2.insert(tk.END, json_key)

    def post(self):
        request = self.post_text_1.get("1.0", "end-1c")
        url = self.def_url.get()
        header={"Content-Type": "application/xml; charset=utf-8"}
        res = requests.post(url,headers=header,data=request.encode('utf-8'),allow_redirects=False, verify=False, timeout=30)
        self.post_text_3.delete("1.0", tk.END)
        self.post_text_3.insert(tk.END,res.text)
        

style = Style(theme='darkly')
root = style.master
json_formatter = JSONFormatter(root)
root.mainloop()