#!usr/bin/env python
#-*- coding:utf-8 -*-
import math
import os
import glob
import numpy as np
import jieba
import string
import jieba.analyse
import sys,time
import json
 
def is_number(uchar):
        """判断一个unicode是否是数字"""
        if uchar >= u'\u0030' and uchar<=u'\u0039':
                return True
        else:
                return False



def is_alphabet(uchar):
        """判断一个unicode是否是英文字母"""
        if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                return True
        else:
                return False


filename=r"./location_videos_description"
file=open(filename, "r",encoding='utf-8')
# file=open(filename, "r")
# 计数
count=0
# 文件总行数
lenF=0
for index, line in enumerate(open(filename,'rb')):
    lenF += 1
print("总长度为"+str(lenF))
# 存储的字典

dic={}
print("Reading...")
while 1:
    # L means hashtag list,id means video id
    # 计数

    count=count+1
    if count%20==0:
        left=count/lenF*100
        print("->"+str(left)+"%")
   
    # 负责读取每一行
    hastag=False
    L=[]
    id=""
    line=file.readline()
    line=str(line)
    # print(line)
    if not line:
        break
    i=0
    while 1:
        # 负责读取Hashtag的List
        # print(line[i])
        if line[i]=="#":
            needadd=""
            hastag=True
            while 1:
                needadd=needadd+line[i]
                i=i+1
                if line[i]=="\r" or line[i]=="\n" or i>=len(line)-1 or line[i]=="#" or line[i]==" " or line[i]=="." or line[i]=="," or line[i]=="!" or line[i]=="?" or line[i]=="\\" or not(is_alphabet(line[i]) or is_number(line[i])):
                    L.append(needadd)
                    break
        else:
            i=i+1
            if i>=len(line):
                break
    i=0
    while 1:
        # 读取id
        try:
            if line[i]==":":
                id=line[:i]
                # print(line)
                # print(id)
                break
            else:
                i=i+1
                if i>len(line):
                    break
        except Exception as identifier:
            print(i)
            print(line)
        

    if hastag==False:
        continue
    else:
        # print(L)
        dic[id]=L

print("\nFinished")

str_json = json.dumps(dic, ensure_ascii=False)
# 不加ensure_ascii=False会只写入ascii符号
filew=open(r"F:/2019Hashtag/hashtagEnglish.json",'w',encoding='utf-8')
filew.write(str_json)
filew.close