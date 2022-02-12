"""中华新华字典功能"""
from botoy import GroupMsg, FriendMsg, Picture, Text
from botoy.collection import MsgTypes
from botoy.decorators import ignore_botself, startswith
from botoy.parser import group as gp# 群消息(GroupMsg)相关解析
from botoy.parser import friend as fp # 好友消息(FriendMsg)相关解析
from botoy import jconfig, logger

import httpx,random,time,ijson,re

@ignore_botself#忽略机器人自身的消息
def receive_group_msg(ctx: GroupMsg):
    if(ctx.Content.find("的聊天记录")!=-1):
        return
    elif(ctx.Content.find("查询成语")!=-1 or ctx.Content.find("成语查询")!=-1):
        text = ctx.Content.replace(" ", "")[4:]#替换前4个字为空
        if not text:
            Text("未检测到成语")
        else:
            Text(idiom(text))
        return
    elif(ctx.Content.find("查询汉字")!=-1 or ctx.Content.find("汉字查询")!=-1):
        text = ctx.Content.replace(" ", "")[4:]#替换前4个字为空
        if not text:
            Text("未检测到汉字")
        elif len(text)>1:
            Text("只能查询单个汉字嗷")
        else:
            Text(word(text))
        return
    elif(ctx.Content.find("查询词语")!=-1 or ctx.Content.find("词语查询")!=-1):
        text = ctx.Content.replace(" ", "")[4:]#替换前4个字为空
        if not text:
            Text("未检测到词语")
        else:
            Text(ciyu(text))
        return
    elif(ctx.Content.find("查询歇后语")!=-1 or ctx.Content.find("歇后语查询")!=-1):
        text = ctx.Content.replace(" ", "")[5:]#替换前4个字为空
        if not text:
            Text("未检测到歇后语")
        else:
            Text(xiehouyu(text))
        return
    
@ignore_botself#忽略机器人自身的消息
def receive_friend_msg(ctx: FriendMsg):
    if(ctx.Content.find("的聊天记录")!=-1):
        return
    elif(ctx.Content.find("查询成语")!=-1 or ctx.Content.find("成语查询")!=-1):
        text = ctx.Content.replace(" ", "")[4:]#替换前4个字为空
        if not text:
            Text("未检测到成语")
        else:
            Text(idiom(text))
        return
    elif(ctx.Content.find("查询汉字")!=-1 or ctx.Content.find("汉字查询")!=-1):
        text = ctx.Content.replace(" ", "")[4:]#替换前4个字为空
        if not text:
            Text("未检测到汉字")
        elif len(text)>1:
            Text("只能查询单个汉字嗷")
        else:
            Text(word(text))
        return
    elif(ctx.Content.find("查询词语")!=-1 or ctx.Content.find("词语查询")!=-1):
        text = ctx.Content.replace(" ", "")[4:]#替换前4个字为空
        if not text:
            Text("未检测到词语")
        else:
            Text(ciyu(text))
        return
    elif(ctx.Content.find("查询歇后语")!=-1 or ctx.Content.find("歇后语查询")!=-1):
        text = ctx.Content.replace(" ", "")[5:]#替换前4个字为空
        if not text:
            Text("未检测到歇后语")
        else:
            Text(xiehouyu(text))
        return
    
def idiom(strs1):
    cacheFileName = './plugins/bot_chinesexinhua/data/idiom.json'
    with open(cacheFileName, 'r', encoding='utf-8') as f:
        obj = list(ijson.items(f, 'item'))
    for i in range(len(obj)):
        users = obj[i]['word']
        if(users == strs1):
            return "【"+strs1+"】"+obj[i]['pinyin']+"\n出处："+obj[i]['derivation']+"\n释义："+obj[i]['explanation']+"\n例句："+obj[i]['example']
    return "未查找到"
    
def word(strs1):
    cacheFileName = './plugins/bot_chinesexinhua/data/word.json'
    with open(cacheFileName, 'r', encoding='utf-8') as f:
        obj = list(ijson.items(f, 'item'))
    for i in range(len(obj)):
        users = obj[i]['word']
        if(users == strs1):
            return "【偏旁："+obj[i]['radicals']+"】"+"【"+obj[i]['oldword']+"】"+strs1+"[笔画"+obj[i]['strokes']+"]"+"["+obj[i]['pinyin']+"]"+"\n释义："+obj[i]['explanation'].replace("\n\n", "\n").replace("\n \n", "\n")
    return "未查找到"
    
def xiehouyu(strs1):
    cacheFileName = './plugins/bot_chinesexinhua/data/xiehouyu.json'
    strs_c=str_chinese(strs1)
    with open(cacheFileName, 'r', encoding='utf-8') as f:
        obj = list(ijson.items(f, 'item'))
    for i in range(len(obj)):
        users = str_chinese(obj[i]['riddle'])
        if(users == strs_c):
            return obj[i]['riddle']+"——"+obj[i]['answer']
    return "未查找到"
    
def ciyu(strs1):
    cacheFileName = './plugins/bot_chinesexinhua/data/ci.json'
    with open(cacheFileName, 'r', encoding='utf-8') as f:
        obj = list(ijson.items(f, 'item'))
    for i in range(len(obj)):
        users = obj[i]['ci']
        if(users == strs1):
            return "【"+strs1+"】"+"\n释义："+obj[i]['explanation'].replace("\n\n", "\n").replace("\n \n", "\n")
    return "未查找到"
    
#仅保留中文字符
def str_chinese(strs):
    return re.sub('[^\u4e00-\u9fa5]+', '', strs)