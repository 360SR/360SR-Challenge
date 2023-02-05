import cv2
import os

if __name__ == '__main__':
    path = ''
    path_save = ''
    folder_list = os.listdir(path)
    for folder in folder_list:
        if os.path.exists(os.path.join(path_save,folder))==False:
            os.makedirs(os.path.join(path_save,folder))
        im_list = os.listdir(os.path.join(path,folder))[::10]
        for name in im_list:
            im = cv2.imread(os.path.join(path,folder,name))
            cv2.imwrite(os.path.join(path_save,folder,name), im)