# encoding:utf-8
import os


def makefile(path):
    for i in range(204,346):
        j = '%03d' % i
        filePath = path + 'PX' + str(j)
        if os.path.exists(filePath):
            print filePath + "目录已存在"
        else:
            os.mkdir(path + 'PX' + str(j))
            print '创建成功'


path = '/Users/xufly/SPIECompetition/PX_Images_Test_DCE/'
makefile(path)
