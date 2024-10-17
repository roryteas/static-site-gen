import os
import shutil


def copy_dir_to_dir(dir1,dir2): 
    if not os.path.exists(dir2):
        print(f"making directory {dir2}")
        os.mkdir(dir2)
    for item in os.listdir(dir1):
          
        if os.path.isfile(os.path.join(dir1,item)):
            print(f"copying {dir1}/{item} to {dir2}/{item}")
            shutil.copy(os.path.join(dir1,item),os.path.join(dir2,item))
        else:
            copy_dir_to_dir(os.path.join(dir1,item),os.path.join(dir2,item))


def recursive_delete_dir(dir):
    item_list = os.listdir(dir)
    for item in item_list:
        if os.path.isfile(os.path.join(dir,item)):
            print(f'deleting {dir}/{item} file')
            os.remove(os.path.join(dir,item))
        else:
            print(f'deleting {dir}/{item} directory and contents')
            shutil.rmtree(os.path.join(dir,item))

