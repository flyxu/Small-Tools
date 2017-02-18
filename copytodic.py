import shutil
import os
path='/Users/xufly/Project/PythonProject/Keras_Learning/PX_train_dataset/'
for file in os.listdir(path):
    filepath=path+file
    if 'tad_f0' in filepath:
        shutil.copy(filepath, '/Users/xufly/Desktop/SPIE_tad/f0/')
    elif 'tad_f1' in filepath:
        shutil.copy(filepath, '/Users/xufly/Desktop/SPIE_tad/f1/')
    else:
        pass
#shutil.copy('/Users/xufly/Project/PythonProject/Keras_Learning/PX_train_dataset/PX001_L1_tad_f0_zA_rotijk0_0_0_sft0_0_0.png','/Users/xufly/Desktop/SPIE_tad/f0/')

