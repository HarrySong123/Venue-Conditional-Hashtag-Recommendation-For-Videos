#!usr/bin/env python
#-*- coding:utf-8 -*-
from nltk.corpus import wordnet as wn
import numpy as np
import jieba
import jieba.analyse
import codecs
#读取文本文件
def read_from_file(directions):      
    decode_set=['utf-8','gb18030','ISO-8859-2','gb2312','gbk','Error']#编码集
    #编码集循环
    for k in decode_set:
        try:
            file = open(directions,"r",encoding=k)
            readfile = file.read()#这步如果解码失败就会引起错误，跳到except。
            
            #print("open file %s with encoding %s" %(directions,k))#打印读取成功
            #readfile = readfile.encode(encoding="utf-8",errors="replace")#若是混合编码则将不可编码的字符替换为"?"。
            file.close()
            break#打开路径成功跳出编码匹配
        except:
            if k=="Error":#如果碰到这个程序终止运行
                raise Exception("%s had no way to decode"%directions)
            continue
    return readfile

#读取文件

keywords=['Galaxy','rctid','LSbeerfest','rockchoir','TR','england','wembley','LAGALAXY','estadioazteca','LAGalaxy']

linestore=['eminent','Wembley','stadium','london','wembleystadium','rap','music','musicvine','vine','repost','lights','crowd','stan','rapper','slimshady','vinefamous']

for line1 in keywords:
    x=0
    for line2 in linestore:
        a=wn.synsets(str(line1))
        b=wn.synsets(str(line2))
        # print(a,str(line1))
        # print(b,str(line2))
        Last=0
        for syn1 in a:
            for syn2 in b:
                score=syn1.path_similarity(syn2)
                # print(str(score))
                if score is not None:
                    if Last<score:
                        Last=score
        if x<Last:
            x=Last
    print(str(line1)+" accuracy is :"+str(x))
