import sys
import pickle
import time

def out(text=""):
    print(text)

out("准备工作中...")
with open("config.dat",'rb') as filea:
    file = pickle.load(filea)
with open("version.ver","r") as verfile:
    version = verfile.read()
def help_method():
    out("可用方法：")
    out("  ")
    out("————————————")

    for key in file:
        out("命令:"+key)
        
    out("命令:version")
    out("命令:exit")
    out("命令:print_log")
    out("命令:help")


help_method()
while 1:
    a = input("输入指令>>>")
    if a == "version":
        out("版本号"+str(version))
        out()
    elif a == "money":
        out("当前金币:"+str(file["money"]))
    elif a == "name":
        out("用户名称:"+str(file["name"]))
    elif a == "author":
        out("作者:"+str(file["author"]))
    elif a == "lock_draw":
        out(file["lock_draw"])
    elif a == "lock_print_exam":
        out(file["lock_print_exam"])
    elif a == "lock_color_change_color":
        out(file["lock_color_change_color"])
    elif a == "lock_notepad":
        out(file["lock_notepad"])
        
    elif a == "print_log":
        answer = input("确定?(y/n) 或 (exit)")
        if answer == "y" or answer == "yes":
            with open("storage/data.log",'r') as file_log:
                out(file_log.read())
        else:
            out("已取消")

    elif a == "":
        out("")
    else:
        out("命令不存在！")
        
    if a == "exit":
        out("保存修改中...")
        time.sleep(1)
        break
