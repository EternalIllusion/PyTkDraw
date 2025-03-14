#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 


from time import strftime,localtime
from codecs import open
logname=f'{__file__}.log'
print('[DEBUG|IO] Output Filename:'+logname,f';\ntime:{strftime("%Y-%m-%d-%H-%M-%S",localtime())}')
#sys.stdout=open(logname,'w','UTF-8')


rootTK=None
import json
from tkinter import messagebox
from time import sleep
from threading import Thread
def rSetTKAttrib(s1,s2,s3,i):
    if rootTK == None:
        return
    else:
        rootTK.wm_attributes("-topmost",i)
def l(I):
            l = os.listdir(I)
            lll=[]
            for ll in l:
                lllll=os.path.join(I,ll)
                if lllll.split('.')[-1] in ['txt','backup'] and not '~$' in lllll.split('.')[0] and os.path.isfile(lllll):
                        try:
                            with open(lllll, 'r') as f:
                                json.load(f)
                            lll.append(ll)
                        except json.JSONDecodeError:pass
                else:pass
            return lll
def save_data(s,f):
    with open(f, 'w') as ff:
        json.dump(s, ff, indent=4)
def fc():
    texts=Fun.GetText('datat','Text_3').replace('\n',',').replace('*','').split(',')#uiEle = Fun.GetElement(uiName,"Text_3").get(1).replace('\n',',').split(',')
    o={}
    if len(texts) < 1 or texts==None:return
    for i in texts:
        #print(i)
        if i in [None,'']:continue
        if chr(9) in i :
            lst=i.split(chr(9))
            try:lst[1]=int(lst[1])
            except:lst[1]=1
            o[lst[0]]=lst[1:2]+[0,False]
        else:o[i]=[1,0,False]
    print("[DEBUG|datat]@fc o=",o)
    attr = Fun.GetElement('datat',"dict_class").get()
    print("[DEBUG|datat]@fc attr=",attr)
    try:save_data(o,attr)
    except:
        rSetTKAttrib('datat','root',"-topmost",0)
        messagebox.showinfo("操作失败", f"数据{attr}保存失败：\nEterIll.CppCore.<fileIO.cpp>:Access Denied.")
        rSetTKAttrib('datat','root',"-topmost",1)
        return
    rSetTKAttrib('datat','root',"-topmost",0)
    messagebox.showinfo("操作成功", f"数据{attr}保存成功")
    rSetTKAttrib('datat','root',"-topmost",1)
def Button_5_onCommand(uiName,widgetName):
    rSetTKAttrib('datat','root',"-topmost",0)
    openPath = tkinter.filedialog.asksaveasfilename(initialdir=os.path.abspath('.'),title='保存名单',filetypes=[('数据文件','*.txt'),('数据备份文件','*.backup'),('All files','*')])
    texts=Fun.GetText('datat','Text_3').replace('\n',',').replace('*','').split(',')#uiEle = Fun.GetElement(uiName,"Text_3").get(1).replace('\n',',').split(',')
    o={}
    if len(openPath) < 1 or openPath in [None,'']:
        rSetTKAttrib('datat','root',"-topmost",1)
        return
    for i in texts:
        #print(i)
        if i in [None,'']:continue
        if chr(9) in i :
            lst=i.split(chr(9))
            try:lst[1]=int(lst[1])
            except:lst[1]=1
            o[lst[0]]=lst[1:2]+[0,False]
        else:o[i]=[1,0,False]
    print("[DEBUG|datat]@save_data o=",o)#attr = Fun.GetElement('datat',"dict_class").get()
    if '.txt' in openPath or '.TXT' in openPath:pass
    else:openPath+='.txt'
    print("[DEBUG|datat]@save_data openPath=",openPath)
    attr=str(openPath).split('/')[-1]
    try:save_data(o,openPath)
    except:
        rSetTKAttrib('datat','root',"-topmost",0)
        messagebox.showinfo("操作失败", f"数据{attr}保存失败：\nEterIll.CppCore.<fileIO.cpp>:Access Denied.")
        rSetTKAttrib('datat','root',"-topmost",1)
        return
    rSetTKAttrib('datat','root',"-topmost",0)
    messagebox.showinfo("操作成功", f"数据{attr}保存成功")
    rSetTKAttrib('datat','root',"-topmost",1)
def Button_6_onCommand(uiName,widgetName):
    ComboBox_13 = Fun.GetElement('datat',"ComboBox_13")
    ComboBox_13.config(values=l(os.getcwd()))
    attr = Fun.GetElement('datat',"dict_class").get()
    print("[DEBUG|datat]@load_data attr=",attr)
    d={}
    o=''
    try:
        with open(attr, 'r') as f:
            d = json.load(f)#        messagebox.showinfo("操作成功", f"数据{attr}加载成功")
    except (FileNotFoundError, json.JSONDecodeError):
        try:
            with open('data.txt', 'r') as f:
                d = json.load(f)#            messagebox.showinfo("操作成功", f"原神数据加载成功")
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("错误", "文件未找到或格式错误，使用默认数据\nEterIll.CppCore.<fileIO.cpp>:Read Access Denied.")#load_data()
    print("[DEBUG|datat]@load_data d=",d)
    v9=chr(9)
    for i in d:
        #print(i)
        if d[i][2]==True:o+='**'+i+'**'+f'{v9} - {d[i][0]}{v9} - {d[i][1]}\n'
        else:o+=i+f'{v9} - {d[i][0]}{v9} - {d[i][1]}\n'
    o=f'姓名{v9} 权重值{v9} 幸运值\n'+o
    print("[DEBUG|datat]@load_data o=",o)
    Fun.SetText('datat','Text_4',o)
