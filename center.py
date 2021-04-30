import numpy as np
import cv2
from PIL import Image
import os
from tqdm import tqdm
'''
黑底图片居中 母图120*120  使肿瘤居中
'''

def Picture_Synthesis(mother_img, son_img, save_img):
    """
    图片叠加
    :param mother_img: 母图
    :param son_img: 子图
    :param save_img: 保存图片名
    :return:
    """
    #将图片赋值,方便后面的代码调用
    M_Img = Image.fromarray(mother_img)
    S_Img = Image.fromarray(son_img)
    factor = 1
    # 子图缩小的倍数1代表不变，2就代表原来的一半
    # print(type(M_Img))

    # 获取图片的尺寸
    M_Img_w, M_Img_h = M_Img.size  # 获取被放图片的大小（母图）
    # print("母图尺寸：", M_Img.size)
    S_Img_w, S_Img_h = S_Img.size  # 获取小图的大小（子图）
    # print("子图尺寸：", S_Img.size)

    size_w = int(S_Img_w / factor)
    size_h = int(S_Img_h / factor)

    # 防止子图尺寸大于母图
    if S_Img_w > size_w:
         S_Img_w = size_w
    if S_Img_h > size_h:
         S_Img_h = size_h

    # # 重新设置子图的尺寸
    # icon = S_Img.resize((S_Img_w, S_Img_h), Image.ANTIALIAS)
    icon = S_Img.resize((S_Img_w, S_Img_h), Image.ANTIALIAS)
    w = int((M_Img_w - S_Img_w) / 2)
    h = int((M_Img_h - S_Img_h) / 2)


    coordinate = (w, h)
    # 粘贴子图到母图的指定坐标（当前居中）
    M_Img.paste(icon, coordinate, mask=None)

    # 保存图片
    M_Img.save(save_img)


def Center(origin_img, save_img):
    '''
    只针对黑底图片
    :param origin_img: 初始图片路径
    :param save_img: 保存后图片路径
    :return:
    '''
    # Load image as grayscale (since it's b&w to start with)
    image = Image.open(origin_img)
    img_arr = np.array(image).astype(np.float)
    crop = img_arr



    back_ground = np.zeros((240, 240), dtype=np.uint8)

    Picture_Synthesis(back_ground, crop, save_img)


if __name__ == '__main__':
    # test_dir = './301jpg2'
    test_dir = 'G:\Brain_tumor\other_jpg'


    test_dir_list = []
    test_dir_path_list = []

    count_test = 0

    for root, dirs, files in os.walk(test_dir):
        if count_test != 0:
            break
        for dir in dirs:
            # 获取目录的名称
            test_dir_list.append(dir)
            test_dir_path_list.append(os.path.join(root, dir))
        count_test += 1

    for idx, param in enumerate(tqdm(test_dir_path_list)):# 将测试集进行裁切 例如进入TCGA-02-0006

        for root, dirs, files in os.walk(param):# 遍历此目录下的子目录
            for dir in dirs:
                if dir.find('GlistrBoost') != -1:
                    mask_image_path = dir
            for dir in dirs:
                if dir.find('GlistrBoost') != -1:
                    # 遍历到切分目录跳过
                    continue
                for root, dirs, files in os.walk(param+'\\'+dir):#遍历此子目录下的文件
                    count = 0
                    files_len = [i for i in range(len(files))]#files未按0 1 2 3顺序变为
                    for filename in files_len:
                        # mask_image_path目录下的文件与正在检索的目录下文件名称一致

                        if not os.path.exists('dataset\\' + param+'\\'+dir):
                            os.makedirs('dataset\\' + param+'\\'+dir)
                        Center(param+'\\'+dir+'\\'+str(filename)+'.jpg', 'dataset\\' + param+'\\'+dir+'\\'+str(count) + '.jpg')

                        count += 1
