#!usr/bin/env python
#-*- coding:utf-8 -*-
# The script which get unrepeating hashtags from 'hashtagEnglish.json' and store its result in 'allEnglishHashtag.txt' as a list;

import json
import io
import sys
# print(content[73843759:73843959])
with open('hashtagEnglishFinal.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("读取JSON文件中的内容：")
    # print(aa)

# print(aa.values())


alltag=[];
progress=0
progressAll=len(aa)
print(progressAll)
for listall in aa.values():
    # 遍历每一个video的taglist
    progress+=1
    if progress%10==0:
        rate=progress/progressAll
        print("Have done "+str(rate*100)+"%")
    
    for word in listall:
        # 遍历taglist中的tag
        
        if word not in alltag:
            alltag.append(word)

alltag=json.dumps(alltag,ensure_ascii=False)

file=open(r"F:\2019Hashtag\allEnglishHashtagFinal.txt","w",encoding='utf-8')
file.write(alltag)
file.close()


        
