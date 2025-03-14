#coding=utf-8
#import libs 
import sys
import result_cmd
import result_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  result:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = result_sty.SetupStyle()
        if isTKroot == True:
            root.title("展示窗口")
            root.overrideredirect(True)
            Fun.WindowDraggable(root,0,'#efefef')
            root.resizable(False,False)
            root.wm_attributes("-transparentcolor","#ffffff")
            Fun.CenterDlg(uiName,root,0,0)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 480,height = 140)
        Form_1.configure(bg = "#ffffff")
        Fun.SetRootRoundRectangle(Form_1,0,0,480,140,radius=40,fill='#efefef',outline='#ffffff',width=0)
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="别紧张",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2,'label_name')
        Label_2.place(x = 0,y = 0,width = 480,height = 120)
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='华文中宋', size=60,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="按住此处拖拽(点击关闭提示)",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_3)
        Label_3.place(x = 160,y = 120,width = 160,height = 20)
        Label_3.configure(relief = "flat")
        Label_3.bind("<Button-1>",Fun.EventFunction_Adaptor(result_cmd.Label_3_onButton1,uiName=uiName,widgetName="Label_3"))
        Button_4 = tkinter.Button(Form_1,text="快速启停",width = 10,height = 4)
        Fun.Register(uiName,'Button_4',Button_4)
        Button_4.place(x = 320,y = 120,width = 120,height = 20)
        Button_4.configure(command=lambda:result_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_5 = tkinter.Button(Form_1,text="X",width = 10,height = 4)
        Fun.Register(uiName,'Button_5',Button_5)
        Button_5.place(x = 440,y = 120,width = 20,height = 20)
        Button_5.configure(bg = "#c47d7d")
        Button_5.configure(activebackground = "#ff0000")
        Button_5.configure(activeforeground = "#ffffff")
        Button_5.configure(command=lambda:result_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_5_Ft=tkinter.font.Font(family='Corbel', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_5.configure(font = Button_5_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        result_cmd.rootTK=root
        
        from threading import Thread
        import animTK
        import ctypes
        user32 = ctypes.windll.user32
        sw = user32.GetSystemMetrics(0)
        def animfunc():
            print("[INFO|Result]Waiting For Tkinter Response ...",end='')
            i=0
            while root==None:
                i=(i+1)%1000000
                if i == 0:print('.',end='')
            print("")
            Thread(target=lambda:animTK.startupanim(root,480,140,abs(sw-480-int(sw*0.2)),0)).start()
        Thread(target=animfunc).start()


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = result(root)
    root.mainloop()
