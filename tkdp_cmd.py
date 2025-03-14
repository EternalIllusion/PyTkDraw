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

import json
import threading
from threading import Thread
from time import sleep, time
gmtime=time
from tkinter import messagebox
import random
rootTK=None
t=None

rolling=False
selected_name=False
dictvalues = {
    "张三": [1, 0, False],
    "李四": [1, 0, False],
    "王五": [1, 0, False],
    "赵六": [1, 0, False]
}
sub=0
def subtask():
    global sub
    topmost(0)
    print(sub)
    if sub==1:return
    sys.path.append(os.getcwd())
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import result
    result.result(topLevel)
    sub=1
    tkinter.Tk.wait_window(topLevel)
#st=Thread(target=subtask)
#st.start()
def destroysub(root):
    Fun.Destroy('result','UIClass')
    Fun.Destroy('result','root')
    root.destroy()
    topmost(1)
    subrst()
    foc()
def subrst():
    global sub
    sub=0
########################################################################################################################
########################################################################################################################
#文件IO
def listavailable(pathnow):#遍历文件列表
    import json
    dirnow = os.listdir(pathnow)
    lll=[]
    for ll in dirnow:
        lllll=os.path.join(pathnow,ll)
        if lllll.split('.')[-1] in ['txt'] and not '~$' in lllll.split('.')[0] and os.path.isfile(lllll):
                try:
                    with open(lllll, 'r') as f:
                        json.load(f)
                    lll.append(ll)
                except:pass
        else:pass
    return lll

def load_data():
    ComboBox_13 = Fun.GetElement('tkdp',"ComboBox_13")
    ComboBox_13.config(values=listavailable(os.getcwd()))
    print("[DEBUG]@load_data listavailable=",listavailable(os.getcwd()))
    attr = Fun.GetElement('tkdp',"dict_class").get()
    print("[DEBUG]@load_data attr=",attr)
    label_status=Fun.GetElement('tkdp','label_status')
    try:
        with open(attr, 'r') as f:
            global dictvalues
            dictvalues = json.load(f)
            label_status.config(text=f"操作成功,数据{attr}加载成功")#        messagebox.showinfo("操作成功", f"数据{attr}加载成功")
    except (FileNotFoundError, json.JSONDecodeError):
        label_status.config(text=f"数据{attr}加载失败，使用data.txt")
        try:
            with open('data.txt', 'r') as f:
                dictvalues = json.load(f)#            messagebox.showinfo("操作成功", f"原神数据加载成功")
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("错误", "文件未找到或格式错误，使用默认数据")#load_data()
    print("[DEBUG]@load_data dictvalues=",dictvalues)

def save_data():
    global dictvalues
    with open('data.txt', 'w') as f:
        json.dump(dictvalues, f, indent=4)#    messagebox.showinfo("操作成功", "数据保存成功")


########################################################################################################################
########################################################################################################################

#用户UI_维护
def foc():
    if sub==1:
        button_start=Fun.GetElement('result','Button_4')
        try:button_start.focus()
        except:pass
        return 0
    else:
        button_start=Fun.GetElement('tkdp','func_toggle')
        try:button_start.focus()
        except:pass
        return 0
foc()
def topmost(i):#窗口置顶
    if rootTK == None or sub==1:
        return
    else:
        rootTK.wm_attributes("-topmost",i)
        return


def stop_roll():#滚动停止
    try:
        global t
        global dictvalues
        global rolling
        global selected_name

        rolling = False#杀死滚动线程
        topmost(0)#取消置顶

        total_weight = sum(weight for name, (weight, _, _) in dictvalues.items())
        rand_num =int(random.uniform(0, total_weight))

        temp=[]#临时名单
        for name, (weight, _, _) in dictvalues.items():
                if weight > 0:  # 跳过权重为0的名字
                    temp += weight * [name]
        selected_name = temp[rand_num]#抽卡！爷的回合！

        t=None#防止滚动线程复活
        #展示结果
        if selected_name:
            weight, selected, marked = dictvalues[selected_name]
            dictvalues[selected_name] = [weight, selected + 1, marked]#幸运值增加
            save_data()#保存数据
    except:pass
    button_start=Fun.GetElement('tkdp','func_toggle')
    button_start.config(text="启动！", command=lambda:Button_5_onCommand('tkdp',"Button_5"))
    button_start2=Fun.GetElement('result','Button_4')
    try:button_start2.config(text="快速启停", command=lambda:Button_5_onCommand('tkdp',"Button_5"))
    except:pass
    foc()
    if selected_name:
        if dictvalues[selected_name][2]==True:selected_name=f'*{selected_name}*'
        #print(1,selected_name)
        Fun.SetText('tkdp','label_name',f"{selected_name}")
        Fun.SetText('result','label_name',f"{selected_name}")
        Fun.SetText('tkdp','label_status',f"已经抽到了: {selected_name}")
        Fun.SetText('tkdp',"label_selected",f"{selected_name}{chr(9)}|幸运值:{dictvalues[selected_name][1]}{chr(9)}|权重:{dictvalues[selected_name][0]}")
        Fun.SetText('tkdp','label_name',f"{selected_name}")
        Fun.SetText('result','label_name',f"{selected_name}")
        Fun.SetText('tkdp','label_status',f"已经抽到了: {selected_name}")


def roll_names():
    global dictvalues
    global rolling
    global selected_name

    tms=gmtime()#起始时间
    temp=[]#临时列表（仅展示）
    for name, (_, _, _) in dictvalues.items():temp.append(name)

    while rolling:#滚动循环
        walltime=int((gmtime()-tms)*100000)/100
        total_weight = sum(weight for name, (weight, _, _) in dictvalues.items())
        if total_weight == 0:
            messagebox.showinfo("提示", "权重总和为0，无法进行点名。")
            rolling = False
            stop_roll()
            return
        current = 0
        rnd = int(random.uniform(0,len(temp)))
        sel=temp[rnd]
        if not rolling:
            Fun.SetText('tkdp','label_name',f"{selected_name}")
            Fun.SetText('result','label_name',f"{selected_name}")
            Fun.SetText('tkdp','label_status',f"已经抽到了: {selected_name}")
            return#raise ValueError('Expection Raised To kill the thread.')
        if dictvalues[sel][2]==True:sel=f'*{sel}*'
        Fun.SetText('tkdp','label_name',f"{sel}")
        Fun.SetText('result','label_name',f"{sel}")
        Fun.SetText('tkdp','label_status',f"已经抽到了: {sel}")
        #Fun.SetText('tkdp',"label_selected",f"{sel}")
        if walltime>=20000.0:
            rolling=False
            stop_roll()
            return
        if not rolling:
            Fun.SetText('tkdp','label_name',f"{selected_name}")
            Fun.SetText('result','label_name',f"{selected_name}")
            Fun.SetText('tkdp','label_status',f"已经抽到了: {selected_name}")
            return#raise ValueError('Expection Raised To kill the thread.')
        
    
def plusw():
    global dictvalues
    load_data()
    name = Fun.GetText('tkdp','label_selected')
    name = name.split(chr(9))[0]
    if name in dictvalues:
        weight, selected, marked = dictvalues[name]
        dictvalues[name] = [weight + 1, selected, marked]
        save_data()
        Fun.SetText('tkdp',"label_selected",f"{selected_name}{chr(9)}|幸运值:{dictvalues[selected_name][1]}{chr(9)}|权重:{dictvalues[selected_name][0]}")
        messagebox.showinfo("操作成功", f"{name} 的权重已增加至{weight + 1}")
        return
    elif '*' in name and name.replace('*','') in dictvalues:
        name=name.replace('*','')
        weight, selected, marked = dictvalues[name]
        dictvalues[name] = [weight + 1, selected, marked]
        save_data()
        Fun.SetText('tkdp',"label_selected",f"{selected_name}{chr(9)}|幸运值:{dictvalues[selected_name][1]}{chr(9)}|权重:{dictvalues[selected_name][0]}")
        messagebox.showinfo("操作成功", f"{name} 的权重已增加至{weight + 1}")
        return
    else:messagebox.showinfo("？？？", "你在擀甚麽？")

def minuw():
    global dictvalues
    load_data()
    name = Fun.GetText('tkdp','label_selected')
    name = name.split(chr(9))[0]
    if name in dictvalues:
        weight, selected, marked = dictvalues[name]
        if weight > 0:  # 权重不能小于0
            dictvalues[name] = [weight - 1, selected, marked]
            save_data()
            Fun.SetText('tkdp',"label_selected",f"{selected_name}{chr(9)}|幸运值:{dictvalues[selected_name][1]}{chr(9)}|权重:{dictvalues[selected_name][0]}")
            messagebox.showinfo("操作成功", f"{name} 的权重已减少至{weight - 1}")
            return
        else:messagebox.showinfo("操作失败", f"{name} 的权重不能小于0")
    elif '*' in name and name.replace('*','') in dictvalues:
        name=name.replace('*','')
        weight, selected, marked = dictvalues[name]
        if weight > 0:  # 权重不能小于0
            dictvalues[name] = [weight - 1, selected, marked]
            save_data()
            Fun.SetText('tkdp',"label_selected",f"{selected_name}{chr(9)}|幸运值:{dictvalues[selected_name][1]}{chr(9)}|权重:{dictvalues[selected_name][0]}")
            messagebox.showinfo("操作成功", f"{name} 的权重已减少至{weight - 1}")
            return
        else:messagebox.showinfo("操作失败", f"{name} 的权重不能小于0")
    else:messagebox.showinfo("？？？", "你在擀甚麽？")

def toggle_mark():#标记（未完成）
    global dictvalues
    load_data()
    name = Fun.GetText('tkdp','label_selected')
    if name in dictvalues:
        weight, selected, marked = dictvalues[name]
        dictvalues[name] = [weight, selected, not marked]
        messagebox.showinfo("操作成功", f"{name} 的当前标记状态为{not marked}（功能不完善）")
        save_data()
        return
    elif '*' in name and name.replace('*','') in dictvalues:
        name=name.replace('*','')
        weight, selected, marked = dictvalues[name]
        dictvalues[name] = [weight, selected, not marked]
        messagebox.showinfo("操作成功", f"{name} 的当前标记状态为{not marked}（功能不完善）")
        save_data()
        return
    else:messagebox.showinfo("？？？", "你在擀甚麽？")

 
def Button_5_onCommand(uiName,widgetName):#开始滚动
    global dictvalues
    global rolling
    global selected_name
    global t
    load_data()
    if rolling:
        return
    rolling = True
    label_status=Fun.GetElement(uiName,'label_status')
    button_start=Fun.GetElement(uiName,'func_toggle')
    button_start2=Fun.GetElement('result','Button_4')
    label_status.config(text="滚动中...")
    button_start.config(text="停止", command=stop_roll)
    try:button_start2.config(text="快速启停", command=stop_roll)
    except:pass
    #label_name=Fun.GetElement(uiName,'label_name')
    #label_name.config(text="")
    selected_name = None
    t=None
    foc()
    topmost(1)
    t=Thread(target=roll_names)
    t.start()
    
l_start_roll=lambda:Button_5_onCommand('tkdp',"Button_5")
l_stop_roll=lambda:stop_roll()
dataw=0
def Button_11_onCommand(uiName,widgetName):#数据窗口
    #return
    global dataw
    save_data()
    if dataw==1:return
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import datat
    datat.datat(topLevel)
    dataw=1
    tkinter.Tk.wait_window(topLevel)
    dataw=0
    #print(InputDataArray)

#绑定按键callback
def Button_10_onCommand(uiName,widgetName):
    minuw()
def Button_9_onCommand(uiName,widgetName):
    plusw()
def Button_8_onCommand(uiName,widgetName):
    #st=Thread(target=subtask)
    #st.start()
    subtask()
    button_start2=Fun.GetElement('result','Button_4')
    try:button_start2.config(text="快速启停", command=lambda:Button_5_onCommand('tkdp',"Button_5"))
    except:pass
    #toggle_mark()
def Button_14_onCommand(uiName,widgetName):
    load_data()
def Button_15_onCommand(uiName,widgetName):
    save_data()

########################################################################################################################
########################################################################################################################
import animTK
def animfunc():
    print("[INFO]Waiting For Tkinter Response ...",end='')
    i=0
    while rootTK==None:
        i=(i+1)%1000000
        if i == 0:print('.',end='')
    print("")
    Thread(target=lambda:animTK.startupanim(rootTK,430,330)).start()
Thread(target=animfunc).start()