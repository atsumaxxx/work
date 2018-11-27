# グローバル変数
nikkei_heikin = ""

# インポート
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

# 無限ループ
while True:

    # 指定周期待機させる
    #time.sleep(60)
    time.sleep(2)

    # ファイルオープン
    f = open("nikkei_heikin.csv","a")
    writer = csv.writer(f, lineterminator="\n")
    csv_list = []

    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    csv_list.append(time_)
    
    # htmlセット
    url = "https://www.nikkei.com/"
    html = requests.get(url)

    # パーサーオブジェクト
    soup = BeautifulSoup(html.text,"html.parser")

    # html要素取得
    span = soup.find_all("span")

    for tag in span:
        try:
            string_ = tag.get("class").pop(0)
            #print(string_)

            if string_ in "m-miH01C_rate":
                nikkei_heikin = tag.string
                break
        except:
            pass

    print("日経平均 = " + nikkei_heikin + "円")
    csv_list.append(nikkei_heikin)
    writer.writerow(csv_list)
    
    f.close()
    
