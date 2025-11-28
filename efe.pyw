from tkinter import *
from random import randint, choice
from time import process_time as CLOCK
import pickle
import tkinter.messagebox
import tkinter.font
import time
first_time = CLOCK()
import functions
try:
    
    from functions import log
    from functions import LOAD
    from functions import DUMP
    from functions import catch_error
    import functions
    import sets
    import tkinter.ttk as ttk
    #from PIL import Image, ImageTk
except (ImportError, ModuleNotFoundError) as e:
    tkinter.messagebox.showwarning(
        "警告", "程序所需要的模块未找到，可能会导致某些功能不可用，请联系作者解决\nError:"+str(e))

log(text="-------------------------")
log(types="times", timea="start")


class Cherror(BaseException):
    '''每天十五道题错误'''
    class Xgeterror(BaseException):
        '''乘数错误'''
        pass

    class Numerror(BaseException):
        '''数字错误'''
        pass


class Choose_difficult(functions.functions):
    def __init__(self):
        '''选择难度'''

        self.pvalue = 50
        self.lvalue = 50
        self.all_checks = False

    @catch_error
    def grid(self):
        '''布局'''
        self.ctk = Tk()
        self.ctk.withdraw()
        self.pvar = IntVar(self.ctk)
        self.lvar = IntVar(self.ctk)

        self.pvar.set(50)
        self.lvar.set(50)
        self.ctk.title("选择难度")
        self.ctk.geometry("450x480")
        self.ctk.iconbitmap("favicon.ico")
        self.ctk.resizable(0, 0)
        self.ctk.wm_attributes("-topmost", 1)
        self.cframe = Frame(self.ctk)
        self.cframe.pack()

        Label(self.cframe, text="选择难度", font=("Arial", 22)).pack(pady=15)
        # 加法
        self.plmframe = ttk.LabelFrame(self.ctk)
        self.plmframe.pack()
        self.pframe = Frame(self.plmframe)  # ctk
        self.pframe.pack(anchor="nw")
        Label(self.pframe, text="加法:", font=("微软雅黑", 11)).pack(
            fill=BOTH, side=LEFT, padx=30, pady=15)
        # orient=HORIZONTAL,length=200
        self.pspin = ttk.Entry(self.pframe, textvariable=self.pvar)
        self.pspin.pack(padx=20, pady=20, fill=BOTH)
        # 减法
        self.lframe = Frame(self.plmframe)
        self.lframe.pack(anchor="nw")
        ttk.Label(self.lframe, text="减法:", font=("微软雅黑", 11)).pack(
            fill=BOTH, side=LEFT, padx=30, pady=15)
        self.lspin = ttk.Entry(self.lframe, textvariable=self.lvar)
        self.lspin.pack(padx=20, pady=20, fill=BOTH)

        self.mframe = Frame(self.plmframe)
        self.mframe.pack(anchor="nw")
        self.m1frame = Frame(self.mframe)
        self.m2frame = Frame(self.mframe)
        self.m1frame.pack()
        self.m2frame.pack(side=LEFT)

        for x in range(1, 10):
            strings = "".join(("self.f", str(x), " = BooleanVar(self.ctk)"))
            exec(strings)
        for x in range(1, 10):
            strings = "".join(("self.s", str(x), " = BooleanVar(self.ctk)"))
            exec(strings)

        self.f1.set(True)
        self.f2.set(True)
        self.f5.set(True)
        self.s1.set(True)
        self.s2.set(True)
        self.s5.set(True)
        self.s6.set(True)
        self.s7.set(True)
        self.s8.set(True)
        self.s9.set(True)

        Label(self.m1frame, text="乘数1:", font=("微软雅黑", 11)).pack(
            fill=BOTH, padx=30, side=LEFT, pady=20)
        Label(self.m2frame, text="乘数2:", font=("微软雅黑", 11)).pack(
            fill=BOTH, side=LEFT, pady=20, padx=30)
        self.all_check = ttk.Checkbutton(
            self.plmframe, text="全选", command=self.all_checkit)
        self.all_check.pack(side=RIGHT, padx=10)

        for x in range(1, 10):
            strings = "".join(("self.checkf", str(x), " =  ttk.Checkbutton(self.m1frame,text=", str(
                x), ",variable=self.f", str(x), ").pack(side=LEFT)"))
            exec(strings)
        for y in range(1, 10):
            strings = "".join(("self.checks", str(y), " = ttk.Checkbutton(self.m2frame,text=", str(
                y), ",variable=self.s", str(y), ").pack(side=LEFT)"))
            exec(strings)

        self.cbutton = ttk.Button(self.ctk, text="确认", command=self.post)
        self.cbutton.pack(pady=15)
        self.cbutton.bind("<Return>", self.post)
        self.ctk.deiconify()
        self.ctk.mainloop()

    def reset(self):
        '''重置数字'''
        self.lvar.set(50)
        self.pvar.set(50)

    def test(self):
        '''测试数字是否符合标准'''
        try:
            assert bool(self.pvar.get()) is True
            assert bool(self.lvar.get()) is True
            int(self.pvar.get())
            int(self.lvar.get())
            self.pvar.get() - 1
            self.lvar.get() - 1
            assert self.lvar.get() > 0 and self.pvar.get() > 0
            assert self.pvar.get() <= 500 and self.lvar.get() <= 500
            assert self.lvar.get() >= 5 and self.pvar.get() >= 5

            yesno = True

        except Exception as e:
            yesno = False
        finally:
            return yesno

    @catch_error
    def all_checkit(self):
        '''乘数全选'''
        strings = False if self.all_checks else True
        self.all_checks = bool(strings)
        for x in range(1, 10):
            exec_strings = "".join(
                ("self.f", str(x), ".set(strings)", ";self.s", str(x), ".set(strings)"))
            exec(exec_strings)

    def xget(self):
        '''获得乘数'''

        self.allow_1 = []
        self.allow_2 = []
        for i, item in enumerate(["self.f1", "self.f2", "self.f3", "self.f4", "self.f5", "self.f6", "self.f7", "self.f8", "self.f9"]):
            self.items = eval(item).get()
            if self.items:
                self.allow_1.append(i+1)
        for i, item in enumerate(["self.s1", "self.s2", "self.s3", "self.s4", "self.s5", "self.s6", "self.s7", "self.s8", "self.s9"]):
            self.items = eval(item).get()
            if self.items:
                self.allow_2.append(i + 1)

        strings = bool(self.allow_1 != [] and self.allow_2 != [])
        if strings is False:
            raise Cherror.Xgeterror()

    @catch_error
    def pget(self, value=""):
        """设置最大数字加法"""
        self.pvalue = float(self.pspin.get())

    @catch_error
    def lget(self, value=""):
        """设置最大数字减法"""
        self.lvalue = float(self.lspin.get())

    def post(self):
        '''提交数据'''

        try:
            if not self.test():
                raise Cherror.Numerror()
            self.xget()
        except Cherror.Numerror:
            tkinter.messagebox.showwarning("警告", "数字错误!")
            return
        except Cherror.Xgeterror:
            tkinter.messagebox.showwarning("警告", "乘数有误!")
            return

        self.pget()
        self.lget()
        self.ctk.withdraw()

        print(self.pvalue, self.lvalue)

        E = Everyday()
        E.main_efe(int(self.pvalue), int(self.lvalue),
                   self.allow_1, self.allow_2)


class Everyday(functions.functions):
    def __init__(self, *args, **kwrd):
        '''初始化主程序'''
        functions.functions.__init__(self)
        self.data = sets.Sets.__init__(self)

        self.cancallmusic = self.data["askcallmusic"]
        self.backgroundcolor = self.data["bg"]
        self.textwrongcolor = "red"
        self.leftframecolor = self.data["leftframecolor"]
        self.time_stop = False
        self.willdo_again = False
        self.tkexit = False

    @catch_error
    def main_efe(self, max_1, max_2, allow_1, allow_2):
        """主函数"""

        print("获取的加数最大值:{max1},减数最大值:{max2}".format(max1=max_1, max2=max_2))
        self.plus_max = max_1
        self.minus_max = max_2
        self.mode = (self.plus_max, self.minus_max)
        self.tk = Tk()
        self.tk.title("每天十五道题")
        self.tk.withdraw()
        self.tk.iconbitmap("favicon.ico")
        self.tk.geometry("800x320")
        self.tk.resizable(1, 0)
        self.tk.protocol("WM_DELETE_WINDOW", self.efeexit)
        #self.windowstyle = ttk.Style(self.tk)#
        #self.windowstyle.theme_use(self.data["style"])
        self.leftframe = Frame(
            self.tk, width=400, bg=self.data["leftframecolor"], height=300)
        self.leftframe.pack(side=LEFT, fill=BOTH)
        self.frame = Frame(self.tk, height=650, width=750,
                           bg=self.backgroundcolor)
        self.frame.pack(fill=BOTH, expand=YES)

        self.startending = False
        self.labelstart = Label(self.frame, bg=self.backgroundcolor,
                                text="每天十五道题", pady=38, font=(self.data["titlefont"], 40))
        self.labelstart.pack()
        self.butstart = Button(self.frame, pady=35, padx=35, text="开始",
                               bg=self.backgroundcolor, command=self.startend)
        self.butstart.pack(pady=10)
        self.butstart.bind("<Return>", self.startend)
        # 对窗口的编辑
        self.relpy = []
        self.money = StringVar(self.tk)
        self.name = StringVar(self.tk)
        self.level = StringVar(self.tk)
        self.time_var = StringVar(self.tk)
        # 把菜单组件写上
        self.m = Menu(self.frame)
        self.fm = Menu(self.m, tearoff=0)
        self.fm.add_command(label="版本", command=self.help_html)
        self.fm.add_command(
            label="打赏", command=lambda: functions.functions.give_money(self))
        self.fm.add_command(label='''关于"每天十五道题"''', command=start)
        self.fm.add_cascade(label="设置", command=self.use_sets)
        self.fm.add_separator()
        self.fm.add_command(label="退出", command=self.efeexit)
        self.m.add_cascade(label="程序", menu=self.fm)

        self.em = Menu(self.m, tearoff=0)
        self.m.add_cascade(label="功能", menu=self.em)
        self.em.add_command(
            label="清空信息", command=lambda: functions.functions.clean(self))
        self.em.add_command(label="打开做题记录", command=lambda: functions.functions.open_exam_list(
            self))  # functions.open_exam_list

        self.mm = Menu(self.m, tearoff=0)
        self.m.add_cascade(label="解锁功能", menu=self.mm)
        self.mm.add_command(
            label="小本子", command=lambda: functions.functions.easy_text(self))
        self.mm.add_command(label="辅助画图", command=functions.mycanvas)
        self.mm.add_command(
            label="打印当前题目", command=lambda: functions.functions.print_exam(self))

        self.exm = Menu(self.m, tearoff=0)
        self.m.add_cascade(label="调试", menu=self.exm)
        self.exm.add_command(
            label="禁止输入框", command=lambda: functions.functions.again(self))
        self.exm.add_command(
            label="打开日志", command=lambda: functions.functions.open_data(self))
        self.exm.add_command(
            label="开发者命令行", command=lambda: functions.help_py())
        self.tk.config(menu=self.m)

        log(text="menu设置成功")
        try:
            with open("config.dat", "rb") as file:
                self.file_data = pickle.load(file)
            self.money_var = self.file_data["money"]
            self.name_var = self.file_data["name"]
        except (TypeError, NameError, AttributeError) as e:
            log("error:"+str(e), types='error')
            log("file_data:"+str(self.file_data), types="error")
            print("第一次打开发生错误:" + str(e))
            functions.repair()
        else:
            log("左窗口栏设置成功!")
        finally:
            with open("config.dat", "rb") as file:
                self.file_data = pickle.load(file)
            self.money_var = self.file_data["money"]
            self.name_var = self.file_data["name"]
            self.money.set("金币:"+str(self.money_var))
            self.name.set("你的名字:"+str(self.name_var))
            self.btstyle = ttk.Style()
            self.btstyle.configure("BW.TButton",)
            self.name_label = Label(
                self.leftframe, textvariable=self.name, bg=self.data["leftframecolor"], font=("微软雅黑", 9))
            self.name_label.pack(padx=20)
            self.money_label = Label(
                self.leftframe, textvariable=self.money, bg=self.data["leftframecolor"], font=("微软雅黑", 9))
            self.money_label.pack(padx=20)

            self.name_button = ttk.Button(
                self.leftframe, text="修改名称", command=self.change_name)
            self.name_button.pack(padx=20)

        self.shop_button = ttk.Button(
            self.leftframe, text="商店", command=self.shop_command)
        self.shop_button.pack(padx=20)

        '''定义文字'''

        self.label = Label(self.frame, bg=self.backgroundcolor, text="题目数量：15")
        self.label.pack(anchor="nw", pady=5)
        self.sizegrip = ttk.Sizegrip(self.frame)
        self.sizegrip.pack(anchor="se", side=RIGHT)
        self.allow_1 = allow_1
        self.allow_2 = allow_2

        self.pack_exams()
        self.right_pack()
        print("允许的乘数1列表:"+str(self.allow_1))
        print("允许的乘数2列表:" + str(self.allow_2))

    @catch_error
    def use_sets(self):
        """调用设置"""
        sets.Sets.main(self)

    @catch_error
    def use_style(self, datajson: dict):
        """
        应用风格;
        参数说明:datajson：个性化字典
        """
        print("开始应用")
        functions.functions.use_color(self, datajson)
        if datajson["style"] == "TK":
            pass

        self.cancallmusic = bool(datajson["askcallmusic"])

    def read_json(self, use=True):
        '''
        获取数据
        若指定use=True,自动应用'''

        with open("storage/set.json", "r") as file:
            raw_json = file.read()
            self.json_data = LOAD(raw_json)
            print("得到的数据" + str(self.json_data))
            if use:
                self.use_style(self.json_data)
            return self.json_data

    def bBTK(self):
        '''应用TK'''
        self.data["style"] = "TK"
        self.usestylelabel.config(text="使用风格: TK")

    def bBTTK(self):
        '''应用TTK'''
        self.data["style"] = "TTK"
        self.usestylelabel.config(text="使用风格: TTK")

    def bBSUNKEN(self):
        '''应用SUNKEN'''
        tkinter.messagebox.showinfo("注意", "暂不支持")

    def submit(self):
        ''''提交数据'''
        print("提交的数据"+str(self.data))
        if tkinter.messagebox.askyesno("确认", "确认修改?"):
            with open("storage/set.json", "w") as file:
                self.data["style"] = self.tlistbox.get(
                    self.tlistbox.curselection())
                file.write(functions.DUMP(self.data))
            self.toptk.destroy()
        self.read_json()

    @catch_error
    def time_change(self):
        # 不断获取用户用时
        while 1:
            if self.time_stop:
                continue
            if self.startending:
                try:
                    self.timec = self.get_usetime()
                    self.showtimestrings = "".join(("用时:", self.timec))
                    self.time_var.set(self.showtimestrings)
                    self.time_label.config(text=self.showtimestrings)
                except TclError:
                    pass
            if self.willdo_again:
                print(self.timec)
            if self.tkexit:
                raise RuntimeError
            time.sleep(0.1)

    @catch_error
    def mainloop(self):
        '''主循环'''
        import threading
        #self.tkthread = threading.Thread(target=self.tk.update)
        # self.tkthread.start()
        self.timethread = threading.Thread(target=self.time_change)
        self.timethread.setDaemon(1)
        self.timethread.start()
        self.tk.mainloop()

    @catch_error
    def open_color(self, way="bg"):
        '''
        选择颜色
        参数way:bg,wrongbg,spellbg,leftframecolor
        '''
        self.color = tkinter.colorchooser.askcolor(
            title="选择颜色", color="lightgreen")
        if self.color[-1] is None:
            tkinter.messagebox.showwarning("警告", "未选择任何颜色!")
            return

        self.data[way] = self.color[-1]
        print("选择的颜色" + str(self.color[-1]))
        strings = "".join(("self.", way, "label.config(bg=self.color[1])"))
        exec(strings)

    def yesnosound(self):
        '''获取是否打开声音'''
        self.data["askcallmusic"] = self.yesno.get()

    def __use_font(self, way=""):
        '''
        提交字体
        way:font,spellfont,titlefont
        '''
        try:
            self.forfont = self.listbox.get(self.listbox.curselection())
            self.data[way] = self.forfont
            strings = "".join(
                ("self.", way, "label.config(font=(self.forfont,12))"))
            exec(strings)
            self.ftk.destroy()
        except AssertionError:
            tkinter.messagebox.showwarning("警告", "未选择!")

    def open_font(self, way):
        '''选择字体'''
        self.ftk = Toplevel()
        self.ftk.iconbitmap("favicon.ico")
        self.ftk.title("选择字体")
        self.ftk.resizable(0, 0)
        self.ftk.wm_attributes("-topmost", 1)
        self.ftk.geometry("300x300")
        self.ftk.update()
        Label(self.ftk, text="选择字体", font=("微软雅黑", 12)).pack(pady=10)
        self.scroll = Scrollbar(self.ftk)
        self.scroll.pack(fill=Y, side=RIGHT)
        self.listbox = Listbox(self.ftk, yscrollcommand=self.scroll.set)
        self.listbox.pack(pady=10)
        self.scroll.config(command=self.listbox.yview)
        for font in tkinter.font.families():
            if font.startswith("@"):
                continue
            self.listbox.insert(END, font)
        self.fontbutton = ttk.Button(
            self.ftk, text="确认", command=lambda: self.__use_font(way))
        self.fontbutton.pack()

    @catch_error
    def pack_exams(self, *args, **kwrd):
        '''编写题目'''
        self.true2 = []
        self.right = 0
        self.wrong = 0
        self.true = []
        self.true3 = []
        self.T = 0
        self.F = 0
        self.wrong_list = []
        self.relpy = []
        for x in range(1, 16):
            strings = "".join(("self.var", str(x), " = StringVar(self.tk)"))
            exec(strings)

        self.f1 = Frame(self.frame, bg=self.backgroundcolor)  # 加法
        self.f1.pack(side=LEFT, expand=YES, padx=10, pady=10)

        self.f2 = Frame(self.frame, bg=self.backgroundcolor)  # 减法
        self.f2.pack(side=LEFT, expand=YES, padx=10, pady=10)

        self.f3 = Frame(self.frame, bg=self.backgroundcolor)  # 乘法·
        self.f3.pack(side=LEFT, expand=YES, padx=10, pady=15)

        self.n1 = randint(1, self.plus_max)
        self.n2 = randint(1, self.plus_max)
        while (self.n1 + self.n2 >= self.plus_max):
            self.n1 = randint(1, self.plus_max)
            self.n2 = randint(1, self.plus_max)

        self.label1 = str(self.n1)+"+"+str(self.n2)+"等于多少？"
        self.true.append(self.n1+self.n2)
        self.relpy.append(self.n1+self.n2)
        functions.functions.Set(self)
        self.textl1 = Label(self.f1, bg=self.backgroundcolor, text=self.label1)
        self.textl1.pack(anchor='nw')
        self.entry1 = ttk.Entry(self.f1)
        self.entry1.pack()

        self.n1 = randint(1, self.plus_max)
        self.n2 = randint(1, self.plus_max)
        while (self.n1 + self.n2 >= self.plus_max):
            self.n1 = randint(1, self.plus_max)
            self.n2 = randint(1, self.plus_max)
        self.label2 = str(self.n1)+"+"+str(self.n2)+"等于多少？"
        self.true.append(self.n1+self.n2)
        self.relpy.append(self.n1+self.n2)
        functions.functions.Set(self)
        self.textl2 = Label(self.f1, bg=self.backgroundcolor, text=self.label2)
        self.textl2.pack(anchor='nw')
        self.entry2 = ttk.Entry(self.f1)
        self.entry2.pack()

        self.n1 = randint(1, self.plus_max)
        self.n2 = randint(1, self.plus_max)
        while (self.n1 + self.n2 >= self.plus_max) == True:
            self.n1 = randint(1, self.plus_max)
            self.n2 = randint(1, self.plus_max)
        self.label3 = str(self.n1)+"+"+str(self.n2)+"等于多少？"
        self.true.append(self.n1+self.n2)
        self.relpy.append(self.n1+self.n2)
        functions.functions.Set(self)
        self.textl3 = Label(self.f1, bg=self.backgroundcolor, text=self.label3)
        self.textl3.pack(anchor='nw')
        self.entry3 = ttk.Entry(self.f1)
        self.entry3.pack()

        self.n1 = randint(1, self.plus_max)
        self.n2 = randint(1, self.plus_max)
        while (self.n1 + self.n2 >= self.plus_max) == True:
            self.n1 = randint(1, self.plus_max)
            self.n2 = randint(1, self.plus_max)
        self.label4 = str(self.n1)+"+"+str(self.n2)+"等于多少？"
        self.true.append(self.n1+self.n2)
        self.relpy.append(self.n1+self.n2)
        functions.functions.Set(self)
        self.textl4 = Label(self.f1, bg=self.backgroundcolor, text=self.label4)
        self.textl4.pack(anchor='nw')
        self.entry4 = ttk.Entry(self.f1)
        self.entry4.pack()

        self.n1 = randint(1, self.plus_max)
        self.n2 = randint(1, self.plus_max)
        while (self.n1 + self.n2 >= self.plus_max) == True:
            self.n1 = randint(1, self.plus_max)
            self.n2 = randint(1, self.plus_max)
        while True:
            if self.n2 >= self.n1:
                self.n1 = randint(5, 14)
                self.n2 = randint(6, 14)
            else:
                break

        self.label5 = str(self.n1)+"+"+str(self.n2)+"等于多少？"
        self.true.append(self.n1+self.n2)
        self.relpy.append(self.n1+self.n2)
        functions.functions.Set(self)
        self.textl5 = Label(self.f1, bg=self.backgroundcolor, text=self.label5)
        self.textl5.pack(anchor='nw')
        self.entry5 = ttk.Entry(self.f1)
        self.entry5.pack()

        self.n1 = randint(1, self.minus_max)
        self.n2 = randint(1, self.n1)
        while self.n1 == self.n2 or self.n1 < self.n2:
            self.n1 = randint(1, self.minus_max)
            self.n2 = randint(1, self.minus_max)
        while True:
            if self.n2 >= self.n1:
                self.n1 = randint(1, self.minus_max)
                self.n2 = randint(1, self.minus_max)
            else:
                break
        self.label6 = str(self.n1)+"-"+str(self.n2)+"等于多少？"
        functions.functions.Set(self)
        self.true2.append(self.n1-self.n2)
        self.relpy.append(self.n1-self.n2)
        self.textl6 = Label(self.f2, bg=self.backgroundcolor, text=self.label6)
        self.textl6.pack(anchor='nw')
        self.entry6 = ttk.Entry(self.f2)
        self.entry6.pack()

        self.n1 = randint(1, self.minus_max)
        self.n2 = randint(1, self.n1)
        while self.n1 == self.n2 or self.n1 < self.n2:
            self.n1 = randint(1, self.minus_max)
            self.n2 = randint(1, self.minus_max)
        while True:
            if self.n2 >= self.n1:
                self.n1 = randint(1, self.minus_max)
                self.n2 = randint(1, self.minus_max)
            else:
                break
        self.label7 = str(self.n1)+"-"+str(self.n2)+"等于多少？"
        functions.functions.Set(self)
        self.true2.append(self.n1-self.n2)
        self.relpy.append(self.n1-self.n2)
        self.textl7 = Label(self.f2, bg=self.backgroundcolor, text=self.label7)
        self.textl7.pack(anchor='nw')
        self.entry7 = ttk.Entry(self.f2)
        self.entry7.pack()

        self.n1 = randint(1, self.minus_max)
        self.n2 = randint(1, self.n1)
        while self.n1 == self.n2 or self.n1 < self.n2:
            self.n1 = randint(1, self.minus_max)
            self.n2 = randint(1, self.minus_max)
        while True:
            if self.n2 >= self.n1:
                self.n1 = randint(1, self.minus_max)
                self.n2 = randint(1, self.minus_max)
            else:
                break

        self.label8 = str(self.n1)+"-"+str(self.n2)+"等于多少？"
        functions.functions.Set(self)
        self.true2.append(self.n1-self.n2)
        self.relpy.append(self.n1-self.n2)
        self.textl8 = Label(self.f2, bg=self.backgroundcolor, text=self.label8)
        self.textl8.pack(anchor='nw')
        self.entry8 = ttk.Entry(self.f2)
        self.entry8.pack()

        self.n1 = randint(1, self.minus_max)
        self.n2 = randint(1, self.n1)
        while self.n1 == self.n2 or self.n1 < self.n2:
            self.n1 = randint(1, self.minus_max)
            self.n2 = randint(1, self.minus_max)
        while True:
            if self.n2 >= self.n1:
                self.n1 = randint(1, self.minus_max)
                self.n2 = randint(1, self.minus_max)
            else:
                break
        self.label9 = str(self.n1)+"-"+str(self.n2)+"等于多少？"
        functions.functions.Set(self)
        self.true2.append(self.n1-self.n2)
        self.relpy.append(self.n1-self.n2)
        self.textl9 = Label(self.f2, bg=self.backgroundcolor, text=self.label9)
        self.textl9.pack(anchor='nw')
        self.entry9 = ttk.Entry(self.f2)
        self.entry9.pack()

        self.n1 = randint(1, self.minus_max)
        self.n2 = randint(1, self.n1)
        while self.n1 == self.n2 or self.n1 < self.n2:
            self.n1 = randint(1, self.minus_max)
            self.n2 = randint(1, self.minus_max)
        while True:
            if self.n2 >= self.n1:
                self.n1 = randint(1, self.minus_max)
                self.n2 = randint(1, self.minus_max)
            else:
                break
        self.label10 = str(self.n1) + "-" + str(self.n2) + "等于多少？"
        functions.functions.Set(self)
        self.true2.append(self.n1-self.n2)
        self.relpy.append(self.n1-self.n2)
        self.textl10 = Label(
            self.f2, bg=self.backgroundcolor, text=self.label10)
        self.textl10.pack(anchor='nw')
        self.entry10 = ttk.Entry(self.f2)
        self.entry10.pack()

        self.x = choice(self.allow_1)
        self.y = choice(self.allow_2)
        self.label11 = str(self.x)+"x"+str(self.y)+"等于多少？"
        functions.functions.Set(self)
        self.true3.append(self.x * self.y)
        self.relpy.append(self.x * self.y)
        self.textl11 = Label(
            self.f3, bg=self.backgroundcolor, text=self.label11)
        self.textl11.pack(anchor='nw')
        self.entry11 = ttk.Entry(self.f3)
        self.entry11.pack()

        self.x = choice(self.allow_1)
        self.y = choice(self.allow_2)
        self.label12 = str(self.x)+"x"+str(self.y)+"等于多少？"
        functions.functions.Set(self)
        self.true3.append(self.x * self.y)
        self.relpy.append(self.x * self.y)
        self.textl12 = Label(
            self.f3, bg=self.backgroundcolor, text=self.label12)
        self.textl12.pack(anchor='nw')
        self.entry12 = ttk.Entry(self.f3)
        self.entry12.pack()

        self.x = choice(self.allow_1)
        self.y = choice(self.allow_2)
        self.label13 = str(self.x)+"x"+str(self.y)+"等于多少？"
        functions.functions.Set(self)
        self.true3.append(self.x * self.y)
        self.relpy.append(self.x * self.y)
        self.textl13 = Label(
            self.f3, bg=self.backgroundcolor, text=self.label13)
        self.textl13.pack(anchor='nw')
        self.entry13 = ttk.Entry(self.f3)
        self.entry13.pack()

        self.x = choice(self.allow_1)
        self.y = choice(self.allow_2)
        self.label14 = str(self.x)+"x"+str(self.y)+"等于多少？"
        functions.functions.Set(self)
        self.true3.append(self.x * self.y)
        self.relpy.append(self.x * self.y)
        self.textl14 = Label(
            self.f3, bg=self.backgroundcolor, text=self.label14)
        self.textl14.pack(anchor='nw')
        self.entry14 = ttk.Entry(self.f3)
        self.entry14.pack()

        self.x = choice(self.allow_1)
        self.y = choice(self.allow_2)
        self.label15 = str(self.x)+"x"+str(self.y)+"等于多少？"
        functions.functions.Set(self)
        self.true3.append(self.x * self.y)
        self.relpy.append(self.x * self.y)
        self.textl15 = Label(
            self.f3, bg=self.backgroundcolor, text=self.label15)
        self.textl15.pack(anchor='nw')
        self.entry15 = ttk.Entry(self.f3)
        self.entry15.pack()

        print("正确答案"+str(self.relpy))

    @catch_error
    def right_pack(self):
        '''右边的设置'''
        self.rightframe = Frame(self.frame, bg=self.backgroundcolor)
        self.rightframe.pack(side=RIGHT, fill=BOTH,
                             expand=YES, pady=10, padx=30)
        self.button = ttk.Button(
            self.rightframe, text="确定", state=NORMAL, command=self.show)
        self.button.pack(fill=X, side=TOP)
        self.a_button = ttk.Button(
            self.rightframe, text="退出", state=NORMAL, command=self.efeexit)
        self.a_button.pack(fill=X, side=TOP)
        self.again_button = ttk.Button(
            self.rightframe, text="刷新", state=NORMAL, command=lambda: self.do_again(self.f1, self.f2, self.f3))
        self.again_button.pack(fill=X)
        self.time_label = Label(
            self.rightframe, bg=self.backgroundcolor, textvariable=self.time_var)
        self.time_label.pack(side=BOTTOM, anchor="se")

        log("全部设置成功")
        self.tk.deiconify()
        self.mainloop()

    @catch_error
    def efeexit(self):
        '''关闭，退出'''
        if (tkinter.messagebox.askokcancel("确认", "   确认关闭?")):
            self.if_tk_quit()

    def show(self, event=None):
        """展示结果"""
        self.again()
        self.true = str(self.true) + "\n" + str(self.true2) + \
            "\n" + str(self.true3)
        self.showlabel = Label(
            self.rightframe, bg=self.backgroundcolor, text=str(self.true))
        self.showlabel.pack()

        self.EXAM(self.relpy)
        self.button.config(state=DISABLED)
        self.get_usetime()
        self.time_stop = True
        self.TF(T=self.T, F=self.F, timec=self.timec, backgroundcolor=self.backgroundcolor,
                allow_1=self.allow_1, allow_2=self.allow_2, mode=self.mode, askcallmusic=self.cancallmusic)
        self.change_wrong_text_color(self.data["wrongbg"])
        self.money.set("金币:"+str(int(self.money_var)+int(self.T)))
        log("答题获得金钱"+str(self.money.get()))
        self.money_var = int(self.money_var) + self.T

    @catch_error
    def do_again(self, *args):
        '''重新做题'''
        for arg in args:
            arg.destroy()
        try:
            self.showlabel.destroy()
        except AttributeError:
            # 第一次
            pass
        self.tk.withdraw()
        self.clock()
        self.pack_exams(undo=True)

        self.button.config(state=NORMAL)

        self.tk.deiconify()
        self.willdo_again = False
        self.time_stop = False

    @catch_error
    def change_name(self):
        '''改变名字'''
        self.name_frame = Tk()
        self.name_frame.iconbitmap("favicon.ico")
        self.name_frame.title("修改")
        self.name_frame.geometry("200x200")
        Label(self.name_frame, text="原名:"+self.file_data["name"]).pack(pady=10)
        self.name_entry = ttk.Entry(self.name_frame)
        self.name_entry.pack(pady=10)
        self.name_button2 = ttk.Button(
            self.name_frame, text="确定", command=self.len_name)
        self.name_button2.pack(pady=10)

    @catch_error
    def len_name(self):
        '''检查用户所给的名字'''
        if str(self.name_entry.get()) is None:
            tkinter.messagebox.showwarning("注意", "请不要输入空格")
            return
        elif len(str(self.name_entry.get())) > 5:
            tkinter.messagebox.showwarning("注意", "不要超过5个字符")
        else:
            self.file_data["name"] = str(self.name_entry.get())
            self.name_var = str(self.name_entry.get())
            self.name.set("你的名字:"+str(self.name_entry.get()))
            tkinter.messagebox.showinfo("成功", "成功")
            log("修改名字为:" + self.name_var)

    @catch_error
    def if_tk_quit(self):
        '''退出时触发'''
        global first_time
        self.file_data["name"] = self.name_var
        print("名字:"+str(self.name_var))
        print("金币:"+str(self.money_var))
        self.file_data["money"] = self.money_var
        # 备份
        with open("data.dat.bak", 'wb') as bak_file:
            pickle.dump(self.file_data, bak_file)
        with open('config.dat', 'wb') as f:
            pickle.dump(self.file_data, f)
        log(types="times", timea="end")
        end_time = time.time()
        print("运行时间:" + str(end_time - first_time) + "秒")
        self.tkexit = True

        exit()
        

        raise SystemExit

    @catch_error
    def shop_command(self):
        """商店选择"""
        self.shop = Tk()
        self.shop.iconbitmap("favicon.ico")
        self.shop.title("商店")
        self.listbox = Listbox(self.shop, height=11, bd=0)
        self.listbox.pack(padx=25, pady=25)
        self.shopitems = ['小本子 50金币', '简易画图 100金币', '打印题目 250金币', ]
        for self.item in self.shopitems:
            self.listbox.insert(END, self.item)
        self.listbox.selection_set(0)
        self.shop_yes = ttk.Button(self.shop, text='确定', command=self.shop_go)
        self.shop_yes.bind("<Return>", self.shop_go)
        self.shop_yes.pack(pady=10)
        Label(self.shop, text="提示:购买后，重启生效").pack()

    @catch_error
    def shop_go(self):
        '''处理用户所选相'''
        self.select = self.listbox.get(self.listbox.curselection())
        print("选择:"+self.select)
        if self.select == self.shopitems[0]:  # 小本子
            if self.file_data["lock_color_change_color"] == True:
                tkinter.messagebox.showinfo("提示", "您已购买过!")
            elif int(self.money_var) < 50:
                tkinter.messagebox.showerror("警告", "当前金币不够!")
            else:
                self.money_var = str(int(self.money_var) - 50)
                self.file_data["lock_notepad"] = True
                self.file_data["money"] = self.money_var
                print("数据:"+str(self.file_data))
                self.money.set("金币:"+str(self.money_var))
                tkinter.messagebox.showinfo("注意", "成功!")
                log("已买"+self.select)
        elif self.select == self.shopitems[1]:  # 画图
            if self.file_data["lock_draw"] == True:
                tkinter.messagebox.showinfo("提示", "您已购买过!")
            elif int(self.money_var) < 100:
                tkinter.messagebox.showerror("警告", "当前金币不够!")
            else:
                self.money_var = str(int(self.money_var) - 100)
                self.file_data["lock_draw"] = True
                self.file_data["money"] = self.money_var
                print("数据:"+str(self.file_data))
                self.money.set("金币:"+str(self.money_var))
                log("已买"+self.select)
                tkinter.messagebox.showinfo("注意", "成功!")
        elif self.select == self.shopitems[2]:  # 打印题目
            if self.file_data["lock_print_exam"]:
                tkinter.messagebox.showinfo("提示", "您已购买过!")
            elif int(self.money_var) < 250:
                tkinter.messagebox.showerror("警告", "当前金币不够!")
            else:
                self.money_var = str(int(self.money_var) - 250)
                self.file_data["lock_print_exam"] = True
                self.file_data["money"] = self.money_var
                print("数据:"+str(self.file_data))
                self.money.set("金币:"+str(self.money_var))
                log("已买"+self.select)
                tkinter.messagebox.showinfo("注意", "成功!")


def start():
    a = Toplevel()
    a.iconbitmap("favicon.ico")
    a.title("关于每天十道题")
    try:
        v = sys.version
    except Exception:
        v = "Python 3"
    with open("version.ver", "r") as file:
        version = file.read()
    Label(a, text="python版本:" + str(v)).pack()
    Label(a, text="软件版本:" + str(version)).pack()
    Label(a, text="Tk版本:" + str(TkVersion)).pack()
    Label(a, text="每天十道题为广众小朋友出题，是一个很好的软件", font=("微软雅黑", 13)).pack()
    Label(a, text="谢谢大家", font=("微软雅黑", 12)).pack()
    Label(a, text="作者：睿睿", font=("微软雅黑", 11)).pack()
    a.mainloop()


def main():
    '''开启每天十五道题主进程'''
    C = Choose_difficult()
    C.grid()

##########################start############################


if __name__ == "__main__":
    main()
