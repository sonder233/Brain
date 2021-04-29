from PIL import Image
import os
from tqdm import tqdm
import numpy as np


def nidus_cut(origin_image_path, save_image_path, name, mask_image_path):
    # 原始图片地址，保存地址，病灶切分地址
    mask_image = Image.open(mask_image_path)
    mask_image_arr = np.array(mask_image) > 35
    origin_image = Image.open(origin_image_path)
    origin_image_arr = np.array(origin_image)
    origin_image_arr[mask_image_arr == False] = 0
    # 原始图片切分
    im = Image.fromarray(origin_image_arr)
    if not os.path.exists('dataset\\'+save_image_path):
        os.makedirs('dataset\\'+save_image_path)

    im.save('dataset\\'+save_image_path+'\\'+name)


if __name__ == '__main__':
    test_dir = '../301at'
    # 这里输入你的要切分的地址文件夹
    # |----要输入文件夹
    #   |--人名
    #     |--flair
    #     |--t1

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


    '''
    GlistrBoost为分割方块文件夹，分割方块命名为mask
    '''
    for idx, param in enumerate(tqdm(test_dir_path_list)):# 将测试集进行裁切 例如进入TCGA-02-0006
        count = 1
        for root, dirs, files in os.walk(param):# 遍历此目录下的子目录
            for dir in dirs:
                if dir.find('GlistrBoost') != -1:
                    mask_image_path = dir
            for dir in dirs:
                if dir.find('GlistrBoost') != -1:
                    # 遍历到切分目录跳过
                    continue
                for root, dirs, files in os.walk(param+'\\'+dir):#遍历此子目录下的文件
                    files_len = [i for i in range(len(files))]#files未按0 1 2 3顺序变为
                    for filename in files_len:
                        # mask_image_path目录下的文件与正在检索的目录下文件名称一致
                        nidus_cut(param+'\\'+dir+'\\'+str(filename)+'.jpg', param+'\\'+dir, str(filename)+'.jpg', param+'\\'+mask_image_path+'\\'+'mask.jpg')
                        count += 1
