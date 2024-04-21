import os
import tkinter as tk  # 导入tkinter库，用于创建GUI
from tkinter import ttk  # 导入ttk模块，用于创建更现代的GUI组件
from tkinter import filedialog  # 导入filedialog模块，用于打开文件选择对话框（如果需要的话）
from tkinter import messagebox  # 导入messagebox模块，用于显示消息框

from ai_translator.model import OpenAIModel, AI
from ai_translator.translator.translator import Translator
from ai_translator.translator.pdf_translator import PDFTranslator

api_key_key = "GLM_API_KEY"


# 假设的翻译函数
def translate(text, src_lang, dest_lang):
    model = load_model(model_combobox.get(), model_combobox.get())
    translator = Translator(model=model)
    translated = translator.translate_text(text, src_lang, dest_lang)
    return translated


def translate_pdf_file(pdf_file_path, file_format, target_language):
    output_file_path = pdf_file_path.replace(".pdf", f"_translated")
    model = load_model(model_combobox.get(), model_combobox.get(), os.environ.get(api_key_key))
    translator = PDFTranslator(model=model)
    translator.translate_pdf(pdf_file_path, file_format, target_language, output_file_path)
    return output_file_path

def load_model(ai: str, model: str):
    e_ai = AI.GLMAI
    model_combobox.set("glm-4")
    api_key_key = "GLMAI_API_KEY"

    if ai == "openai":
        e_ai = AI.OPENAI
        model_combobox.set("gpt-3.5-turbo")
        api_key_key = "OPENAI_API_KEY"

    api_key = os.environ.get(api_key_key)

    model = OpenAIModel(ai=e_ai, model=model, api_key=api_key)
    return model


# 翻译文本的函数
def translate_text():
    # 获取原文本和语言选项
    src_text = original_text.get("1.0", tk.END)
    src_lang = src_lang_combobox.get()
    if src_lang == "Autodetection":
        src_lang = ""
    dest_lang = dest_lang_combobox.get()

    # 翻译文本
    translated = translate(src_text, src_lang, dest_lang)

    # 显示翻译后的文本
    translated_text.delete("1.0", tk.END)
    translated_text.insert(tk.END, translated)


# 翻译PDF的函数
def translate_pdf():
    # 弹出文件选择框，选择一个 pdf 文件
    pdf_file_path = filedialog.askopenfilename()
    if not pdf_file_path:
        return

    # 弹出文件选择框，选择一个目标语言
    dest_lang = dest_lang_combobox.get()
    if dest_lang == "Autodetection":
        dest_lang = ""

    # 翻译PDF
    translated = translate_pdf_file(pdf_file_path, file_format="PDF", target_language=dest_lang)

    # 弹框，翻译完成
    messagebox.showinfo("Translate PDF", f"Translated PDF saved to {translated}")

def main():
    # 使用global关键字声明全局变量，这样在其他函数中就可以访问到这些变量了
    global original_text, translated_text, src_lang_combobox, dest_lang_combobox, ai_combobox, model_combobox

    # 创建主窗口
    root = tk.Tk()
    root.title("Translation GUI")  # 设置窗口标题

    # 创建下拉框，选择模型提供商，有 openai 和 glmai
    ai = ["openai", "glmai"]
    ai_combobox = ttk.Combobox(root, values=ai, state="readonly")  # 创建一个下拉框，用于选择模型提供商
    ai_combobox.grid(row=0, column=1, padx=10, pady=10)  # 将下拉框添加到窗口，并设置位置和间距
    ai_combobox.set("glmai")  # 设置默认值

    models = ["gpt-3.5-turbo", "glm-4"]
    model_combobox = ttk.Combobox(root, values=models, state="readonly")  # 创建一个下拉框，用于选择模型
    model_combobox.grid(row=0, column=3, padx=10, pady=10)  # 将下拉框添加到窗口，并设置位置和间距
    model_combobox.set("glm-4")  # 设置默认值

    # 创建按钮
    translate_button = tk.Button(root, text="Translate", command=translate_text)  # 创建一个按钮，用于翻译文本
    translate_button.grid(row=1, column=0, padx=10, pady=10)  # 将按钮添加到窗口，并设置位置和间距

    translate_pdf_button = tk.Button(root, text="Translate PDF", command=translate_pdf)  # 创建一个按钮，用于翻译PDF
    translate_pdf_button.grid(row=1, column=2, padx=10, pady=10)  # 将按钮添加到窗口，并设置位置和间距

    # 创建文本框
    original_text = tk.Text(root, height=10, width=50)  # 创建一个文本框，用于输入原文
    original_text.grid(row=2, column=0, padx=10, pady=10)  # 将文本框添加到窗口，并设置位置和间距

    translated_text = tk.Text(root, height=10, width=50)  # 创建一个文本框，用于显示译文
    translated_text.grid(row=2, column=4, padx=10, pady=10)  # 将文本框添加到窗口，并设置位置和间距

    # 创建下拉框
    src_languages = ["Autodetection", "English", "Spanish", "French", "German", "Chinese"]  # 定义语言选项
    src_lang_combobox = ttk.Combobox(root, values=src_languages, state="readonly")  # 创建一个下拉框，用于选择原文语言
    src_lang_combobox.grid(row=3, column=0, padx=10, pady=20)  # 将下拉框添加到窗口，并设置位置和间距
    src_lang_combobox.set("Autodetection")  # 设置下拉框的默认选项

    dest_languages = ["English", "Spanish", "French", "German", "Chinese"]
    dest_lang_combobox = ttk.Combobox(root, values=dest_languages, state="readonly")  # 创建一个下拉框，用于选择译文语言
    dest_lang_combobox.grid(row=3, column=4, padx=10, pady=20)  # 将下拉框添加到窗口，并设置位置和间距
    dest_lang_combobox.set("Chinese")  # 设置下拉框的默认选项

    # 启动GUI主循环
    root.mainloop()


# 如果这个Python文件是直接运行的，而不是作为模块导入的，那么就执行main函数
if __name__ == "__main__":
    main()
