from tkinter import *
import random
import time

class MyCanvas():
    def __init__(self):
        '''This is my Canvas'''
        self.tk = Tk()
        self.tk.title("画图")
        self.Done = 0
        self.canvas = Canvas(self.tk,bg="white",height=500,width=500)
        self.canvas.pack()
        self.canvas.bind('<ButtonRelease-1>',self.Draw)      
        self.canvas.bind('<Button-2>',self.Exit)      # 绑定事件到中键
        self.canvas.bind('<Button-3>',self.Del)       # 绑定事件到右键
        self.canvas.bind_all('<Delete>',self.Del)      # 绑定事件到Delete键
        self.canvas.bind_all('<KeyPress-d>',self.Del)      # 绑定事件到d键
        self.menu = Menu(self.tk)
        self.m = Menu(self.menu,tearoff=1)
        self.m.add_command(label="清空",command=self.Del)
        self.m.add_command(label="退出",command=self.Exit)
        self.menu.add_cascade(label="程序",menu=self.m)
        self.tk.config(menu=self.menu)
        self.tk.mainloop()
        
    def Draw(self,event=None):
        if self.Done == 0:
            self.canvas.create_line(event.x,event.y,event.x + 2,event.y + 2)
            self.x1 = event.x
            self.y1 = event.y
            self.Done += 1
        else:
            self.canvas.create_line(self.x1,self.y1,event.x,event.y)
            del self.x1
            del self.y1
            self.Done = 0
            
        
    def Exit(self,event=None):
        exit()
        quit()
        
    def Del(self,event=None):
        self.items = self.canvas.find_all()
        for item in self.items:
            self.canvas.delete(item)


mycanvas = MyCanvas()
    
