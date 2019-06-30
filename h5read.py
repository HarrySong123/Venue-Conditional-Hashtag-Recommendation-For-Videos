import h5py  #导入工具包
import numpy as np
#HDF5的读取：
f = h5py.File('raw_dataset.h5','r')   #打开h5文件
print(list(f.keys()))                            #可以查看所有的主键
features = f['features'][95529]                    #取出主键为data的所有的键值
videoid=f['videos_id'][:]
print(features)
print(type(videoid))
videoid=videoid.tolist()
print(type(videoid))
idfind=videoid.index(1037959866251350016)
print(idfind)
f.close()