import requests  # 请求网页数据
from bs4 import BeautifulSoup  # 美味汤解析数据
import pandas as pd
import time
from tqdm import trange  # 获取爬取速度
import json
import pymongo


def get_bilibili_coment(url_list):
    client = pymongo.MongoClient('47.116.72.249',
                                 27017)

    db = client['bilibili']  # 连接的数据库

    collection = db['comment2']  # 连接的表

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.80 Safari/537.36",
        "cookie": "_uuid=C3150A71-BDA5-49A3-0537-6175EDC2F39620188infoc; "
                  "buvid3=6DB8775C-6684-4FA0-A3DD-64E10BBCD95A70393infoc; rpdid=|(J~JYku||~m0J'ulmllku|Jl; "
                  "LIVE_BUVID=AUTO1115959329782941; sid=8x23ndag; CURRENT_QUALITY=80; blackside_state=1; "
                  "CURRENT_FNVAL=80; bsource=search_baidu; PVID=1; DedeUserID=6499941; "
                  "DedeUserID__ckMd5=c344150befb518ea; SESSDATA=0cf60f14%2C1618744325%2C02501*a1; "
                  "bili_jct=8dd60705de0b6072539fa682afc25d70; bfe_id=1bad38f44e358ca77469025e0405c4a6"  # Headers中copy即可
    }

    # file = open("bilibili_danmu.txt", 'w')
    for item in url_list:
        base_url = item[0]
        movieNamae = item[1]
        print(base_url)
        print(movieNamae)
        for i in trange(1, 101):
            url = base_url + f"&pn={i}"
            response = requests.get(url, headers=headers)
            response.encoding = 'utf-8'
            # soup = BeautifulSoup(response.text, features="lxml")
            data = json.loads(response.content.decode())['data']['replies']
            print(data[0]['content']['message'])
            for item in data:
                # file.write(item['content']['message'])
                data_ = item['content']['message']
                print(str(data_))
                collection.insert_one({"comment": str(data_), "movie": movieNamae})
                # file.write(str(data_))


if __name__ == "__main__":
    url_list = [["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=68400556", "肖申克的救赎"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=93198003", "霸王别姬"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=31270285", "阿甘正传"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=71360198", "盗梦空间"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=70665722", "星际穿越"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=32173331", "楚门的世界"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=79682481", "三傻大闹宝莱坞"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=28428625",  "放牛班的春天"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=78049441", "无间道"],
                ["https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&oid=40452040", "教父"],
                ]


    url = "https://api.bilibili.com/x/v2/reply?&type=1&jsonp=jsonp&pn=6&oid=68400556"
    get_bilibili_coment(url_list)
    print("弹幕爬取完成")
