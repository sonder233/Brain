import matplotlib.pyplot as plt
import cv2
from scipy.io import loadmat
import os

img = cv2.imread("62.jpg")
img2 = cv2.imread("2.jpg")
imgs = [img,img2]
file_path = r"G:\Brain_tumor\301samp_后20_jpg\jiqiulian\flair"
for root, dirs, files in os.walk(file_path):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        #遍历文件
        for f in files:
            print(os.path.join(root, f))

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))

plt.figure()
for i in range(1,150):  # X为图片的个数
    plt.subplot(30,5,i)  # a,b 分别为图片集的行数，列数
    plt.imshow(img)
plt.show()