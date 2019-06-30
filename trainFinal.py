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
countCut1=0
# counter to cut dataset
# print(type(sys.argv[1]))
enough1=False
enough2=False
for iterofkey in sorted(keyList):
    if countCut>=int(sys.argv[1]):
        try:
            iterofkey=int(iterofkey)
            idfind=videoid.index(iterofkey)
        except Exception as identifier:
            continue
        venue=f['labels'][idfind]
        if venue==20 and not enough1:
            print("20 ",iterofkey)
            trainList.append(iterofkey)
            countCut+=1
            # countCut1+=1
        if venue==39 and not enough2:
            print("39 ",iterofkey)
            trainList.append(iterofkey)
            # countCut+=1
            countCut1+=1
    if countCut>=30:
        enough1=True
    if countCut1>=30:
        enough2=True    
    if countCut1>=30 and countCut>=30:
        break
    # if countCut%10<=6:
    #     trainList.append(iterofkey)
    # elif countCut%10==7 or countCut%10==8:
    #     validationList.append(iterofkey)
    # elif countCut%10==9:
    #     testList.append(iterofkey)
    # countCut+=1
    # if countCut>=100:
    #     break
# cut the dataset
# print("Catch"+trainList[0])
# print("ALL"+str(len(keyList)))
# listBan=['1007573896981270528','999575882702417920','999419352149598208','991085289273442304','987526245833117696','986681847843266560','980309339455762432','979670387220983808','973158362097270784','973117024811249664','969466516909244416','969051363046834176','967449058195419136','967194601318436864','957118065034866688','954682876924960768','954490610717511680','950395012078804992','947627662325747712','942828482482827264','937436023514882048','933238236162187264','931872236133031936','929891046719107072','917556615736082432','1281715919755911168','1281692607952875520','1281273140026445824','1280159741582667776','1279291045833822208','1278459498385887232','1278171586474156032','1278136225450139648','1277751720914849792','1277718394900504576','1277641050949304320','1277564494155227136','1277325632493580288','1277223336073666560','1277027864784920576','1275722268555051008','1275410002840535040','1275312257253163008','1275081459459375104','1274439233347739648','1274356215694426112','1273491503532457984','1272418779397349376','1272337878479163392','1272336620288368640','1272338249272713216','1272338758280663040','1272339823709569024','1272340887598514176','1272341324514881536','1272261689626292224','1272262001661558784','1271924532340486144','1271496592305844224','1270827516793712640','1270538728976809984','1270263892484022272','1270178005142167552','1267588096468692992','1267445924159422464','1267284483783196672','1266536579154243584','1266022728868712448','1265515874991960064','1265103093092200448','1264939967478669312','1264112088029507584','1263930703184846848','1263721856914075648','1263411879343538176','1263036276668846080','1262856910567776256','1262765983794884608','1262675819805949952','1262620954384048128','1262340915969048576','1261537242682900480','1261117799590432768','1259705110259724288','1259508281819766784','1258862755247960064','1258507984468951040','1258348285786296320','1257186771792691200','1256319759021182976','1255526803083583488','1255431571436109824','1254379474909794304','1253001976258650112','1250098173976952832','1250139470909546496','1249208549281095680','1248345490840801280','1245621741926436864','1245184341420998656','1244753515541659648','1241814225274966016','1241279367687143424','1240686848297381888','1239945062352412672','1239745625793404928','1239475373432070144','1237286124527968256','1237126455234809856','1235843113835728896','1234807062631276544','1234727213337919488','1234732651173302272','1233560884778315776','1233320095590359040','1233320230835957760','1233108645810778112','1233049191048699904','1233049843179106304','1233052126327058432','1233061303582126080','1231935095955398656','1231554242704715776','1231269649828687872','1228973483389083648','1226566395068866560','1226568231238942720','1226568940889788416','1226186555442552832','1224384891475677184','1224066160770109440','1222486195154968576','1221221914971164672','1220763492609847296','1218821215876239360','1218263930087284736','1217881289898741760','1215169000795967488','1213736562215874560','1213012399381192704','1213012750347997184','1208700616629985280','1208394730992812032','1208457590787772416','1208462531107475456','1207671548681863168','1207055676154028032','1206948920115769344','1206875442372644864','1206785286701981696','1205121928252604416','1204922882619568128','1204929286260535296','1204907879808049152','1204077390872092672','1203788482082938880','1200844771364061184','1198900497542172672','1198654121423613952','1198483683368407040','1196863141334958080','1196799341709746176','1195700831828541440','1195648898258116608','1194591451464998912','1194302937158299648','1194110577648517120','1194003499953147904','1193848297245278208','1192839278598967296','1192357277173682176','1191991554475696128','1191683773297819648','1191472500824252416','1191359933065875456','1191290198777282560','1191213715975188480','1191017313693065216','1190978614112546816','1188632421529501696','1188623716574449664','1188330356584169472','1188058819000168448','1185531306143096832','1185486334157377536','1185165560217219073','1184499770086092800','1184112011819241472','1184049463510167552','1183977831836078080','1183947205393408000','1183310166503079936','1183051493499432960','1182197849757523968','1182171868564787200','1181948134130143232','1181854612710420480','1181657732064161792','1181150104992788480','1180474617769455616','1180454960068997120','1180418473734631424','1180258952793997312','1180122570876403712','1179102912040062976','1177977653777825792','1177999724389826560','1177938324242034688','1177920917184176128','1177540930996162560','1176940650110042112','1176020009223385088','1175815566972383232','1175382674656108544','1175096304595324928','1174983026204143616','1174383292020391936','1174243710381223936','1173171769251598336','1170991804162658304','1168573062179065856','1168541538750484480','1167536199360245760','1166396309834764288','1166240996821184512','1165109278944948224','1159525919841538048','1159247334094557184','1158225032368226304','1157967134203191296','1157259075722391552','1156360228393328640','1155778925205815296','1155765504393338880','1155053433817079808','1154118528572469248','1152959595472695296','1149888468756152320','1149876222155694080','1148261814161870848','1148134740101402624','1147504168727392256','1147115218367889408','1145343017402949632','1144123841287766016','1141671829438967808','1141439643381088256','1141179252046262272','1141179252046262272','1141080044249518080','1140515970654638080','1139801703441731584','1139797427453415424','1139753133287849984','1139757203595943936','1139244913905618944','1138818301095555072','1138610903580069888','1138475690530877440' ,'1138165042010050560','1138157391213715456','1138063275595272192' ,'1137727045594439680','1137414188600557568','1135443749569282048','1133990014737444864','1130730113319747584' ,'1130109105567358976','1127565949265182720' ,'1118182371540570112' ,'1113061871856001024' ,'1109045437907824640' ,'1102446432247767040','1099936203597586432' ,'1094723310387957760' ,'1093593066021253120' ,'1091871145801699328' ,'1087308731198439424','1084357131672711168','1084360006045941760','1080358012809637888','1079790647621619712','1074963463228588032','1074677472802783232','1074240319459319808','1070575903412727808' ,'1070302740728754176','1068540435087384576','1068065200646844416','1066370641906860032','1064873951379054592','1061732000328769536','1060666518389604352','1055887530367119360','1054776841879662592','1053552602107338752' ,'1052870470032408576' ,'1051545649453092864' ,'1051453238286647296','1048157685704470528','1033997216115052544','1034027303401123840','1017361061445521408','1031613244151869440','1029994381681311744','1026946725803589632','1028807087326945280']
def generate_arrays_from_file_train():
    while 1:
        for i in sorted(trainList):
            # to traverse the videoid in json file
            if(i in BanList):
                continue
            # print()
            # print(i)
            i=int(i)
            # if(i<1007660697678737408):
            #     continue
        
            # i used to be a str,here to change it into int
            # print("id:"+str(i))
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

            data=aa[str(i)]
            # the label list of each video

            one_hots = to_categorical(data,num_classes=lengthhashtag)
            # transfer the int array into a onehot array
            
            outputmatrix=sum(one_hots)
            # get the sum in order to get the value of output

            inputmatrix=numpy.expand_dims(inputmatrix, axis=0)
            # change the matrix to the size of input
            outputmatrix=numpy.expand_dims(outputmatrix, axis=0)        
            # change the matrix to the size of output
            prediction=outputmatrix.flatten()
            # print(type(prediction))
            prediction=prediction.tolist()
            # print(max(prediction))
            # print(prediction)
            ind=prediction.index(max(prediction))
            # print(str(i),out[ind])
            yield(inputmatrix,outputmatrix) 

def generate_arrays_from_file_validation():
    while 1:
        for i in validationList:
            # to traverse the videoid in json file
            if(i in BanList):
                continue

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

            data=aa[str(i)]
            # the label list of each video

            one_hots = to_categorical(data,num_classes=lengthhashtag)
            # transfer the int array into a onehot array

            outputmatrix=sum(one_hots)
            # get the sum in order to get the value of output

            inputmatrix=numpy.expand_dims(inputmatrix, axis=0)
            # change the matrix to the size of input
            outputmatrix=numpy.expand_dims(outputmatrix, axis=0)        
            # change the matrix to the size of output
            yield(inputmatrix,outputmatrix) 

def generate_arrays_from_file_test():
    while 1:
        for i in testList:
            # to traverse the videoid in json file
            
            if(i in BanList):
                continue
            
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

            data=aa[str(i)]
            # the label list of each video

            one_hots = to_categorical(data,num_classes=lengthhashtag)
            # transfer the int array into a onehot array

            outputmatrix=sum(one_hots)
            # get the sum in order to get the value of output


            inputmatrix=numpy.expand_dims(inputmatrix, axis=0)
            # change the matrix to the size of input
            outputmatrix=numpy.expand_dims(outputmatrix, axis=0)        
            # change the matrix to the size of output
            
            yield(inputmatrix,outputmatrix) 

model = keras.Sequential()
# initialize a model

model.add(keras.layers.Dense(64, activation='relu', input_shape=(sizeinput,)))
# Add a layer with sizeinput units
model.add(keras.layers.Dropout(0.5))

model.add(keras.layers.Dense(32, activation='relu'))
# Allconnected layer
model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(64, activation='tanh'))
# Allconnected layer
# model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(lengthhashtag, activation='sigmoid'))
# Add a softmax layer with hashtagsize output units:
# sgd = keras.optimizers.SGD(lr=0.1, decay=1e-3, clipvalue=0.5)
# sgd1 = keras.optimizers.clip_norm=1

# sgd = keras.optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True,clipvalue=0.5)
adam=keras.optimizers.Adam(lr=0.0001)
model.compile(loss='binary_crossentropy',
              optimizer='Adam',
              metrics=['accuracy'])


# model.fit_generator(generate_arrays_from_file_train(),epochs=3,verbose=2,validation_data=validationList,steps_per_epoch=len(trainList))
lentrain=len(trainList)
lenvalidation=len(validationList)
model.fit_generator(generate_arrays_from_file_train(),epochs=500,steps_per_epoch=lentrain,callbacks=[keras.callbacks.TerminateOnNaN()])    

# lentest=1

# loss,accuracy=model.evaluate_generator(generate_arrays_from_file_test(),steps=lentest)

# print('loss',loss)
# print('accuracy',accuracy)
model.save('modelnewSigmoidBinary.h5')
