import pickle as file
from json import dumps as DUMP

money = "0"
name = "小胖子"
data = {
        "money":money,
        "name":name,
        "author":"张帅哥",
        "lock_draw":False,
        "lock_print_exam":False,
        "lock_color_change_color": False,
        "lock_notepad": False
        }
strings = file.dumps(data)
print("执行config.dat")
config = open("config.dat",'wb')
config.write(strings)
config.close()

set_data = {
    "bg": "#90ee90",
    "font": "\u9ed1\u4f53",
    "askcallmusic": False,
    "style": "vista",
    "wrongbg": "#ff0000",
    "startmusic": None,
    "spellbg": "",
    "spellfont": "Arial",
    "leftframecolor": "#9296A7",
    "titlefont": "\u7b49\u7ebf Light"
    
}
print("执行set.json")

with open("storage/set.json",'w') as sfile:
    sfile.write(DUMP(set_data))

print("执行完毕!")
print("按任意键退出--")

input()
