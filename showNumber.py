import nibabel as nib
import numpy as np


def compute_orientation(init_axcodes, final_axcodes):
    """
    A thin wrapper around ``nib.orientations.ornt_transform``

    :param init_axcodes: Initial orientation codes
    :param final_axcodes: Target orientation codes
    :return: orientations array, start_ornt, end_ornt
    """
    ornt_init = nib.orientations.axcodes2ornt(init_axcodes)
    ornt_fin = nib.orientations.axcodes2ornt(final_axcodes)

    ornt_transf = nib.orientations.ornt_transform(ornt_init, ornt_fin)

    return ornt_transf, ornt_init, ornt_fin


def do_reorientation(data_array, init_axcodes, final_axcodes):
    """
    source: https://niftynet.readthedocs.io/en/dev/_modules/niftynet/io/misc_io.html#do_reorientation
    Performs the reorientation (changing order of axes)

    :param data_array: 3D Array to reorient
    :param init_axcodes: Initial orientation
    :param final_axcodes: Target orientation
    :return data_reoriented: New data array in its reoriented form
    """
    ornt_transf, ornt_init, ornt_fin = compute_orientation(init_axcodes, final_axcodes)
    if np.array_equal(ornt_init, ornt_fin):
        return data_array

    return nib.orientations.apply_orientation(data_array, ornt_transf)


# I test the code by the following simple demo, and it works.

lits_path = 'G:\\深度学习\\t12.nii'
kits_path = 'G:\\深度学习\\t12.nii'

wrong = 'G:\\深度学习\\t1.nii'
save_path = 'G:\\深度学习\\t12.nii'

lits_nii = nib.load(lits_path)
lits_data = lits_nii.get_fdata()  # shape = (512, 512, 123)
lits_axcodes = tuple(nib.aff2axcodes(lits_nii.affine))  # ('R', 'A', 'S')
kits_nii = nib.load(kits_path)
kits_data = kits_nii.get_fdata()  # shape = (100, 523, 523)
kits_axcodes = tuple(nib.aff2axcodes(kits_nii.affine))  # ('I', 'P', 'L')

new_kits_img = do_reorientation(kits_data, kits_axcodes, lits_axcodes)  # shape = (523, 523, 100)
new_lits_img = do_reorientation(lits_data, lits_axcodes, kits_axcodes)  # shape = (123, 512, 512)

example_filename = 'G:\\深度学习\\301samp\\chenjinfeng\\t1.nii'

nii_img = nib.load(example_filename)

affine = nii_img.affine.copy()
hdr = nii_img.header.copy()

# 形成新的nii文件
new_nii = nib.Nifti1Image(new_kits_img, affine, hdr)

# 保存nii文件，后面的参数是保存的文件名
nib.save(new_nii, save_path)