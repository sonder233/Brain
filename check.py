from nibabel.viewers import OrthoSlicer3D
from nibabel import nifti1
import nibabel as nib
from matplotlib import pylab as plt
import matplotlib
import numpy as np
from nilearn.image import new_img_like,resample_to_img
import os

# 文件名，nii或nii.gz
example_filename = 'G:\\深度学习\\301samp\\chenjinfeng\\t1.nii'
wrong = r'G:\深度学习\301samp_后20\huozengyu\t2.nii'
save_path = 'G:\\深度学习\\t3.nii'

def flip_image(image, axis):
    try:
        new_data = np.copy(image.get_fdata())
        for axis_index in axis:
            #根据axis对image数组进行翻转
            new_data = np.flip(new_data, axis=axis_index)
    except TypeError:
        new_data = np.flip(image.get_fdata(), axis=axis)

    affine = image.affine.copy()
    hdr = image.header.copy()

    # 形成新的nii文件
    new_nii = nib.Nifti1Image(new_data, affine, hdr)
    # return new_img_like(image, data=new_data)
    return new_nii

img = nib.load(example_filename)
#print(img.shape)
nii_img = nib.load(wrong)
nii_data = img.get_fdata()
new_data = nii_data.copy()
new_data = new_data[::-1]  # 沿x轴反转
# new_data = new_data[:, ::-1]  # 沿y轴反转


# new_image2=flip_image(img,axis=[2])

#result_data = new_data.transpose(2,1,0)

#print(new_image2)
print(new_data.shape)

#print(new_data)
#print(new_data.shape)
#
affine = nii_img.affine.copy()
hdr = nii_img.header.copy()

# 形成新的nii文件
new_nii = nib.Nifti1Image(new_data, affine, hdr)

# 保存nii文件，后面的参数是保存的文件名
nib.save(new_nii, save_path)

def show_one_file(save_path):
    img = nib.load(save_path)

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

show_one_file(save_path)

#
#
#
#
# # 打印文件信息
# print(img)
# print(type(img))
# print(img.dataobj.shape)
# # img_change = np.transpose(img, (1, 0, 2))
# # img_2 = np.swapaxes(img,0,1)
# # nib.save(img, os.path.join(save_path, 'test.nii'))
#
# img = nib.load(example_filename)
# # shape不一定只有三个参数，打印出来看一下 (201, 230, 126)
# width, height, queue = img.dataobj.shape
#
# # 计算看需要多少个位置来放切片图
# x = int((queue / 10) ** 0.5) + 1
# num = 1
# # 按照10的步长，切片，显示2D图像
#
#
# def show_one_file(img):
#     # shape不一定只有三个参数，打印出来看一下
#     width, height, queue = img.dataobj.shape
#
#     # 计算看需要多少个位置来放切片图
#     x = int((queue / 10) ** 0.5) + 1
#     print(x)
#     num = 1
#     # 按照10的步长，切片，显示2D图像
#     for i in range(0, queue, 10):
#         img_arr = img.dataobj[:, :, i]
#         #img_arr = np.transpose(img_arr, (1, 0))
#         # img_2d = np.transpose(img_2d, (1, 0))
#         plt.subplot(x, x, num)
#         plt.imshow(img_arr, cmap='gray')
#         num += 1
#
#     plt.show()
#
# show_one_file(img)
#


