#!usr/bin/env python
#-*- coding:utf-8 -*-
import json
import io
import sys
# print(content[73843759:73843959])
with open('hashtagEnglishFinal.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("读取JSON文件中的内容：")
    # print(aa)
b = open(r"F:\2019Hashtag\allEnglishHashtagFinal.txt", "r",encoding='UTF-8')
out = b.read()
out = json.loads(out)


alltag=[]
Dicnew={}
progress=0
progressAll=len(aa)
print(progressAll)
for keyiter in aa.keys():
    # 遍历每一个video的taglist
    progress+=1
    if progress%10==0:
        rate=progress/progressAll
        print("Have done "+str(rate*100)+"%")
    
    listall=aa[keyiter]
    keylist=[]
    for word in listall:
        # 遍历taglist中的tag
        keylist.append(out.index(word))
    Dicnew[keyiter]=keylist

Dicnew=json.dumps(Dicnew,ensure_ascii=False)

filew=open(r"F:/2019Hashtag/hashtagLabelFinal.json",'w',encoding='utf-8')
filew.write(Dicnew)
filew.close


        
