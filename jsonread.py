#!usr/bin/env python
#-*- coding:utf-8 -*-
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
filename=r"F:/2019Hashtag/jsontest.json"
file=open(filename,"rb")
content=file.readlines()
content="".join('%s' %id for id in content)
length=len(content)
file.close
print("length"+str(length))
# print(content[73843759:73843959])
with open('hashtagLabel.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("读取JSON文件中的内容：")

for i in aa.values():
    for j in i:
        print(type(j))
    