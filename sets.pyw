from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import tkinter.colorchooser
import functions



class Sets():
    def __init__(self):
        '''Warning: don't allow you to create a new object!'''
        self.data = self.read_json(use=False)
        return self.data
    
    def main(self):
        print(self.data)
        self.toptk = Tk()
        self.toptk.iconbitmap("favicon.ico")
        self.toptk.title("设置")
        self.toptk.geometry('380x400')
        self.toptk.resizable(0,0)
        self.notebook = ttk.Notebook(self.toptk)
        self.top = Frame(self.toptk)
        self.top.pack(fill=BOTH, expand=YES)
        self.bglabel = Label(self.top, text='背景颜色', bg=self.data["bg"],relief=SUNKEN,bd=0.5)
        self.bglabel.grid(row=0,pady=10,padx=10)
        ttk.Button(self.top, text='选择颜色', command=lambda:self.open_color("bg")).grid(row=0,column=1)
        self.wrongbglabel = Label(self.top, text="错误颜色", bg=self.data["wrongbg"],relief=SUNKEN,bd=0.5)
        self.wrongbglabel.grid(row=1)
        ttk.Button(self.top, text="选择颜色", command=lambda :self.open_color("wrongbg")).grid(row=1, column=1)
        self.spellbglabel = Label(self.top,text='输入字符颜色',bg=self.data["spellbg"],relief=SUNKEN,bd=0.5)
        self.spellbglabel.grid(row=2,pady=10,padx=10)
        ttk.Button(self.top, text="选择颜色", command=lambda: self.open_color("spellbg")).grid(row=2, column=1)
        self.leftframecolorlabel = Label(self.top, text="左栏背景颜色", bg=self.data["leftframecolor"], relief=SUNKEN, bd=0.5)
        self.leftframecolorlabel.grid(row=3, pady=10, padx=10)
        ttk.Button(self.top, text="选择颜色", command=lambda: self.open_color("leftframecolor")).grid(row=3, column=1)
        ttk.Button(self.top, text="确认", command=self.submit).place(x=130,y=300)
        
        self.top2 = Frame(self.toptk)
        self.fontlabel = Label(self.top2, text='布局字体',font=(self.data["font"],12))
        self.fontlabel.grid(row=0, padx=5, pady=5)
        ttk.Button(self.top2, text='选择', command= lambda: self.open_font("font")).grid(row=0, column=1, padx=5, pady=5)
        self.spellfontlabel = Label(self.top2, text="输入字体", font=(self.data["spellfont"], 12))
        self.spellfontlabel.grid(row=1)
        ttk.Button(self.top2, text='选择', command=lambda:self.open_font("spellfont")).grid(row=1, column=1, padx=5, pady=5)
        self.titlefontlabel = Label(self.top2, text="大字字体", font=(self.data["titlefont"], 12))
        self.titlefontlabel.grid(row=2)
        ttk.Button(self.top2, text='选择', command=lambda:self.open_font("titlefont")).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.top2, text="确认", command=self.submit).place(x=130,y=300)
        

        self.top3 = Frame(self.toptk)
        self.top3.pack(padx=10,pady=10)
        self.yesno = BooleanVar(self.toptk)
        self.startyesno = BooleanVar(self.toptk)
        self.yesno.set(bool(self.data["askcallmusic"]))
        self.startyesno.set(bool(self.data["startmusic"]))

        self.musicframe = Frame(self.top3)
        self.musicframe.pack(fill=BOTH)
        Label(self.musicframe, text='显示报告后播放声音').grid(row=0,padx=5,pady=5)
        self.Check1 = ttk.Checkbutton(self.musicframe, text='播放',command=self.yesnosound,variable=self.yesno)
        self.Check1.grid(row=0, column=1, padx=5, pady=5)
        Label(self.musicframe, text="开始程序后播放声音").grid(row=1, padx=5, pady=5)
        self.Check2 = ttk.Checkbutton(self.musicframe, text='播放',command=self.yesnosound,variable=self.startyesno)
        self.Check2.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.top3, text="确认", command=self.submit).place(x=130,y=300)
        
        self.styleframe = Frame(self.top3)
        self.styleframe.pack(fill=BOTH,expand=YES)
        self.usestylelabel = Label(self.styleframe, text='使用风格')
        self.usestylelabel.pack(anchor="nw",padx=5,pady=5)
        self.tlistbox = Listbox(self.styleframe,height=11,bd=0) 
        self.tlistbox.pack(anchor="nw",side=LEFT,padx=5,pady=5)
        allstyle = ttk.Style()

        for self.item in allstyle.theme_names():
            self.tlistbox.insert(END, self.item)
        self.tlistbox.selection_set(0)
        ttk.Button(self.top3, text="确认", command=self.submit).place(x=130,y=300)
        
        self.notebook.add(self.top, text="颜色")
        self.notebook.add(self.top2, text="字体")
        self.notebook.add(self.top3, text="声音&风格")
        
        self.notebook.pack(fill=BOTH,expand=YES)
        self.toptk.mainloop()
    
if __name__ == "__main__":
    a = Sets()
    a.main()
