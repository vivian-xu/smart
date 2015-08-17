# -*- Encoding: utf-8 -*-
import os

BASE_DIR = __file__[:-8]

cache_dir = BASE_DIR + 'cache'
print cache_dir

for file in os.listdir(cache_dir):
    filename = cache_dir+'/'+file
    print filename

#    f = open(filename)
    with open(filename)  as f:
        line = ''.join(f.readlines()).decode('gbk')
        print line


#f.close()
