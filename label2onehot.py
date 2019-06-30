# The script is used to test onehot code;
import json
import numpy as np
from keras.utils import to_categorical

b = open(r"F:\2019Hashtag\allEnglishHashtagFinal.txt", "r",encoding='UTF-8')
# read the list of all hashtags

out = b.read()
out = json.loads(out)
# transfer the json file into a dictionary

lengthhashtag=len(out)
# the number of all hashtags

with open('hashtagLabelFinal.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("读取JSON文件中的内容：")

# print(aa.values())
data = aa

keys=aa.keys()

# print(type(keys))
s=""
for i in aa.keys():
    s=i
    if True:
        break
print(s)
data=data[s]
data = np.array(data)
print(data)

one_hots = to_categorical(data,num_classes=lengthhashtag)

one_hots=sum(one_hots).reshape([lengthhashtag,1])

# a.reshape([4,5])
print(one_hots)

# print(shape(one_hots))