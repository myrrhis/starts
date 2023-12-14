import os
import glob

def files_list(top, extension, flag=False):
    result = []
    result += glob.glob('*.py')

    if flag:
        dirs = [i for i in os.listdir(top) if os.path.isdir(i)]
        for i in dirs:
            result += glob.glob((os.path.join(i, '*.py')))

    return result

def remdir(dir):
    dirs = [i for i in os.listdir(dir) if os.path.isdir(i)]
    if dirs:
        return 'Unsuccess removing'
    for file in os.listdir(dir):
        os.remove(os.path.join(dir, file))
    os.rmdir(dir)
    return 'Success removing'
  
