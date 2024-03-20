import tkinter as tk  # 导入tkinter库，用于创建GUI
from tkinter import ttk  # 导入ttk模块，用于创建更现代的GUI组件
from tkinter import filedialog  # 导入filedialog模块，用于打开文件选择对话框（如果需要的话）
from tkinter import messagebox  # 导入messagebox模块，用于显示消息框


# 假设的翻译函数
def fake_translate(text, src_lang, dest_lang):
    # 这里应该是调用翻译API的代码
    # 现在只是简单地返回原文加上" translated"来模拟翻译过程
    return text + " translated"


# 翻译文本的函数
def translate_text():
    # 获取原文本和语言选项
    src_text = original_text.get("1.0", tk.END)
    src_lang = src_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()

    # 翻译文本
    translated = fake_translate(src_text, src_lang, dest_lang)

    # 显示翻译后的文本
    translated_text.delete("1.0", tk.END)
    translated_text.insert(tk.END, translated)


# 翻译PDF的函数
def translate_pdf():
    # 显示一个信息框，提示PDF翻译功能尚未实现
    messagebox.showinfo("Info", "PDF translation is not implemented yet.")


def main():
    # 使用global关键字声明全局变量，这样在其他函数中就可以访问到这些变量了
    global original_text, translated_text, src_lang_combobox, dest_lang_combobox

    # 创建主窗口
    root = tk.Tk()
    root.title("Translation GUI")  # 设置窗口标题

    # 创建文本框
    original_text = tk.Text(root, height=10, width=50)  # 创建一个文本框，用于输入原文
    original_text.grid(row=0, column=0, padx=10, pady=10)  # 将文本框添加到窗口，并设置位置和间距

    translated_text = tk.Text(root, height=10, width=50)  # 创建一个文本框，用于显示译文
    translated_text.grid(row=0, column=2, padx=10, pady=10)  # 将文本框添加到窗口，并设置位置和间距

    # 创建下拉框
    languages = ["English", "Spanish", "French", "German", "Chinese"]  # 定义语言选项
    src_lang_combobox = ttk.Combobox(root, values=languages, state="readonly")  # 创建一个下拉框，用于选择原文语言
    src_lang_combobox.grid(row=1, column=0, padx=10, pady=5)  # 将下拉框添加到窗口，并设置位置和间距
    src_lang_combobox.set("English")  # 设置下拉框的默认选项

    dest_lang_combobox = ttk.Combobox(root, values=languages, state="readonly")  # 创建一个下拉框，用于选择译文语言
    dest_lang_combobox.grid(row=1, column=2, padx=10, pady=5)  # 将下拉框添加到窗口，并设置位置和间距
    dest_lang_combobox.set("Spanish")  # 设置下拉框的默认选项

    # 创建按钮
    translate_button = tk.Button(root, text="Translate", command=translate_text)  # 创建一个按钮，用于翻译文本
    translate_button.grid(row=2, column=0, padx=10, pady=10)  # 将按钮添加到窗口，并设置位置和间距

    translate_pdf_button = tk.Button(root, text="Translate PDF", command=translate_pdf)  # 创建一个按钮，用于翻译PDF
    translate_pdf_button.grid(row=2, column=2, padx=10, pady=10)  # 将按钮添加到窗口，并设置位置和间距

    # 启动GUI主循环
    root.mainloop()


# 如果这个Python文件是直接运行的，而不是作为模块导入的，那么就执行main函数
if __name__ == "__main__":
    main()
