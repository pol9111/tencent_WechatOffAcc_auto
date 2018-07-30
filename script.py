import json
import pymongo
import re
from config import *

def response(flow):
    global like_num, title, pub_time, read_num, comment_num
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    table = db[MONGO_COLLECTION]

    # 获取微信广告json文件, 里面有阅读数和点赞数
    url_msg = 'mp.weixin.qq.com/mp/getappmsgext?'
    if url_msg in flow.request.url:
        text_msg = flow.response.text
        data_py = json.loads(text_msg)
        content = data_py.get('appmsgstat')
        like_num = content.get('like_num')
        read_num = content.get('read_num')
        comment_num = data_py.get('comment_count')

    # 获取文章响应文件, 并匹配标题和发布时间
    url_article = 'mp.weixin.qq.com/s?'
    if url_article in flow.request.url:
        text_arti = flow.response.text
        pub_time = re.findall(r'publish_time.*"(\d+-\d+-\d+)".*', text_arti)[0]
        title = re.findall(r'msg_title\s=\s"(.*?)";', text_arti)[0]

    data = {
        '文章标题': title,
        '发布时间': pub_time,
        '阅读数': read_num,
        '点赞数': like_num,
        '评论数': comment_num,
    }
    print(data)
    table.update({'文章标题': title}, {'$set': data}, True)




