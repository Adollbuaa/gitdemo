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

label1.grid(column=1,row=1,columnspan=1,rowspan=1)
label2.grid(column=1,row=3,columnspan=1,rowspan=1)
whitelabel1.grid(column=1,row=2,columnspan=1,rowspan=1)
whitelabel2.grid(column=1,row=4,columnspan=1,rowspan=1)
whitelabel3.grid(column=1,row=6,columnspan=1,rowspan=1)
whitelabel4.grid(column=2,row=7,columnspan=1,rowspan=1)

textbox1=Entry(top)
textbox2=Entry(top)
textbox1.grid(column=2,row=1,columnspan=1,rowspan=1)
textbox2.grid(column=2,row=3,columnspan=1,rowspan=1)

def select(textbox1,textbox2,top):
    essay=textbox1.get()
    file=textbox2.get()
    if essay=='' and file=='':
        messagebox.showinfo("请输入文本或位置后再次查询")
    else :
        if essay!='':
            essay=essay
        else:
            f=open(file)
            essay=f.read()
            
            #查找文本内容，使得文本内容为essay # G:\学习\大计基\大计基\The Diary of Anne Frank.txt
        top.destroy
        Tk1=Tk()
        Tk1.title('文本编辑器')
        Tk1.geometry('700x480')
        tk1label1=Label(Tk1,text='开始')
        button11=Button(Tk1,text='文本助手',command=lambda:text_analyze1(essay,Tk1))
        button13=Button(Tk1,text='关闭',command=Tk1.destroy)
        button12=Button(Tk1,text='更多帮助',command=lambda:text_service1(Tk1))
        
        tk1label1.grid(column=0,row=2,columnspan=1,rowspan=1)
        button11.grid(column=1,row=1,columnspan=1,rowspan=1)
        button12.grid(column=2,row=1,columnspan=1,rowspan=1)
        button13.grid(column=13,row=14,columnspan=1,rowspan=1)
        
        text_edit= Text(Tk1, width=60, height=20)
        text_edit.grid(row=3, column=1, rowspan=10, columnspan=10)
        text_edit.insert(INSERT,essay)
        top_Scrollbar=Scrollbar(Tk1)
        top_Scrollbar.config(command=text_edit.yview)
        text_edit.config(yscrollcommand=top_Scrollbar.set)
        top_Scrollbar.grid(row=3, column=13, rowspan=10,sticky='NS')
        
        button14=Button(Tk1,text='保存',command=lambda:text_keep(Tk1,text_edit,file))
        button14.grid(column=1,row=14,columnspan=1,rowspan=1)
        
        tk1label2=Label(Tk1,text='系统有待升级，当前仅支持打开文件状态下保存')
        tk1label2.grid(column=1,row=15,columnspan=3,rowspan=1)
        Tk1.mainloop()
        #文本助手
def text_analyze1(essay,Tk1):
    Tk2=Tk()
    Tk2.title('文本助手')
    Tk2.geometry('300x200')
    button20=Button(Tk2,text='查找词频',command=lambda:text_find1(essay,Tk2))
    button21=Button(Tk2,text='查看单词与词频',command=lambda:text_analyze2(essay,Tk2))
    button22=Button(Tk2,text='关键词柱状图',command=lambda:picture(real_num(essay,1),real_num(essay,2)))
    button23=Button(Tk2,text='关闭',command=Tk2.destroy)
    button20.pack(anchor=CENTER)
    button21.pack(anchor=CENTER)
    button22.pack(anchor=CENTER)
    button23.pack(anchor=CENTER)
    Tk2.mainloop()
    def text_analyze2(essay,Tk2):
    print('文档转换后的单词序列为：')
    print(','.join(text_apart(essay)))
    print('文档中单词对应的频次为：')
    print(text_count(text_apart(essay),3))
def text_apart(essay):
    essay1=list(essay)
    alist=list('abcdefghijklmnopqrstuvwxyz')
    book=[]
    wordone=''
    for i in range (len(essay1)):
        every=essay1[i].lower()
        if every in alist:
            wordone+=every
        else:
            if wordone=='':
                wordone=''
            else:
                book+=[wordone]
                wordone=''
    return book