import os
import sys

path = '/Users/xufly/SPIECompetition/PX_Images_Test_DCE/'

for file in os.listdir(path):
    oldpath = os.path.join(path, file)
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    print filename
    baoliu = filename.split('-')[1][1:4]
    newfilename = 'PX' + baoliu + '_DCE' + filetype
    newpath = os.path.join(path, newfilename)
    os.rename(oldpath, newpath)
print 'ok'
