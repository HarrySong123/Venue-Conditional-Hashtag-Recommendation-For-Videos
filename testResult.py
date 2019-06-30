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
import heapq
maxvenue=188
b = open(r"F:\2019Hashtag\allEnglishHashtagFinal.txt", "r",encoding='UTF-8')
# read the list of all hashtags

out = b.read()
out = json.loads(out)
b.close()

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
name1=""
countCut=0
# counter to cut dataset
# print(type(sys.argv[1]))
for iterofkey in sorted(keyList):
    if countCut>=int(sys.argv[1]):
        trainList.append(iterofkey)
    # elif countCut==0 or countCut==1:
    #     validationList.append(iterofkey)
    # elif countCut==2:
    #     testList.append(iterofkey)
    # countCut+=1
    # if countCut>50000:
    #     break
    # if countCut%10<=6:
        # trainList.append(iterofkey)
    # elif countCut%10==7 or countCut%10==8:
    #     validationList.append(iterofkey)
    # elif countCut%10==9:
    #     testList.append(iterofkey)
    countCut+=1

def generate_arrays_from_file_test():
    for i in sorted(trainList):
        # to traverse the videoid in json file
        i='1273583111296454656'
        print(i)
        name1=i
        i=int(i)
        # i used to be a str,here to change it into int

        idfind=videoid.index(i)
        # the index of HDF5 videoid of the json file's videoid 

        features = f['features'][idfind]
        venue=f['labels'][idfind]
        # get the features and venue in nparray
        # here venue is a integar id to represent the venue, and its venue name 
        # can be read from 'leaf_venue_name.txt'
        
        venue=venue/maxvenue
        # regularize the venue
        
        inputmatrix=numpy.hstack((features,venue))
        # matrix merging to a new matrix inputmatrix

        # data=aa[str(i)]
        # the label list of each video

        inputmatrix=numpy.expand_dims(inputmatrix, axis=0)
        # change the matrix to the size of input      
        # change the matrix to the size of output
    
        return inputmatrix


model = keras.models.load_model("modelnew.h5")

prediction = model.predict(generate_arrays_from_file_test())

prediction=prediction.flatten()
print(type(prediction))
prediction=prediction.tolist()
print(max(prediction))
# print(prediction)
max_num_index_list = map(prediction.index, heapq.nlargest(10, prediction))
# ind=prediction.index(max(prediction))
for ind in max_num_index_list:
    print(name1,out[ind])
