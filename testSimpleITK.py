import SimpleITK as sitk
itk_img = sitk.ReadImage('G:\\深度学习\\301samp\\GUJUN\\flair.nii')
img = sitk.GetArrayFromImage(itk_img)
print("img shape:",img.shape)