#coding=utf-8
#import libs 
import sys
import datat_cmd
import datat_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
import json
#Define UI Class
class  datat:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = datat_sty.SetupStyle()
        if isTKroot == True:
            root.title("数据窗口")
            root.wm_attributes("-topmost",1)
            root.resizable(False,False)
            Fun.CenterDlg(uiName,root,0,0)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 480,height = 340)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Text_3 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_3',Text_3)
        Text_3.place(x = 220,y = 10,width = 250,height = 290)
        Text_3.configure(relief = "sunken")
        Text_3_Scrollbar = tkinter.Scrollbar(Text_3,orient=tkinter.VERTICAL)
        Text_3_Scrollbar.place(x = 230,y = 0,width = 20,height = 290)
        Text_3_Scrollbar.config(command = Text_3.yview)
        Text_3.config(yscrollcommand = Text_3_Scrollbar.set)
        Fun.Register(uiName,'Text_3_Scrollbar',Text_3_Scrollbar)
        Text_4 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_4',Text_4)
        Text_4.place(x = 10,y = 10,width = 200,height = 290)
        Text_4.configure(relief = "sunken")
        Text_4_Scrollbar = tkinter.Scrollbar(Text_4,orient=tkinter.VERTICAL)
        Text_4_Scrollbar.place(x = 180,y = 0,width = 20,height = 290)
        Text_4_Scrollbar.config(command = Text_4.yview)
        Text_4.config(yscrollcommand = Text_4_Scrollbar.set)
        Fun.Register(uiName,'Text_4_Scrollbar',Text_4_Scrollbar)
        Button_5 = tkinter.Button(Form_1,text="保存",width = 10,height = 4)
        Fun.Register(uiName,'Button_5',Button_5)
        Button_5.place(x = 310,y = 310,width = 90,height = 20)
        Button_5.configure(command=lambda:datat_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_6 = tkinter.Button(Form_1,text="读取/刷新",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Button_6.place(x = 220,y = 310,width = 80,height = 20)
        Button_6.configure(command=lambda:datat_cmd.Button_6_onCommand(uiName,"Button_6"))
        ComboBox_13_Variable = Fun.AddTKVariable(uiName,'ComboBox_13')
        ComboBox_13 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_13_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_13',ComboBox_13,'dict_class')
        ComboBox_13.place(x = 10,y = 310,width = 200,height = 20)
        ComboBox_13.configure(state = "readonly")
        ComboBox_13["values"]=['data.txt']
        ComboBox_13.current(0)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        datat_cmd.rootTK=root
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
                else:pass
            return lll
        ComboBox_13["values"]=l(os.getcwd())
        Fun.InitElementData(uiName)
                
        import animTK
        from threading import Thread

        def animfunc():
            print("[INFO]Waiting For Tkinter Response ...",end='')
            i=0
            while root==None:
                i=(i+1)%1000000
                if i == 0:print('.',end='')
            print("")
            datat_cmd.Button_6_onCommand('datat','Button_6')
            Thread(target=lambda:animTK.startupanim(root,480,340)).start()
        Thread(target=animfunc).start()

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = datat(root)
    root.mainloop()
