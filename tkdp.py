#coding=utf-8
#import libs 
import sys
import tkdp_cmd
import tkdp_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
import json
#Define UI Class
class  tkdp:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = tkdp_sty.SetupStyle()
        if isTKroot == True:
            root.title("随机点名v114")
            root.resizable(False,False)
            Fun.CenterDlg(uiName,root,430,330)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 430,height = 330)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_3 = tkinter.Label(Form_1,text="随★机★点★名",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_3)
        Label_3.place(x = 10,y = 10,width = 130,height = 20)
        Label_3.configure(relief = "flat")
        Label_4 = tkinter.Label(Form_1,text="别紧张",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4,'label_name')
        Label_4.place(x = 10,y = 40,width = 410,height = 90)
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='华文中宋', size=60,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Button_5 = tkinter.Button(Form_1,text="启动！",width = 10,height = 4)
        Fun.Register(uiName,'Button_5',Button_5,'func_toggle')
        Button_5.place(x = 10,y = 140,width = 410,height = 30)
        Button_5.configure(command=lambda:tkdp_cmd.Button_5_onCommand(uiName,"Button_5"))
        LabelFrame_6 = tkinter.LabelFrame(Form_1,text="功能",takefocus = True,width = 10,height = 4)
        Fun.Register(uiName,'LabelFrame_6',LabelFrame_6)
        LabelFrame_6.place(x = 10,y = 170,width = 410,height = 120)
        LabelFrame_6.configure(relief = "groove")
        Button_11 = tkinter.Button(LabelFrame_6,text="查看所有数据",width = 10,height = 4)
        Fun.Register(uiName,'Button_11',Button_11,'func_data')
        Button_11.place(x = 8,y = 61,width = 195,height = 30)
        Button_11.configure(command=lambda:tkdp_cmd.Button_11_onCommand(uiName,"Button_11"))
        Label_16 = tkinter.Label(LabelFrame_6,text="如果没有数据请点击刷新，关闭子窗口后才能再打开",width = 10,height = 4)
        Fun.Register(uiName,'Label_16',Label_16,'label_status')
        Label_16.place(x = 8,y = 1,width = 390,height = 30)
        Label_16.configure(anchor = "w")
        Label_16.configure(relief = "flat")
        Button_10 = tkinter.Button(LabelFrame_6,text="减权",width = 10,height = 4)
        Fun.Register(uiName,'Button_10',Button_10,'func_minum')
        Button_10.place(x = 300,y = 31,width = 98,height = 28)
        Button_10.configure(command=lambda:tkdp_cmd.Button_10_onCommand(uiName,"Button_10"))
        Button_9 = tkinter.Button(LabelFrame_6,text="加权",width = 10,height = 4)
        Fun.Register(uiName,'Button_9',Button_9,'func_plusm')
        Button_9.place(x = 200,y = 31,width = 98,height = 28)
        Button_9.configure(command=lambda:tkdp_cmd.Button_9_onCommand(uiName,"Button_9"))
        Button_8 = tkinter.Button(LabelFrame_6,text="打开展示小窗",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8,'func_mark')
        Button_8.place(x = 205,y = 61,width = 195,height = 30)
        Button_8.configure(command=lambda:tkdp_cmd.Button_8_onCommand(uiName,"Button_8"))
        Label_17 = tkinter.Label(LabelFrame_6,text="名字最多七个字",width = 10,height = 4)
        Fun.Register(uiName,'Label_17',Label_17,'label_selected')
        Label_17.place(x = 8,y = 31,width = 190,height = 30)
        Label_17.configure(anchor = "w")
        Label_17.configure(relief = "flat")
        ComboBox_13_Variable = Fun.AddTKVariable(uiName,'ComboBox_13')
        ComboBox_13 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_13_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_13',ComboBox_13,'dict_class')
        ComboBox_13.place(x = 200,y = 10,width = 100,height = 20)
        ComboBox_13.configure(state = "readonly")
        ComboBox_13["values"]=['data.txt']
        ComboBox_13.current(0)
        Button_14 = tkinter.Button(Form_1,text="加载/刷新",width = 10,height = 4)
        Fun.Register(uiName,'Button_14',Button_14,'func_load')
        Button_14.place(x = 300,y = 10,width = 60,height = 20)
        Button_14.configure(command=lambda:tkdp_cmd.Button_14_onCommand(uiName,"Button_14"))
        Button_15 = tkinter.Button(Form_1,text="保存",width = 10,height = 4)
        Fun.Register(uiName,'Button_15',Button_15,'func_save')
        Button_15.place(x = 360,y = 10,width = 60,height = 20)
        Button_15.configure(command=lambda:tkdp_cmd.Button_15_onCommand(uiName,"Button_15"))
        Label_18 = tkinter.Label(Form_1,text="©EternalIllusion,2024   All rights reserved.  Version.114.r5.14",width = 10,height = 4)
        Fun.Register(uiName,'Label_18',Label_18)
        Label_18.place(x = 10,y = 300,width = 410,height = 20)
        Label_18.configure(anchor = "w")
        Label_18.configure(relief = "flat")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        tkdp_cmd.rootTK=root
        def l(I):
            l = os.listdir(I)
            lll=[]
            for ll in l:
                lllll=os.path.join(I,ll)
                if lllll.split('.')[-1] in ['txt'] and not '~$' in lllll.split('.')[0] and os.path.isfile(lllll):
                        try:
                            with open(lllll, 'r') as f:
                                json.load(f)
                            lll.append(ll)
                        except json.JSONDecodeError:pass
                        except:pass
                else:pass
            return lll
        ComboBox_13["values"]=l(os.getcwd())
        Fun.InitElementData(uiName)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = tkdp(root)
    root.mainloop()
