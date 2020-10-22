import pymongo
import pandas as pd
from EmotionAnalyser.langconv import *


def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line)
    #line = line.encode('utf-8')
    return line


client = pymongo.MongoClient('47.116.72.249',
                             27017)  # 创建连接，因为用的本机的mongodb数据库，所以直接写localhost即可，也可以写成127.0.0.1，27017为端口

db = client['bilibili']  # 连接的数据库

collection = db['comment']  # 连接的表

data = pd.DataFrame(list(collection.find()))
data = data["comment"]

with open('../BilibiliSpider/bilibili_comment.txt', 'wb') as f:
    for item in data:
        #f.write(bytes("-------------"+ "\n" + tradition2simple(item) + "\n", encoding = 'utf-8') )
        f.write(bytes("\n" + tradition2simple(item), encoding = 'utf-8') )
        #f.write('\r\n')
        print(item)
print(data)
