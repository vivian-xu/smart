# -*- Encoding: utf-8 -*-
import os
import re

BASE_DIR = __file__[:-9]
cache_dir = BASE_DIR + 'cache'
item_ptn = re.compile(ur'class="user-info">(.*?)</p>',re.DOTALL)
info_ptn = re.compile(ur'href="/member/(\d*)">(.*?)</a>.*?(\d*-\d*)?">',re.DOTALL)


for f in os.listdir(cache_dir): #一个店铺主页
    filename = cache_dir+'/'+f
#    print filename
    content = ''

    with open(filename) as fp:
        content = ' '.join(fp.readlines()).decode('utf8')
    item_ret = item_ptn.findall(content)  # 一个店铺每个评价的id和分数信息
#    print ' '.join(item_ret)

    for item in item_ret:  # item是每一个评价的信息 ，item_ret 是一个店铺中所有评价
        info_ret = info_ptn.findall(item)
        for id,nm,sc in info_ret:
            if not sc:
                del id,nm,sc
            else:
                print id,nm,sc