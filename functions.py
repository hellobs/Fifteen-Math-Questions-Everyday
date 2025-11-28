import tkinter.messagebox
import tkinter.colorchooser
import tkinter.filedialog
from tkinter import *
#from PIL import Image,ImageTk
import subprocess
import random
import time
import pickle
import os
import logging
import traceback
import tkinter.ttk as ttk
from json import loads as LOAD
from json import dumps as DUMP

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("storage\data.log")
formatter = logging.Formatter(
                    '%(asctime)s - %(filename)s[line:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



def log(text="",types="info",timea="start"):
    '''
    记录日志
    类型: info debug warning error critical times
    timea: (start \ end)
    '''
    for x in ["info","debug","warning","error","critical"]:
        if types == x:
            strings = "logger"+"."+x
            eval(strings)(text)
    if types == "times":
        if timea == "start":
            logger.info("开启时间:"+time.asctime())
        else:
            logger.info("关闭时间:" + time.asctime())
        
def for_shop(func):
    def wrapper(self=None, *args, **kwrd):
        try:
            func(self, *args, **kwrd)
        except Exception as e:
            print(e)
            tkinter.messagebox.showinfo("注意", "重启后方可使用")
    return wrapper

def catch_error(func):
    '''捕捉错误'''
    def wrapper(self=None,*args,**kwrd):
        try:
            func(self, *args, **kwrd)
        except Exception as e:
            print("发生错误:" + str(e))
            error_text = traceback.format_exc()
            tkinter.messagebox.showerror("错误", "".join(("程序出现错误，请联系作者解决\n错误代码:\n", error_text \
                , "\n错误信息已记入至日志中\n")))
            log(text="发生错误:" + str(e), types="error")
            
        finally:
            #正常通过
            pass
    return wrapper

def repair():
    '''
    修复存档（使用备份）
    返回读取值
    '''
    with open("config.dat", 'wb') as file:
        with open("data.dat.bak", 'rb') as bak:
            file.write(bak.read())
            bak.close()
        
    fileobj = open("config.dat", "rb") 
    return pickle.load(fileobj)

try:
    b = open("config.dat","rb")
    f = pickle.load(b)
    b.close()
except Exception as e:
    print("第一次错误:"+str(e))
    '''repair'''
    f = repair()
finally:
    print("数据:"+str(f))


def help_py():
    "open help.exe"
    os.system('help.exe')

@for_shop
def mycanvas(self=None):
    b = open("config.dat","rb")
    f = pickle.load(b)
    b.close()
    print("数据"+str(f))
    if f["lock_draw"] == False:
            tkinter.messagebox.showwarning("注意","你还没解锁!")
            return ''
    '''打开自带笨笨画图'''
    os.popen("mycanvas.exe")

class functions():
    def __init__(self):
        '''此类为每天十五道题的函数'''
        self.functions_number = 0
        self.D = 0              #var的数量
        self.init_undo = False  #判断是否要重做var
        
    def __str__(self):
        print("每天十五道题")
    
    def help_html(self):
        '''这是一个打开帮助网页的函数'''
        os.popen("versions.html")
        
    def write_data(self):
        '''此函数用来写日志'''
        self.f = open("storage/data.txt",'a')
        self.f.write("\n")
        self.f.write(str('打开时间'+' '+time.asctime()))
        self.f.close()

    def give_money(self):
        '''打赏'''
        self.m = Toplevel()
        self.m.title("打赏")
        self.m.iconbitmap('favicon.ico')
        self.m.geometry("500x500")
        self.mo = Frame(self.m)
        try:
            from PIL import Image, ImageTk
        except ModuleNotFoundError as e:
            tkinter.messagebox.showerror("错误", "所依赖的库未找到!")
        self.image = Image.open("image/give_money.png")
        self.tkimage = ImageTk.PhotoImage(image=self.image)
        
        Label(self.mo, text="谢谢打赏！").pack(pady=10)
        Label(self.mo, text="感谢您对作者的支持!").pack(pady=5)
        Label(self.mo,image=self.tkimage).pack(pady=30)
        self.mo.pack()

    def easy_text(self):
        '''小本子'''
        b = open("config.dat","rb")
        f = pickle.load(b)
        b.close()
        print("数据"+str(f))
        if f["lock_notepad"] is False:
            tkinter.messagebox.showwarning("注意","你还没解锁!")
            return ''
        self.showe = Tk()
        self.showe.iconbitmap("favicon.ico")
        self.showe.title("小本子")
        self.text = Text(self.showe,pady=5)
        self.scroll = Scrollbar(self.showe)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.text.pack(side=LEFT,fill=BOTH)
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

    def startend(self):
        "当开启时，原本出现的元件消失"
        self.butstart.pack_forget()
        self.labelstart.pack_forget()
        self.startending = True
        self.clock()
        
    def clean(self):
        "将信息清除"
        with open("storage/data.log", 'w') as self.file:
            self.file.write("")
        with open("storage/exam_list.txt","w") as self.file2:
            self.file2.write("")
        time.sleep(0.1)
        tkinter.messagebox.showinfo("提示", "已清除信息")
        
    def get_usetime(self):
        "停止时间"
        self.timeb = time.time()
        self.a1 = self.timeb - self.timea
        self.a2 = self.a1 / 60
        self.minutes = int(self.a2)
        self.second = (self.a2 - self.minutes) * 60
        self.timec = str(self.minutes) + "分" + str(round(self.second)) + "秒"
        return self.timec
        
    def Set(self):
        "用来准备显示题目"
        self.D += 1
        if self.D > 15:
            self.D = 0
        for x in range(1, 16):
            strings = """
if self.D == """ + str(x) + ''':
    self.var''' + str(x) + '''.set(self.label''' + str(x) + ''')'''
            exec(strings)
                    
    def again(self):
        "将所有输入框禁用"
        for x in range(1,16):
            strings = "self.entry"+str(x)+r".config(state=DISABLED)"
            eval(strings)

    def clock(self):
        "开启计时"
        self.timea = time.time()

    def print_exam(self):
        '''打印题目'''
        b = open("config.dat","rb")
        f = pickle.load(b)
        b.close()
        print("数据"+str(f))
        if f["lock_print_exam"] is False:
            tkinter.messagebox.showwarning("注意","你还没解锁!")
            return ''
        try:
            for x in range(1,16):
                strings = "self.textl"+str(x)+" = self.var"+str(x)+".get()"
                exec(strings)
            
            self.file = tkinter.filedialog.asksaveasfile(mode="w", filetypes=[("文本文件", ".txt"), ("文档文件", ".doc"), ("每天十五道题文件", ".efe")], defaultextension=True)
            for x in range(1,16):
                strings = "self.file.writelines(self.textl"+str(x)+r'+"\n")'
                eval(strings)
            self.file.close() 
        except FileNotFoundError:
            tkinter.messagebox.showwarning(title="警告",message="您没有选择任何文件！")
            return
        except AttributeError:
            tkinter.messagebox.showwarning(title="警告", message="已取消")
            return 
        tkinter.messagebox.showinfo("提示","完成")     

    def open_data(self):
        "打开日志"
        try:
            self.data_file = open("storage/data.log",'r')
            self.datashow = Tk()
            self.datashow.title("日志")
            self.datashow.iconbitmap("favicon.ico")
            self.text = Text(self.datashow,pady=5)
            self.scroll = Scrollbar(self.datashow)
            self.scroll.pack(side=RIGHT,fill=Y)
            self.text.pack(side=LEFT,fill=Y)
            self.scroll.config(command=self.text.yview)
            self.text.config(yscrollcommand=self.scroll.set)
            self.a = self.data_file.readlines()
            for x in self.a:
                self.text.insert(1.0,x)
            
        except IOError:
            self.answer = tkinter.messagebox.askquestion("注意","貌似日志文件被某程序删了，是否重建？")
            if self.answer == 1:
                self.file = open("storage/data.log",'w')
                self.file.write("")
                self.file.close()

    def EXAM(self,List=[]):
        "List参数:加载答案"
        "将会返回一个用于便利显示错误的列表"
        "判断有多少对，多少错"
        "c,T,F"
        for x in range(1, 16):
            strings = "self.a" + str(x) + " = self.entry" + str(x) + ".get()"
            exec(strings)
        self.T = 0
        self.F = 0
        self.A = 15
        self.wrong_list = []
        
        if self.a1 == str(List[0]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl1)
            
        if self.a2 == str(List[1]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl2)
        if self.a3 == str(List[2]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl3)
        if self.a4 == str(List[3]):
            self.T += 1
            
        else:
            self.F += 1
            self.wrong_list.append(self.textl4)
        if self.a5 == str(List[4]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl5)
        if self.a6 == str(List[5]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl6)
        if self.a7 == str(List[6]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl7)
        if self.a8 == str(List[7]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl8)
        if self.a9 == str(List[8]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl9)
        if self.a10 == str(List[9]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl10)
        if self.a11 == str(List[10]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl11)
        if self.a12 == str(List[11]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl12)
        if self.a13 == str(List[12]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl13)
        if self.a14 == str(List[13]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl14)
        if self.a15 == str(List[14]):
            self.T += 1
        else:
            self.F += 1
            self.wrong_list.append(self.textl15)
        
        print("正确"+str(self.T))
        print("错误"+str(self.F))

    def change_wrong_text_color(self, text_wrong_color="red"):
        '''错误的题改变颜色'''
        for labels in self.wrong_list:
            labels.config(bg=text_wrong_color)
    
    @for_shop
    def change_color(self):
        '''改变颜色'''
        b = open("config.dat","rb")
        f = pickle.load(b)
        b.close()
        print("数据"+str(f))
        if f["lock_color_change_color"] is False:
            tkinter.messagebox.showwarning("注意","你还没解锁!")
            return ''
            
        self.colorlist = colorchooser.askcolor()
        self.color = self.colorlist[1]
        self.backgroundcolor = self.color
        self.frame.config(bg=self.backgroundcolor)
        self.use_color(self.backgroundcolor)

    def use_color(self,data:dict):
        '''使用颜色'''
        self.backgroundcolor = data["bg"]
        self.leftframecolor = data["leftframecolor"]
        self.wrongcolor = data["wrongbg"]
        try:
            for x in range(1,16):
                strings = "self.text"+str(x)+".config(bg=self.backgroundcolor)"
                eval(strings)
        except AttributeError as e:
            print("用户没有点击开始")
        
        self.frame.config(bg=self.backgroundcolor)
        self.leftframe.config(bg=self.leftframecolor)
        self.f1.config(bg=self.backgroundcolor)
        self.f2.config(bg=self.backgroundcolor)
        self.f3.config(bg=self.backgroundcolor)
        self.label.config(bg=self.backgroundcolor)
        self.rightframe.config(bg=self.backgroundcolor)
        self.labelstart.config(bg=self.backgroundcolor)
        self.butstart.config(bg=self.backgroundcolor)
        try:
            self.showlabel.config(bg=self.backgroundcolor)
        except:
            pass
        

    def TF(self, T:int, F:int, timec:str, backgroundcolor:str, allow_1:list, allow_2:list,askcallmusic:bool, mode:tuple):
        '''需要提供self,正确T，错误F，时间timec,模式mode,以及背景颜色backgroundcolor'''
        "显示结果"
        self.allow_1 = allow_1
        self.allow_2 = allow_2
        self.T = T
        self.F = F
        self.mode = mode
        self.timec = timec
        self.backgroundcolor = backgroundcolor
        self.tkt = Toplevel()
        self.tkt.title("结果")
        self.tkt.iconbitmap("favicon.ico")
        self.tkt.geometry("400x440")
        self.tkt.iconbitmap("favicon.ico")
        self.tkt.resizable(0,0)
        self.tkt_frame = Frame(self.tkt,bg=self.backgroundcolor)
        self.tkt_frame.pack(fill=BOTH)
        self.st = Label(self.tkt_frame,bg=backgroundcolor,text="正确题数："+str(self.T),font=("Times",14)).pack(pady=5)
        self.sf = Label(self.tkt_frame,bg=backgroundcolor,text="错误题数："+str(self.F),font=("Times",14)).pack(pady=5)
        self.get_usetime()
        Label(self.tkt_frame,bg=self.backgroundcolor,text="做题时间:"+"  "+self.timec,font=("Times",14)).pack(pady=5)

        try:
            from PIL import Image, ImageTk
        except ModuleNotFoundError as e:
            tkinter.messagebox.showerror("错误", "所依赖的库未找到!")
            
        if self.T == 15:
            self.pp = "excellent"
            self.p = self.pp+r".jpg"
        elif self.T >= 13 and self.T < 15:
            self.pp = "good"
            self.p = self.pp+r"png"
        elif self.T < 13 and self.T >= 8:
            self.pp = "notbad"
            self.p = self.pp+r".jpg"
        else:
            self.pp = "fail"
            self.p = self.pp + r".jpg"
            
        if askcallmusic:
            self.sound_path = ".\\sound_or_show\\" + self.pp + r".vbs"
            try:
                os.popen(self.sound_path)
            except Exception as e:
                print("无法播放音乐:"+str(e))
                log("无法播放音乐"+str(e),types="warning")
        else:
            print("不播放音乐")
        
        self.p_path = r"image/" + self.p
        try:
            self.image = Image.open(self.p_path)
            self.p_image = ImageTk.PhotoImage(image=self.image)
            Label(self.tkt_frame, image=self.p_image).pack(side=BOTTOM, pady=40)
        except Exception as e:
            #句柄错误
            log("无法显示图片"+str(e))
            
        self.nowtime = time.strftime(r"%Y-%m-%d:%H:%M:%S")
        self.stf = str(self.nowtime) + ";" + str(self.T) + ";" + str(self.F) + ";" + str(self.timec) + ";" + str(self.mode) + ";" + str(self.allow_1) + str(self.allow_2)
        self.a = open("storage/exam_list.txt",'a')
        self.a.write(self.stf + "\n")
        self.a.close()
        
        

    def open_exam_list(self):
        "打开做题记录"
        try:
            self.efile = open("storage/exam_list.txt", 'r')
            self.raw_data = self.efile.readlines()
            self.co = ["times", "rightexam", "wrongexam", "usetime", "plrange", "munumber"]
            times = []
            rightexam = []
            wrongexam = []
            usetime = []
            plrange = []
            munumber = []
            self.exam_data = [times, rightexam, wrongexam, usetime, plrange, munumber]  #解码后的文件(列表形式)
            self.show = Toplevel()
            self.show.iconbitmap("favicon.ico")
            self.show.title("记录")
            self.show.geometry("650x550")
            
            self.column = ("时间","正确题数","错误题数","用时","选用加减数范围","乘数选择")
            self.treeview = ttk.Treeview(self.show,show="headings",columns=self.column,padding=1)
            self.treeview.pack(side=LEFT, fill=BOTH, expand=YES)
            self.treeview.column(self.column[0], width=140, anchor=CENTER)
            self.treeview.column(self.column[1], width=60, anchor=CENTER)
            self.treeview.column(self.column[2], width=60, anchor=CENTER)
            self.treeview.column(self.column[3], width=80, anchor=CENTER)
            self.treeview.column(self.column[4], width=100, anchor=CENTER)
            self.treeview.column(self.column[5], width=210, anchor=CENTER)
            
            for i in range(0, len(self.column)):
                self.treeview.heading(self.column[i], text=self.column[i])
            for line in self.raw_data:
                line = line.strip()
                self.new_data = line.split(sep=";")
                times = self.new_data[0]
                rightexam = self.new_data[1]
                wrongexam = self.new_data[2]
                usetime = self.new_data[3]
                plrange = self.new_data[4]
                munumber = self.new_data[5]
                self.exam_data = [times, rightexam, wrongexam, usetime, plrange, munumber]
                self.treeview.insert('',"end",value=self.exam_data)
                           
        except IOError:
            self.answer = tkinter.messagebox.showwarning("提示","记录被删除，是否重建？")
            if self.answer == 1:
                self.file = open("storage/exam_list.txt",'w')
                self.file.write("")
                self.file.close()

    def open_exam_list2(self):
        "打开做题记录"
        try:
            self.file = open("storage/exam_list.txt",'r')
            self.show = Tk()
            self.show.iconbitmap("favicon.ico")
            self.show.title("记录")
            self.show.geometry("500x500")
            self.text = Text(self.show,pady=5)
            
            self.scroll = Scrollbar(self.show)
            self.scroll.pack(side=RIGHT,fill=Y)
            self.text.pack(side=LEFT,fill=BOTH,expand=YES)
            self.scroll.config(command=self.text.yview)
            self.text.config(yscrollcommand=self.scroll.set)
            self.a = self.file.readlines()
            self.e = ""
            for x in self.a:
                self.e.join(str(x))
                self.text.insert(1.0,x)
                
        except IOError:
            self.answer = tkinter.messagebox.showwarning("提示","记录被删除，是否重建？")
            if self.answer == 1:
                self.file = open("storage/exam_list.txt",'w')
                self.file.write("")
                self.file.close()
    


   