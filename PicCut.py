import cv2
import os
import numpy as np


img = cv2.imread("62.jpg")
img2 = cv2.imread("2.jpg")
imgs = np.hstack([img,img2])

all_img_path = []

next = True


def cutImg(imgPath):
    next = False
    pass


def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), thickness=1)
        y0 = y - 45
        y1 = y + 45
        x0 = x - 45
        x1 = x + 45

        print(f"中心点坐标（{x}，{y}）")    
        print(f"x轴坐标({x0},{x1})")
        print(f"y轴坐标({y0},{y1})")

        cv2.rectangle(img, (x0, y0), (x1, y1), (0, 0, 255), 1, cv2.LINE_AA)
        imgs = np.hstack([img, img2])
        cv2.imshow("muti_pic", imgs)


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')#去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存成功")


def open_muti_pic():

    cv2.imshow("muti_pic", imgs)

    cv2.setMouseCallback("muti_pic",mouse)
    cv2.waitKey(0)

    pass


def main():
    open_muti_pic()
    print(img.shape)
    pass
    # f = open('filename.txt')
    # line = f.readline()  # 调用文件的 readline()方法
    # while line:
    #     # print(line, end = '')
    #     all_img_path.append(line)
    #     line = f.readline()
    # f.close()
    # print("done")
    # file_path = "C:\\Users\\GaoLong\\Desktop\\301jpg"
    #
    # i = 0
    # while next:
    #     cutImg(all_img_path[i])





    # for root, dirs, files in os.walk(file_path):
    #
    #     # root 表示当前正在访问的文件夹路径
    #     # dirs 表示该文件夹下的子目录名list
    #     # files 表示该文件夹下的文件list
    #
    #     # 遍历文件
    #     #for f in files:
    #         #print(os.path.join(root, f))
    #         # img_path = os.path.join(root, f)
    #         # all_img_path.append(img_path)
    #         image = cv2.imread("62.jpg")
    #         # cv2.namedWindow("image")
    #         # cv2.imshow("image", img)
    #
    #     # 遍历所有的文件夹
    #     # for d in dirs:
    #     #     print(os.path.join(root, d))


    #text_save("filename.txt",all_img_path)

    # size = img.shape
    #
    # w = size[1]  # 宽度
    #
    # h = size[0]  # 高度
    #
    # print(size)
    # print(w)
    # print(h)
    # cv2.namedWindow("image")
    # cv2.imshow("image", img)
    # row, col, chanel = img.shape
    #
    # cv2.resizeWindow("image", 800, 600)
    # cv2.setMouseCallback("image", mouse)
    #
    # k = cv2.waitKey(0)
    # if k == 27:
    #     cv2.destroyAllWindows()


if __name__ == '__main__':
    main()