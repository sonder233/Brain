from nibabel.viewers import OrthoSlicer3D
from nibabel import nifti1
import nibabel as nib
from matplotlib import pylab as plt
import matplotlib
import numpy as np
import os

# 文件名，nii或nii.gz
# example_filename = 'G:\\深度学习\\301samp\\GUJUN\\flair.nii'
example_filename = 'G:\\深度学习\\brain_result\\example_save.nii'


def show_one_file(example_filename):
    img = nib.load(example_filename)

    # shape不一定只有三个参数，打印出来看一下
    width, height, queue = img.dataobj.shape

    # 计算看需要多少个位置来放切片图
    x = int((queue / 10) ** 0.5) + 1
    print(x)
    num = 1
    # 按照10的步长，切片，显示2D图像
    for i in range(0, queue, 10):
        img_arr = img.dataobj[:, :, i]
        img_arr = np.transpose(img_arr, (1, 0))
        # img_2d = np.transpose(img_2d, (1, 0))
        plt.subplot(x, x, num)
        plt.imshow(img_arr, cmap='gray')
        num += 1

    plt.show()

def change_orientation(filename):
    img = nib.load(example_filename)

    # shape不一定只有三个参数，打印出来看一下
    width, height, queue = img.dataobj.shape

    # 计算看需要多少个位置来放切片图
    x = int((queue / 10) ** 0.5) + 1
    print(x)
    num = 1
    # 按照10的步长，切片，显示2D图像
    for i in range(0, queue, 10):
        img_arr = img.dataobj[:, :, i]
        img_arr = np.transpose(img_arr, (1, 0))
        # img_2d = np.transpose(img_2d, (1, 0))
        plt.subplot(x, x, num)
        plt.imshow(img_arr, cmap='gray')
        num += 1

    plt.show()


def change_orien(f_path, s_path):
    nii_img = nib.load(f_path)
    nii_data = nii_img.get_fdata()
    new_data = nii_data.copy()

    result_data = new_data.transpose(1, 0, 2)
    print(result_data.shape)

    #print(new_data)
    print(new_data.shape)

    affine = nii_img.affine.copy()
    hdr = nii_img.header.copy()

    # 形成新的nii文件
    new_nii = nib.Nifti1Image(result_data, affine, hdr)

    # 保存nii文件，后面的参数是保存的文件名
    nib.save(new_nii, s_path)
    pass


if __name__ == '__main__':
    # show_one_file(example_filename)
    file_path = 'G:\\深度学习\\301samp_changed'
    for root, dirs, files in os.walk(file_path, topdown=False):
        for name in files:
            # 文件本身的路径+文件名（带后缀）
            f_path = os.path.join(root, name)
            print(f_path)
            # 需要存储的路径+文件名（带后缀）
            sava_path = f_path.replace('301samp', '301samp_changed')

            #change_orien(f_path, sava_path)
            img_path = os.path.join(root, name)
        # for name in dirs:
        #     print(os.path.join(root, name))

    pass
