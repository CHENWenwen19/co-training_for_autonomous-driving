import os

txt_v1 = './filter_fst_0.7'
txt_v2 = './filter_yolov4_0.7'
total_txt_v1 = os.listdir(txt_v1)
total_txt_v2 = os.listdir(txt_v2)


for i in range(len(total_txt_v1)):
    name_v1 = total_txt_v1[i][:-4]
    for j in range(len(total_txt_v2)):
        name_v2 = total_txt_v2[j][:-4]
        if name_v1 == name_v2:
            f_v1 = open(os.path.join(txt_v1, total_txt_v1[i]), 'r')

            lines_v1 = f_v1.readlines()
            for line_v1 in lines_v1:
                line_v1_ele = line_v1.strip().split()

                f_v2 = open(os.path.join(txt_v2, total_txt_v2[j]), 'r')
                lines_v2 = f_v2.readlines()
                for line_v2  in lines_v2:
                    line_v2_ele = line_v2.strip().split()
                    if line_v1_ele[0] == line_v2_ele[0] and abs(float(line_v1_ele[1])-float(line_v2_ele[1]))<50:
                        #标签相同且bbox的xmin相差不超过50,则认为两者预测的是同一目标，比较其置信度，留下大的对应的标签
                        f_combine = open('combine_fstandyolov4_0.7/' + name_v1 + '.txt', 'a')
                        if line_v1_ele[-1]>line_v2_ele[-1]:
                            f_combine.write(line_v1)
                        else:
                            f_combine.write(line_v2)
                        f_combine.close()
                f_v2.close()

            f_v1.close()
