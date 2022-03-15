import os
import random

#将图片分成了训练集，验证集和测试集；存储在ImageSets,存储内容为图片ID
trainval_percent = 0.9
train_percent = 0.9  #train.py中有区分验证集的操作
xmlfilepath = './Annotations'
txtsavepath = './JPEGImages'
total_xml = os.listdir(xmlfilepath)  #所有xml文件

num = len(total_xml)   #xml文件总数，即所有图片总数
list = range(num)      #从0数到num（不包括num）
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)   #从list中随机取tv个元素，即从所有图片中随机取90%
train = random.sample(trainval, tr)  #从上面90%中随机取90%

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:    #90%-trainval.txt
        ftrainval.write(name)
        if i in train:   #trainval中的90%-train.txt
            ftrain.write(name)
        else:            #trainval中的10%-val.txt
            fval.write(name)
    else:                #90%-test.txt
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
