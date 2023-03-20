import hashlib
import tkinter as tk
from tkinter import ttk
import json
import xml.etree.ElementTree as ET
from ttkbootstrap import Style

class JSONFormatter:
    def __init__(self, master):
        self.master = master
        master.title("Py工具包")
        
        # self.create_widgets()

        # 設置初始視窗大小
        master.geometry("700x700")  

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
        self.input_label_json_1 = ttk.Label(page1, text="請輸入JSON字串")
        self.input_label_json_1.pack()

        self.jsonInput = tk.Text(page1, height=18, width=80)
        self.jsonInput.pack()

        self.output_label_json_2 = tk.Label(page1, text="結果")
        self.output_label_json_2.pack()

        self.jsonOutput = tk.Text(page1, height=18, width=80)
        self.jsonOutput.pack()

        self.format_button_json1 = ttk.Button(page1, text="Format", command=self.format_json,style="success.OutLine.TButton")
        self.format_button_json1.pack()

        # 創建標籤和輸入框
        self.label_sign_1 = tk.Label(page2, text="請輸入要簽名的字符串：")
        self.label_sign_1.pack()

        self.input_text_1 = tk.Text(page2, height=16,width=80)
        self.input_text_1.pack()

        self.label_sign_2 = ttk.Label(page2, text="輸入Key")
        self.label_sign_2.pack()

        self.input_text_2 = tk.Text(page2, height=1,width=80)
        self.input_text_2.pack()

        
        self.sign_output_l1 = ttk.Label(page2, text="簽名結果：")
        self.sign_output_l1.pack()

        self.sign_text = tk.Text(page2, height=16,width=80)
        self.sign_text.pack()
        

        # 創建按鈕和標籤
        self.sign_button_2 = ttk.Button(page2, text="SHA-256", command=self.convert_xml_sha256,style="success.OutLine.TButton")
        self.sign_button_2.pack()
        
        # 創建按鈕和標籤
        self.sign_button_3 = ttk.Button(page2, text="MD5", command=self.convert_xml_md5,style="success.OutLine.TButton")
        self.sign_button_3.pack()


        self.label_getKey_1 = ttk.Label(page4,text="輸入merchant_no")
        self.label_getKey_1.pack()

        self.input_getKey_1 = tk.Text(page4, height=2,width=80)
        self.input_getKey_1.pack()

        self.label_getKey_2 = ttk.Label(page4,text="結果")
        self.label_getKey_2.pack()
        
        self.input_getKey_2 = tk.Text(page4, height=2,width=80)
        self.input_getKey_2.pack()



    # def create_widgets(self):
    #     # 在窗口的左下角添加圖像
    #     img_left = Image.open("img/maple.png")
    #     img_left = img_left.resize((100, 100), Image.LANCZOS)
    #     img_left_tk = ImageTk.PhotoImage(img_left)
    #     canvas_left = tk.Canvas(self.master, width=100, height=100)
    #     canvas_left.pack(side="left", anchor="sw")
    #     canvas_left.create_image(0, 0, anchor="nw", image=img_left_tk)

    #     # 在窗口的右下角添加圖像
    #     img_right = Image.open("img/maple.png")
    #     img_right = img_right.resize((100, 100), Image.LANCZOS)
    #     img_right_tk = ImageTk.PhotoImage(img_right)
    #     canvas_right = tk.Canvas(self.master, width=100, height=100)
    #     canvas_right.pack(side="right", anchor="se")
    #     canvas_right.create_image(0, 0, anchor="nw", image=img_right_tk)    

    def format_json(self):
        try:
            input_data = json.loads(self.jsonInput.get("1.0", "end-1c"))
            output_data = json.dumps(input_data, indent=4)
            self.jsonOutput.delete("1.0", tk.END)
            self.jsonOutput.insert(tk.END, output_data)
        except json.decoder.JSONDecodeError:
            self.jsonOutput.delete("1.0", tk.END)
            self.jsonOutput.insert(tk.END, "Invalid JSON input")
            
    def convert_xml_sha256(self):
        xml_str = self.input_text_1.get("1.0", "end-1c")
        key_str = self.input_text_2.get("1.0", "end-1c")

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
        sign="<sign>"+hash_object.hexdigest().upper()+"</sign>\n"

        xml_str_index = xml_str.index("</xml>")
        ans_xml = xml_str[0:xml_str_index]+sign+xml_str[xml_str_index:]
        self.sign_text.delete("1.0", tk.END)
        self.sign_text.insert(tk.END, ans_xml)


    def convert_xml_md5(self):
        xml_str = self.input_text_1.get("1.0", "end-1c")
        key_str = self.input_text_2.get("1.0", "end-1c")

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
        sign="<sign>"+sign_value.hexdigest().upper()+"</sign>\n"

        xml_str_index = xml_str.index("</xml>")
        ans_xml = xml_str[0:xml_str_index]+sign+xml_str[xml_str_index:]
        self.sign_text.delete("1.0", tk.END)
        self.sign_text.insert(tk.END, ans_xml)

style = Style(theme='darkly')
root = style.master
# root = tk.Tk()
json_formatter = JSONFormatter(root)
root.mainloop()