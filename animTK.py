
from math import cos,pi
from time import sleep
animlist=[]
#format:[[type,time,(args),stepnow],~~~]
animfps=50.0
frameclp=1/animfps
def anim(prev,step,target):
    step=float(step)-int(step)
    n=prev+(target-prev)*(cos(step*pi/2-pi/2))
    if abs(n-target)<1.45:n=target
    return n

def winanim(i,t,tkroot,p,q,x,y,p1,q1,x1,y1):
    #print(i,t,tkroot,p,q,x,y,p1,q1,x1,y1)
    p=anim(p,i/t,p1)
    q=anim(q,i/t,q1)
    x=anim(x,i/t,x1)
    y=anim(y,i/t,y1)
    tkroot.geometry(f'{int(p)}x{int(q)}+{int(x)}+{int(y)}')
    #print(p)
    return

def textanim(i,t,uiName,elementName,p,q,x,y,p1,q1,x1,y1):
    try:ele=Fun.GetElement(uiName,elementName)
    except:return
    ele.place(x = anim(x,i/t,x1),y = anim(y,i/t,y1),width = anim(q,i/t,q1),height = anim(p,i/t,p1))
        #print(ele['padx'],ele['pady'])
        #tkroot.geometry(f'{int(p)}x{int(q)}+{int(x)}+{int(y)}')
        #print(p)
    return

def reganim(animtype,animtime,animargs):
    global animlist
    if animtype in ['win','text']:
        animlist.append([animtype,animtime,animargs,0])
        print(f'[INFO|AnimTK] animlist <- {[animtype,animtime,animargs,0]}')
    return animargs[len(animargs)-4:]
    #return animargs[-4:]

def animthread():
    while animthreadobjFlag:
        sleep(frameclp)
        i=0
        #print(1)
        global animlist
        for i in range(len(animlist)):
            try:animlist[i]=animlist[i]
            except:continue
            if animlist[i][0]=='win':
                winanim(animlist[i][3],animlist[i][1],*animlist[i][2])
                animlist[i][3]=animlist[i][3]+1
                if animlist[i][3]>=animlist[i][1]:animlist.pop(i)
            try:animlist[i]=animlist[i]
            except:continue 
            if animlist[i][0]=='text':
                textanim(animlist[i][3],animlist[i][1],*animlist[i][2])
                animlist[i][3]=animlist[i][3]+1
                if animlist[i][3]>=animlist[i][1]:animlist.pop(i)

animthreadobj=None
animthreadobjFlag=True
def runanimthread():
    print('[INFO|AnimTK]animation thread started running!')
    global animthreadobj
    global animthreadobjFlag
    from threading import Thread
    animthreadobjFlag=True
    animthreadobj=Thread(target=animthread)
    animthreadobj.start()

def stopanimthread():
    print('[INFO|AnimTK]animation thread stopped running!')
    global animlist
    global animthreadobjFlag
    animthreadobjFlag=False
    animlist=[]

def waituntil(typeof):
    l = [i[0] for i in animlist]
    while typeof in l:
        sleep(frameclp)
        l = [i[0] for i in animlist]


def startupanim(rootTK,dw=0,dh=0,tx=0.1,ty=0.1):
    import ctypes
    user32 = ctypes.windll.user32
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    p1,q1=0,0
    t=25#*20ms
    if dw == 0:dw = rootTK.winfo_width()
    if dh == 0:dh = rootTK.winfo_height()
    if tx == 0.1:tx = (sw-dw)/2
    if ty == 0.1:ty = (sh-dh)/2
    runanimthread()
    p1,q1,x1,y1=reganim('win',t,[rootTK,p1,q1,sw,sh,dw,dh,tx,ty])
    waituntil('win')
    stopanimthread()
