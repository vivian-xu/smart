# -*- Encoding: utf-8 -*-
import os
import re

BASE_DIR = __file__[:-8]
cache_dir = BASE_DIR + 'cache'

items_ptn = re.compile(ur'<dl class="recommend-info clearfix">(.*?)</dl>',re.DOTALL)
key_ptn = re.compile(ur'<dt>(.*?)</dt>',re.DOTALL)
value_ptn = re.compile('">([^>]*?)</a>.*?(?!<dt>)') #否定型顺序环视


for f in os.listdir(cache_dir):  # 一个文件，是一个店铺的主页

    # read content from file
    filename = cache_dir+'/'+f
    text = ''
    with open(filename)  as fp:
         text = ''.join(fp.readlines()).decode('utf8')

    like_dic = {}
    reco_dic = {}
    value_lret = []
    value_rret = []

    print '0' *20

    for item in items_ptn.findall(text):  # 一个店铺，n 条评论，一个 item 是一条评论
        key_ret = key_ptn.findall(item)
#        print '-' *20
#        print item
#        print ','.join(key_ret)
        value_lret = []
        value_rret = []

        for k in key_ret:  #一个 k 是一条评论的一个标签（推荐菜，喜欢的菜，标签）
            if k.startswith(ur'喜欢的菜'): #输出每条评论中喜欢的菜，推荐菜
                value_lret = value_ptn.findall(item)
#                print ','.join(value_lret)
            elif k.startswith(ur'推荐菜'):
                value_rret = value_ptn.findall(item)
#                print ','.join(value_rret)

 #           print '*' *20

        for ret in value_lret or value_rret:
            if ret in like_dic:
                like_dic[ret] += 1
            else:
                like_dic[ret] = 1

    for kl, vl in like_dic.items():
        print kl, vl


'''
        for k, v in item_ret:
            if k.startswith('喜欢的菜：'):
                print ''.join(k)
                print ''.join(v)
        print '------'
'''
