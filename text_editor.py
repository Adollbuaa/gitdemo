##text_editor
from tkinter.messagebox import showinfo
from tkinter import*
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import webbrowser
top=Tk()
top.title('文本编辑器')
top.geometry('450x200')

label1=Label(top,text='文本:')
label2=Label(top,text='打开文件:')
whitelabel1=Label(top,text='')
whitelabel2=Label(top,text='')
whitelabel3=Label(top,text='温馨提示:')
whitelabel4=Label(top,text='‘文本’与‘打开文件’同时编辑时，默认‘打开文件’')