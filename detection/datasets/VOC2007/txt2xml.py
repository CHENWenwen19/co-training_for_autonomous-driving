#-*-coding:utf-8-*-
# 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML
from xml.dom.minidom import Document
# python3.7下安装cv2，本机不能直接pip安装，搜索安装包进行安装
import cv2
import os

# 传入序号，
def generate_xml(name,split_lines,img_size,class_ind):
   doc = Document()  # 创建DOM文档对象
   # 问题：创建document对象，如果存在则会把文件价名加在里面的文件前面？
   # 上述问题是在写路径时候Annotations没加反斜杠
   annotation = doc.createElement('annotation')
   # appendChild方法的规定就是向节点添加最后一个子节点。
   doc.appendChild(annotation)

   # 测试输出文件位置问题
   # print("document start")

   # 这里开始写入XML，可具体看每个xml的内容
   title = doc.createElement('folder')
   title_text = doc.createTextNode('VOC2007')#这里修改了文件夹名
   # appendChild:添加子节点
   title.appendChild(title_text)
   annotation.appendChild(title)

   # img_name=name+'.png'#要用jpg格式
   img_name = name + '.jpg'

   title = doc.createElement('filename')
   title_text = doc.createTextNode(img_name)
   title.appendChild(title_text)
   annotation.appendChild(title)

   source = doc.createElement('source')
   annotation.appendChild(source)

   title = doc.createElement('database')
   title_text = doc.createTextNode('The VOC2007 Database')#修改为VOC
   title.appendChild(title_text)
   source.appendChild(title)

   title = doc.createElement('annotation')
   title_text = doc.createTextNode('PASCAL VOC2007')#修改为VOC
   title.appendChild(title_text)
   source.appendChild(title)

   size = doc.createElement('size')
   annotation.appendChild(size)

   title = doc.createElement('width')
   title_text = doc.createTextNode(str(img_size[1]))
   title.appendChild(title_text)
   size.appendChild(title)

   title = doc.createElement('height')
   title_text = doc.createTextNode(str(img_size[0]))
   title.appendChild(title_text)
   size.appendChild(title)

   title = doc.createElement('depth')
   title_text = doc.createTextNode(str(img_size[2]))
   title.appendChild(title_text)
   size.appendChild(title)

   for split_line in split_lines:
       line=split_line.strip().split()
       if line[0] in class_ind:
           object = doc.createElement('object')
           annotation.appendChild(object)

           title = doc.createElement('name')
           title_text = doc.createTextNode(line[0])
           title.appendChild(title_text)
           object.appendChild(title)

           title = doc.createElement('difficult')
           title_text = doc.createTextNode('0')
           title.appendChild(title_text)
           object.appendChild(title)

           bndbox = doc.createElement('bndbox')
           object.appendChild(bndbox)
           title = doc.createElement('xmin')
           title_text = doc.createTextNode(str(int(float(line[1]))))
           title.appendChild(title_text)
           bndbox.appendChild(title)
           title = doc.createElement('ymin')
           title_text = doc.createTextNode(str(int(float(line[2]))))
           title.appendChild(title_text)
           bndbox.appendChild(title)
           title = doc.createElement('xmax')
           title_text = doc.createTextNode(str(int(float(line[3]))))
           title.appendChild(title_text)
           bndbox.appendChild(title)
           title = doc.createElement('ymax')
           title_text = doc.createTextNode(str(int(float(line[4]))))
           title.appendChild(title_text)
           bndbox.appendChild(title)

   # 将DOM对象doc写入文件
   f = open('/home/nj/文档/moco/detection/datasets/VOC2007*/Annotations_fstandyolov4_0.7/' + name + '.xml', 'w')
   f.write(doc.toprettyxml(indent = ''))
   f.close()

if __name__ == '__main__':
   class_ind=('car', 'pedestrian', 'cyclist')# 修改为了3类
   # cur_dir=os.getcwd()
   # 这个路径是label的上一层，不加反斜杠
   labels_dir = os.path.join("/home/nj/文档/moco/detection/datasets/VOC2007*", 'combine_fstandyolov4_0.7')
   # os.walk方法,主要用来遍历一个目录内各个子目录和子文件
   for parent, dirnames, filenames in os.walk(labels_dir): # 分别得到根目录，子目录和根目录下文件
       # 对于根目录下的文件，先取得路径得到前面的文件序号，再生成新的xml
       for file_name in filenames:
           full_path=os.path.join(parent, file_name) # 获取文件全路径
           #print full_path
           f=open(full_path)
           # 读取所有行
           split_lines = f.readlines()
           name= file_name[:-4] # 后四位是扩展名.txt，只取前面的文件名
           #print name
           img_name = name + '.jpg'
           # 将要训练的图片路径添加入img_path中
           img_path = os.path.join('/home/nj/文档/moco/detection/datasets/VOC2007*/JPEGImages', img_name)
           #print img_path
           img_size=cv2.imread(img_path).shape
           # 文件序号，每一行，图片大小，目标类别
           generate_xml(name,split_lines,img_size,class_ind)
print('all txts has converted into xmls')

