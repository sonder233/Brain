import os
import numpy as np
import nibabel as nib
import imageio
from tqdm import tqdm
import matplotlib
from nibabel.viewers import OrthoSlicer3D
from matplotlib import pylab as plt
import warnings

def read_niifile(niifilepath):  # 读取niifile文件
    img = nib.load(niifilepath)  # 下载niifile文件（其实是提取文件）
    img_fdata = img.get_fdata()  # 获取niifile数据
    return img_fdata


def save_fig(niifilepath, savepath):  # 保存为图片
    fdata = read_niifile(niifilepath)  # 调用上面的函数，获得数据
    (x, y, z) = fdata.shape  # 获得数据shape信息：（长，宽，维度-切片数量）
    for k in range(z):
        silce = fdata[:, :, k].transpose((1, 0))  # 三个位置表示三个不同角度的切片

        imageio.imwrite(os.path.join(savepath, '{}.jpg'.format(k)), silce)
        # 将切片信息保存为jpg格式


if __name__ == '__main__':
    savepath = r'G:\Brain_tumor\other_jpg'
    test_dir = r'G:\Brain_tumor\other'
    

    test_dir_list = []
    test_dir_path_list = []
   
    for root, dirs, files in os.walk(test_dir):
        for dir in dirs:
            # 获取目录的名称
            test_dir_list.append(dir)
            test_dir_path_list.append(os.path.join(root, dir))
    
    warnings.filterwarnings("ignore")
    for idx, param in enumerate(tqdm(test_dir_path_list)):#将训练集转为jpg保存
        for root, dirs, files in os.walk(param):
            for filename in files:
                testsavepath = savepath+'\\'+test_dir_list[idx]+'\\'+filename.rstrip('.nii')
                if not os.path.exists(testsavepath):
                    os.makedirs(testsavepath)
                save_fig(param+'\\'+filename, testsavepath)
    
    print('ok')



