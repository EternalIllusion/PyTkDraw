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
#sys.stdout=open(logname,'w','UTF-8')
print('[DEBUG|IO] Output Filename:'+logname,f';\ntime:{strftime("%Y-%m-%d-%H-%M-%S",localtime())}')



from threading import Thread
rootTK=None

def Label_3_onButton1(event,uiName,widgetName):
    Label_3=Fun.GetElement(uiName,'Label_3')
    Label_3.place(x = 160,y = 140,width = 160,height = 0)
def Button_5_onCommand(uiName,widgetName):
    from tkdp_cmd import destroysub
    destroysub(rootTK)
def Button_4_onCommand(uiName,widgetName):
    from tkdp_cmd import l_start_roll,l_stop_roll
    button_start=Fun.GetElement('result','Button_4')
    button_start.config(text="快速启停", command=l_stop_roll)
    l_start_roll()

