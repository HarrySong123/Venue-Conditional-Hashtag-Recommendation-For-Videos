import h5py  #导入工具包
import numpy as np
import json
import io
import sys
# print(content[73843759:73843959])
with open('hashtagEnglish.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("读取JSON文件中的内容：")
    # print(aa)

#HDF5的读取：
f = h5py.File('raw_dataset.h5','r')   #打开h5文件
# print(list(f.keys()))                            #可以查看所有的主键
# features = f['features'][0]                    #取出主键为data的所有的键值
videoid=f['videos_id'][:]
# print(type(videoid))
videoid=videoid.tolist()
# print(type(videoid))
keyList=aa.keys()
count=0
allc=len(keyList)
rate=0
newdic={}
for i in keyList:
    rate+=1
    if rate%10==0:
        print("Have done "+str(rate/allc*100)+"%")
    i=int(i)
    # print(type(i))
    if i in videoid:
        newdic[i]=aa[str(i)]
    # print(idfind)
    # features = f['features'][idfind]                    #取出主键为data的所有的键值
    # venue=f['labels'][idfind]
    # print(features)
    # print(venue)
    # print(type(aa[str(i)]))
str_json = json.dumps(newdic, ensure_ascii=False)
# 不加ensure_ascii=False会只写入ascii符号
filew=open(r"F:/2019Hashtag/hashtagEnglishFinal.json",'w',encoding='utf-8')
filew.write(str_json)
f.close()