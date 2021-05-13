# 需求：封装函数，获取一个指定目录下的所有的内容，如果是文件，则直接打印，如果是文件夹，则继续查找
import os


def getAllFile(path):
    if not os.path.exists(path):
        print("路径不存在，无法操作")
        return
    if os.path.isfile(path):
        print("路径是一个文件：%s" % path)
        return

    filelist = os.listdir(path)
    # 遍历
    for fileName in filelist:
        # 拼接路径
        filePath = os.path.join(path, fileName)
        # 判断是否是文件
        if os.path.isdir(filePath):
            # 目录，继续访问
            print("目录: %s" % filePath)
            # 使用递归
            getAllFile(filePath)
        else:
            print("文件 : %s " % filePath)


if __name__ == '__main__':
    path = "E:\python3_code"  # 指定目录
    getAllFile(path)
