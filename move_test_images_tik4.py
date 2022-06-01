# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:06:46 2021

@author: ridvan

find and move files 
"""

import shutil
import os

folder_kalacak = "E:/ridvan_2021/05_PhD/tik_ler/tik_3/kalacak/"
folder_rcb_unrotate = "E:/ridvan_2021/05_PhD/tik_ler/tik_3/RCB_unrotate/"
#bu klasör içindeki dosyaların isimlerini al
folder_test = "E:/ridvan_2021/05_PhD/tik_ler/tik_4/out_f20k_ele/"

#bu klasörden kes
folder_rfd_v3 = "E:/ridvan_2021/05_PhD/tik_ler/tik_4/in/"
#bu klasöre yapıştır
folder_test3 = "E:/Yolo_v4/darknet/build/darknet/x64/data/pseudo/"
folder_rfd_v2 = "E:/ridvan_2021/05_PhD/tik_ler/tik_3/R_F_D_v2/"


for filename in os.listdir(folder_test):
    img_path = os.path.join(folder_rfd_v3,filename)
    hedef_1= os.path.join(folder_test3,filename)
    
    #txtname= filename[:-3]+"txt"
    #img_path_txt = os.path.join(folder_rfd_v3,txtname)
    #hedef_1_txt= os.path.join(folder_test3,txtname)
    
    try:
        #move jpg files
        shutil.move(img_path, hedef_1)
        # copy txt files 
        #shutil.move(img_path_txt, hedef_1_txt)
    except FileNotFoundError:
        print("dosya bulunamadı")

    
    
