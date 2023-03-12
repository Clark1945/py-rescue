import hashlib
import tkinter as tk
from tkinter import ttk
import json

class JSONFormatter:
    def __init__(self, master):
        self.master = master
        master.title("Py工具包")
        
        # 設置初始視窗大小
        master.geometry("800x650")  

        # 設置分頁
        notebook = ttk.Notebook(master)
        notebook.pack(expand=True, fill='both')

        page1 = ttk.Frame(notebook)
        notebook.add(page1, text='Json Formatter')
        
        page2 = ttk.Frame(notebook)
        notebook.add(page2, text='Do Sign')
        
        page3 = ttk.Frame(notebook)
        notebook.add(page3, text='分頁3')
        
        # page1 的版面
        self.input_label_1 = tk.Label(page1, text="Input:")
        self.input_label_1.pack()

        self.input_text_1 = tk.Text(page1, height=18, width=80)
        self.input_text_1.pack()

        self.output_label_1 = tk.Label(page1, text="Output:")
        self.output_label_1.pack()

        self.output_text_1 = tk.Text(page1, height=18, width=80)
        self.output_text_1.pack()

        self.format_button_1 = tk.Button(page1, text="Format", command=self.format_json)
        self.format_button_1.pack()
            
        # 創建標籤和輸入框
        self.input_label_2 = tk.Label(page2, text="請輸入要簽名的字符串：")
        self.input_label_2.pack()

        self.input_text_2 = tk.Text(page2, height=18,width=80)
        self.input_text_2.pack()

        
        self.label_2 = tk.Label(page2, text="簽名結果：")
        self.label_2.pack()

        self.signature_text = tk.Text(page2, height=18,width=80)
        self.signature_text.pack()
        
        # 創建按鈕和標籤
        self.sign_button_2 = tk.Button(page2, text="SHA-256", command=self.sign_sha256_message)
        self.sign_button_2.pack()
        
        # 創建按鈕和標籤
        self.sign_button_3 = tk.Button(page2, text="MD5", command=self.sign_md5_message)
        self.sign_button_3.pack()
        

    def format_json(self):
        try:
            input_data = json.loads(self.input_text_1.get("1.0", "end-1c"))
            output_data = json.dumps(input_data, indent=4)
            self.output_text_1.delete("1.0", tk.END)
            self.output_text_1.insert(tk.END, output_data)
        except json.decoder.JSONDecodeError:
            self.output_text_1.delete("1.0", tk.END)
            self.output_text_1.insert(tk.END, "Invalid JSON input")
            
    def sign_sha256_message(self):
        # 獲取輸入的字符串
        message = self.input_text_2.get("1.0", "end-1c")

        # 計算SHA256散列
        hash_object = hashlib.sha256(message.encode())

        # 獲取散列值並轉換為十六進制字符串
        hex_digest = hash_object.hexdigest()
        
        # "Sign遷入"
        msg1 = message[:-8]
        sign_mes="<sign>"+hex_digest+"</sign>"
        new_message=msg1+sign_mes+"\n</xml>"
        
        # 在GUI中顯示簽名
        self.signature_text.delete("1.0", tk.END)
        self.signature_text.insert(tk.END, new_message)
    def sign_md5_message(self):
    # 獲取輸入的字符串
        message = self.input_text_2.get("1.0", "end-1c")
    
        # 計算MD5散列
        hash_object = hashlib.md5(message.encode())
    
        # 獲取散列值並轉換為十六進制字符串
        hex_digest = hash_object.hexdigest()
        
        msg1 = message[:-8]
        sign_mes="<sign>"+hex_digest+"</sign>"
        new_message=msg1+sign_mes+"\n</xml>"
        # 在GUI中顯示簽名
        self.signature_text.delete("1.0", tk.END)
        self.signature_text.insert(tk.END, new_message)

root = tk.Tk()
json_formatter = JSONFormatter(root)
root.mainloop()