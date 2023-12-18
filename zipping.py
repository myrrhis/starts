import glob
from zipfile import ZipFile

def zip_selected_ext(name, ext):
    result = glob.glob(f'*.{ext}')
    with ZipFile(f'{name}.zip', 'w') as testzip:
        for i in result:
            testzip.write(i)
