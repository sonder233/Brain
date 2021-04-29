# import  SimpleITK
# from matplotlib import pyplot as plt
# import numpy as np
# import heapq
# import os
#
# origin_path = "D:/lab/machine_learning/heci/301/data/New_Predeal"
# seg_path = "D:/lab/machine_learning/heci/301/data/New_Predeal"
# for root,dirs,files in os.walk(seg_path):
#     for i in dirs:
#         for i in files:
#             if i[-9:] == "T2.nii.gz":
#                 second_path = i[0:7]
#         for i in files:
#             if "Seg" in i:
#                 path = seg_path+"/"+second_path+"/"+i
#                 tmp = SimpleITK.ReadImage(path)
#                 #plt.imshow(SimpleITK.GetArrayFromImage(tmp)[0], cmap=plt.cm.bone)
#                 data = SimpleITK.GetArrayFromImage(tmp)
#                 # print(data.shape[0])
#                 cnt_Arr = []
#                 for i in range(data.shape[0]):
#                     cnt = 0
#                     img = np.array(SimpleITK.GetArrayFromImage(tmp)[i])
#                     # print(img)
#                     rows,cols=img.shape
#                     for i in range(rows):
#                         for j in range(cols):
#                             if(img[i,j] != 0.0):
#                                 cnt += 1
#                     cnt_Arr.append(cnt)
#                 nparr = np.array(cnt_Arr)
#                 res_arr = heapq.nlargest(3, range(len(nparr)), nparr.take)
#
#                 T1_path = seg_path+"/"+second_path+"/"+second_path+"_T1.nii.gz"
#                 if os.path.isfile(T1_path) == False:
#                     T1_path = seg_path+"/"+second_path+"/"+second_path+"_T1c.nii.gz"
#                 T2_path = seg_path+"/"+second_path+"/"+second_path+"_T2.nii.gz"
#                 image_T1 = SimpleITK.ReadImage(T1_path)
#                 image_array_T1 = SimpleITK.GetArrayFromImage(image_T1)[res_arr]
#                 image_T2 = SimpleITK.ReadImage(T2_path)
#                 image_array_T2 = SimpleITK.GetArrayFromImage(image_T2)[res_arr]
#                 image_array_deal=np.array((image_array_T1,image_array_T2))
#                 try:
#                     image_array_deal=image_array_deal.reshape(6,256,256)
#                 except Exception:
#                     image_array_deal=image_array_deal.reshape(6,512,512)
#                 for j in range(6):
#                     image_array_deal[j]=(image_array_deal[j]-np.mean(image_array_deal[j]))/np.std(image_array_deal[j], ddof = 1)
#                 out = SimpleITK.GetImageFromArray(image_array_deal)
#                 filename_out="D:/lab/machine_learning/heci/301/data/Predeal/"+second_path+'.nii.gz'
#                 SimpleITK.WriteImage(out,filename_out)
#                 print(second_path+" Done")

import  SimpleITK
from matplotlib import pyplot as plt
import numpy as np
import heapq
import os

origin_path = "F:/data/MRI/TCGA-SELECTED/TCGA-GBM"
seg_path_base = "F:/data/MRI/TCGA-SELECTED/TCGA-GBM"
for root,dirs,files in os.walk(origin_path):
    for folder in dirs:
        #print(segmentpath)
        if folder[0:4] == "TCGA":
            #print(folder)
            tag_name = folder
            First_path = seg_path_base+"/"+folder
            print(First_path)
            for root,dirs,files in os.walk(First_path):
                for folder in dirs:
                    if folder == "native":
                        #print(folder)
                        seg_path = First_path+"/"+folder
                        for root,dirs,files in os.walk(seg_path):
                            for i in files:
                                 if "Seg" in i:
                                    #print(i)
                                    path = seg_path+"/"+i
                                    #print(path)
                                    tmp = SimpleITK.ReadImage(path)
                                    #print(tmp)
                                    data = SimpleITK.GetArrayFromImage(tmp)
                                    cnt_Arr = []
                                    for i in range(data.shape[0]):
                                        cnt_Arr.append(np.sum(data[i])) # 获得每个照片的权值
                                    nparr = np.array(cnt_Arr)
                                    res_arr = heapq.nlargest(3, range(len(nparr)), nparr.take) # 得到权值最大的三张图片
                                    # print(res_arr)

                                    T1_path = seg_path+"/"+"T1.nii.gz"
                                    T1c_path = seg_path+"/"+"T1c.nii.gz"
                                    T2_path = seg_path+"/"+"T2.nii.gz"
                                    Flair_path = seg_path+"/"+"Flair.nii.gz"

                                    image_T1 = SimpleITK.ReadImage(T1_path)
                                    image_array_T1 = SimpleITK.GetArrayFromImage(image_T1)[res_arr]

                                    image_T1c = SimpleITK.ReadImage(T1c_path)
                                    image_array_T1c = SimpleITK.GetArrayFromImage(image_T1c)[res_arr]

                                    image_T2 = SimpleITK.ReadImage(T2_path)
                                    image_array_T2 = SimpleITK.GetArrayFromImage(image_T2)[res_arr]

                                    image_Flair = SimpleITK.ReadImage(Flair_path)
                                    image_array_Flair = SimpleITK.GetArrayFromImage(image_Flair)[res_arr]

                                    image_array_deal=np.array((image_array_T1, image_array_T1c,image_array_T2, image_array_Flair))
                                    print(image_array_T1.shape)
                                    size_h=image_array_T1.shape[1]
                                    size_w = image_array_T1.shape[2]
                                    try:
                                        image_array_deal=image_array_deal.reshape(12,size_h, size_w)
                                    except Exception:
                                        image_array_deal=image_array_deal.reshape(12,size_h, size_w)
                                    for j in range(6):
                                        #print(np.std(image_array_deal[j], ddof = 1))
                                        image_array_deal[j]=(image_array_deal[j]-np.mean(image_array_deal[j]))/max(1,np.std(image_array_deal[j], ddof = 1))
                                    out = SimpleITK.GetImageFromArray(image_array_deal)
                                    filename_out="F:/data/MRI/TCGA-SELECTED/New-Predeal-GBM/"+tag_name+'.nii.gz'
                                    SimpleITK.WriteImage(out,filename_out)
                                    print(tag_name+" Done")




'''
import zipfile
import pandas as pd
filebase='E:/本科/项目/核磁/data/TCGA/TCGA-GBM/'
filebaseunzip='F:/data/MRI/TCGA-SELECTED/TCGA-GBM/'

LGG=pd.read_csv('E:/本科/项目/核磁/data/GBM_TAG_Selection.csv')
cnt=0
for index,i in LGG.iterrows():
    cnt=cnt+1
    print(cnt)
    filename=filebase+i[0]+'.zip'
    print(filename)
    frzip = zipfile.ZipFile(filename, 'r', zipfile.ZIP_DEFLATED)
    filenameunzip=filebaseunzip+i[0]
    if not os.path.exists(filenameunzip):
        os.makedirs(filenameunzip)
    frzip.extractall(filenameunzip)
    frzip.close()
'''
