import sys
import tkinter as tk
import tqdm
import time
from tkinter import StringVar

####################################
##  ウィンドウ設定
####################################
# Create main window
frm = tk.Tk()

# Change window size
frm.geometry('425x600')

# Change window title
frm.title("作業リスト")

####################################
##  グローバル変数
####################################
hLabel = []        #ラベルのハンドルを格納
hCheck = []        #チェックボックスのハンドルを格納
CheckVal = []      #チェックボックスにチェックが入っているかどうかを格納
hPjName = ['PJ1','PJ2','PJ3','PJ4','PJ5','その他']       #プロジェクト名を格納
CheckTrue = []     #チェックボックスにチェックが入っているものを格納
element_array = [] #リストボックスに表示する文字列を格納
PJ_array = []
TASK_array = []
TASKNM_array = []

####################################
##  関数
####################################
#
# チェックボックスのチェック状況を取得する
#
def check(event):
    for n in range(len(CheckVal)):
        if CheckVal[n].get() == True:
            label = tk.Label(text=u"チェックされています")
            label.place(x=130, y=20*n + 40)
            CheckTrue.append(hPjName[n])
        else:
            label = tk.Label(text=u"チェックされていません")
            label.place(x=130, y=20*n + 40)

        #ラベルのハンドルを追加
        hLabel.append(label)


#
# チェックボックスを動的に作成
#
def makeCheckBox():
    #作成するチェックボックスの個数（Entryの値）を取得
    num = 6
    

    #既出のチェックボックスやラベルを削除
    for n in range(len(hCheck)):
        hCheck[n].destroy()
        hLabel[n].destroy()

    #配列を空にする
    del CheckVal[:]
    del hCheck[:]
    del hLabel[:]

    #Entry1に入力された値分ループ
    for n in range(int(num)):
        #BooleanVarの作成
        bl = tk.BooleanVar()

        #チェックボックスの値を決定
        bl.set(False)

        #チェックボックスの作成
        b = tk.Checkbutton(text = hPjName[n], variable = bl)
        b.place(x=35, y=20*n + 40)

        #チェックボックスの値を，リストに追加
        CheckVal.append(bl)

        #チェックボックスのハンドルをリストに追加
        hCheck.append(b)

#
# ファイルオープン
#
def FileOpen():
    PJ_cnt = 0
    TASK_cnt = 0
    TASKNM_cnt = 0
    f = open('test.txt', 'r')
    # with open('test.txt','r') as f:
    for row in f:
        print(row)
        if row[0:1] == '■':
            for JPName in hPjName:
                if row == '■'+JPName+'\n':
                    PJ_cnt = PJ_cnt + 1
                    PJ_array.append(row)
        if row[0:1] == '・':
            TASKNM_array.append(row)
    f.close()


#
# 文字列チェック
#
def checkString(string, search):
    ret = False
    for n in  CheckTrue:
        if search+CheckTrue[n] == string:
            ret = True

####################################
##  Main
####################################
# Create CheckBox
makeCheckBox()

# FileOpen
FileOpen()

# Edit label
label = tk.Label(frm, text="プロジェクト")
# Display label
label.place(x=35, y=20)

# 検索ボタン
button2 = tk.Button(frm, text=u'検索',width=10)
button2.bind("<Button-1>",check)
button2.place(x=65, y=180)

# 作業名
label1 = tk.Label(frm, text="作業名")
label1.place(x=35, y=230)
Editor1 = tk.Entry(frm, width=50)
Editor1.place(x=35, y=250)

# 作業内容
label2 = tk.Label(frm, text="作業内容")
label2.place(x=35, y=280)
Entry1 = tk.Text(frm, height=10, width=50)
Entry1.place(x=35, y=300)

# 開始日
label3 = tk.Label(frm, text="開始日")
label3.place(x=35, y=450)
Editor3 = tk.Entry(frm, width=10)
Editor3.place(x=105, y=450)

# 終了日
label4 = tk.Label(frm, text="終了日")
label4.place(x=215, y=450)
Editor4 = tk.Entry(frm, width=10)
Editor4.place(x=285, y=450)

# 状態
label3 = tk.Label(frm, text="作業状態")
label3.place(x=35, y=480)
Editor3 = tk.Entry(frm, width=10)
Editor3.place(x=105, y=480)

# 登録ボタン
button3 = tk.Button(frm, text=u'登録',width=10)
button3.bind("<Button-1>",check)
button3.place(x=105, y=530)

# 削除ボタン
button4 = tk.Button(frm, text=u'削除',width=10)
button4.bind("<Button-1>",check)
button4.place(x=215, y=530)

# フレーム作成
f=tk.Frame(master=frm)
# リストボックス
#element_array = ['element_1', 'element_2', 'element_4', 'element_3', 'element_5', 'long_long__element','element_1', 'element_2', 'element_4', 'element_3', 'element_5', 'long_long__element','element_1', 'element_2', 'element_4', 'element_3', 'element_5', 'long_long__element']
val1 = StringVar(value = PJ_array)
listbox = tk.Listbox(f, listvariable=val1,width=20, height=10)
#listbox.place(x=500, y=40)
listbox.grid(row=0, column=0, sticky = 'nsew')
f.place(x=230,y=40)

# スクロールバー
scrollbar = tk.Scrollbar(f, orient='v', command=listbox.yview)
#listbox['yscrollcommand'] = scrollbar.set
listbox.configure(yscrollcommand = scrollbar.set)
scrollbar.grid(row=0, column=3, sticky = 'ns')
#scrollbar.place(x=650, y=20, anchor=tk.N)
#scrollbar.pack(anchor=tk.E, expand=1, fill=tk.Y)



frm.mainloop()

