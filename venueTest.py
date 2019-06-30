import keras
import numpy
import sys
import h5py
import json
import io
import sys
import random
from keras.utils import to_categorical
import tensorflow as tf


maxvenue=188

b = open(r"F:\2019Hashtag\allEnglishHashtagFinal.txt", "r",encoding='UTF-8')
# read the list of all hashtags

out = b.read()
out = json.loads(out)
b.close()
# transfer the json file into a dictionary

lengthhashtag=len(out)
# the number of all hashtags

banl=open(r"F:\2019Hashtag\BanList.txt", "r",encoding='UTF-8')
BanList = banl.read()
BanList = json.loads(BanList)
banl.close()

print(type(BanList))
with open('hashtagLabelFinal.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("Reading Json File")
# The json file includes a dictionary whose key is video_id and its value is the label of hashtag

f = h5py.File('raw_dataset.h5','r')
# The hdf5 file includes 3 keys:video_id,label,features

videoid=f['videos_id'][:]
videoid=videoid.tolist()
# videoid:a list to store video_id in order to get its index
sizeinput = f['features'][0].size + 1
# the size of input

keyList=aa.keys()
# The videoid in json file

keyList=list(keyList)
# transfer the dict_keys into list

# random.shuffle(keyList)

allc=len(keyList)
# the total number of video in json file

rate=0
# to know how the progress is

# train=0.7 vaidation=0.2 test=0.1
trainList=[]
validationList=[]
testList=[]

countCut=0
# counter to cut dataset
# print(type(sys.argv[1]))
venueid=int(sys.argv[1])
for iterofkey in sorted(keyList):
    iterofkey=int(iterofkey)
    try:
        idfind=videoid.index(iterofkey)
    except Exception as identifier:
        continue    
    venue=f['labels'][idfind]
    if venue==venueid:
        print(iterofkey)