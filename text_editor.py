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
    def text_count(text_count1,x):
    sumnum=len(text_count1)
    wordtwo=[]
    num=[]
    d={}
    for i in (text_count1):
        if i in wordtwo:
            wordtwo=wordtwo
            fiction=wordtwo.index(i)
            num[fiction]+=1
        else:
            wordtwo+=[i]
            num+=[1]
    for i in range (len(num)):
        d[wordtwo[i]]=num[i]
    if x==1:
        return wordtwo
    elif x==2:
        return num
    elif x==3:
        return d
def real_num(real_num1,x):
    #停用词表
    stoplist =['a','is','the','in','to']+ ['very', 'ourselves', 'am', 'doesn', 'through', 'me', 'against', 'up', 'just', 'her', 'ours',  'couldn', 'because', 'is', 'isn', 'it', 'only', 'in', 'such', 'too', 'mustn', 'under', 'their', 'if', 'to', 'my', 'himself', 'after', 'why', 'while', 'can', 'each', 'itself', 'his', 'all', 'once', 'herself', 'more', 'our', 'they', 'hasn', 'on', 'ma', 'them', 'its', 'where', 'did', 'll', 'you', 'didn', 'nor', 'as', 'now', 'before', 'those', 'yours', 'from', 'who', 'was', 'm', 'been', 'will', 'into', 'same', 'how', 'some', 'of', 'out', 'with', 's', 'being', 't', 'mightn', 'she', 'again', 'be', 'by', 'shan', 'have', 'yourselves', 'needn', 'and', 'are', 'o', 'these', 'further', 'most', 'yourself', 'having', 'aren', 'here', 'he', 'were', 'but', 'this', 'myself', 'own', 'we', 'so', 'i', 'does', 'both', 'when', 'between', 'd', 'had', 'the', 'y', 'has', 'down', 'off', 'than', 'haven', 'whom', 'wouldn', 'should', 've', 'over', 'themselves', 'few', 'then', 'hadn', 'what', 'until', 'won', 'no', 'about', 'any', 'that', 'for', 'shouldn', 'don', 'do', 'there', 'doing', 'an', 'or', 'ain', 'hers', 'wasn', 'weren', 'above', 'a', 'at', 'your', 'theirs', 'below', 'other', 'not', 're', 'him', 'during', 'which']
    t=0
    maxbox1=[]
    maxbox2=[]
    wordtwo=text_count(text_apart(real_num1),1)
    num=text_count(text_apart(real_num1),2)
    while num!=[]:
        nummax=max(num)
        wordmax=wordtwo[num.index(nummax)]
        wordtwo.remove(wordmax)
        num.remove(nummax)
        if wordmax in stoplist:
            t=t
        else:
            maxbox1+=[wordmax]
            maxbox2+=[nummax]
            t+=1
    if x==1:
        return(maxbox1)
    if x==2:
        return(maxbox2)
        def text_find1(essay,Tk2):
    Tk3=Tk()
    Tk3.title('词频查询')
    Tk3.geometry('300x200')
    n=len(text_apart(essay))
    allword_label=Label(Tk3,text='总词数:'+str(n))
    none_label1=Label(Tk3,text='')
    none_label2=Label(Tk3,text='')
    none_label3=Label(Tk3,text='')
    first_label=Label(Tk3,text='单词(小写)')
    then_label=Label(Tk3,text='频次')
    find_textbox1=Entry(Tk3)
    find_textbox2=Entry(Tk3)
    allword_label.grid(column=1,row=1,columnspan=1,rowspan=1)
    first_label.grid(column=1,row=3,columnspan=1,rowspan=1)
    then_label.grid(column=1,row=5,columnspan=1,rowspan=1)
    find_textbox1.grid(column=2,row=3,columnspan=1,rowspan=1)
    find_textbox2.grid(column=2,row=5,columnspan=1,rowspan=1)
    none_label1.grid(column=1,row=2,columnspan=1,rowspan=1)
    none_label2.grid(column=1,row=4,columnspan=1,rowspan=1)
    none_label3.grid(column=1,row=6,columnspan=1,rowspan=1)
    
    button31=Button(Tk3,text='查询',command=lambda:text_find2(essay,find_textbox1,find_textbox2,Tk3,text_count(text_apart(essay),3)))
    button31.grid(column=1,row=7,columnspan=1,rowspan=1)
    button32=Button(Tk3,text='退出',command=lambda:Tk3.destroy)
    button32.grid(column=3,row=7,columnspan=1,rowspan=1)
def text_find2(essay,find_textbox1,find_textbox2,Tk3,b_d):
    find1=find_textbox1.get()
    find2=text_count(text_apart(essay),3)
    find3=find2[find1]
    find_textbox2.insert(INSERT,find3)
    
    
def picture(x,y):
    plt.bar(x[0:6],y[0:6],0.8,label='Key Words')
    plt.legend()
    plt.xlabel('Words')
    plt.ylabel('Frequency') 
    plt.show()