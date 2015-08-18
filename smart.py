# -*- Encoding: utf-8 -*-

import os
import re

BASE_DIR = __file__[:-8]

cache_dir = BASE_DIR + 'cache'
print cache_dir



for file in os.listdir(cache_dir):
    filename = cache_dir+'/'+file
    print filename

    text = ''
    with open(filename)  as f:
         text = ''.join(f.readlines())

    items_ptn = re.compile(ur'<dl class="recommend-info clearfix">(.*?)</dl>',re.DOTALL)
    items_ret = items_ptn.findall(text)
    print '' .join(items_ret).decode('utf8')
    print '*' *(30)

    for item in items_ret:
#        item_ptn = re.compile(ur'>([^>]*?)\s*</')
#        item_ret = item_ptn.findall(item)

#        print '\n'.join(item_ret).decode('utf8')
        item_ptn = re.compile(ur'<dt>(.*?)</dt>.*?>([^>]*?)</',re.DOTALL)
        item_ret = item_ptn.findall(item)
#        print ''.join(item_ret).decode('utf8')
        for k, v in item_ret:
            print ''.join(k).decode('utf8')
            print ''.join(v).decode('utf8')
    print '------'



