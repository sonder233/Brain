from nibabel.viewers import OrthoSlicer3D
from nibabel import nifti1
import nibabel as nib
from matplotlib import pylab as plt
import matplotlib
import numpy as np
import os
example = 'G:\\深度学习\\301samp\\chenjinfeng\\t1.nii'

example_filename = r'G:\深度学习\301samp_后20\huozengyu\t2.nii'


def show_one_file(example_filename):
    img = nib.load(example_filename)

    # shape不一定只有三个参数，打印出来看一下
    width, height, queue = img.dataobj.shape

    # 计算看需要多少个位置来放切片图
    x = int((queue / 10) ** 0.5) + 1
    print(img.dataobj.shape)
    num = 1
    # 按照10的步长，切片，显示2D图像
    for i in range(0, queue, 10):
        img_arr = img.dataobj[:, :, i]
        # img_arr = np.transpose(img_arr, (1, 0))
        # img_2d = np.transpose(img_2d, (1, 0))
        plt.subplot(x, x, num)
        plt.imshow(img_arr, cmap='gray')
        num += 1

    plt.show()

show_one_file(example_filename)