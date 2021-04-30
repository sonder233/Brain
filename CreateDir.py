import os

def walkFile(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            # print(os.path.join(root, dir))
            temp = os.path.join(root, dir)
            os.makedirs(temp.replace('301registration_jpg','301registration_max'))
    pass
    # 定义一个列表，用来存储结果
    # list = []
    # # 判断路径是否存在
    # if (os.path.exists(path)):
    #     # 获取该目录下的所有文件或文件夹目录
    #     files = os.listdir(path)
    #     for file in files:
    #         # 得到该文件下所有目录的路径
    #         m = os.path.join(path, file)
    #         # 判断该路径下是否是文件夹
    #         if (os.path.isdir(m)):
    #             h = os.path.split(m)
    #             # print('G:\\深度学习\\dataset_max\\test_max\\'+h[1])
    #             os.makedirs('G:\\Brain_tumor\\other_max\\'+h[1])
    #             list.append(h[1])
    #     print(list)


def main():
    walkFile(r'G:\Brain_tumor\301配准完毕\dataset\301registration_jpg')
    pass


if __name__ == '__main__':
    main()
