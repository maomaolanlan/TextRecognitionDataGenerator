# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:56:17 2018
需要运行两次获得正确的colour.txt文件
@author: hubinbin
"""
import os
import numpy as np
from PIL import Image

pictures_path = os.listdir('Font_colour\\img')
color_array=np.zeros((len(pictures_path),3),dtype=int)

DataLirary = {}
for index,picture_path in enumerate(pictures_path):
    picture = Image.open(os.path.join('Font_colour\\img',picture_path))
    r, g, b,alpha=picture.split()
    
    r_=r.getpixel((0,0))
    g_=g.getpixel((0,0))
    b_=b.getpixel((0,0))
    if (r_, g_, b_) in DataLirary:
        print('remove:'+picture_path)
        os.remove(os.path.join('Font_colour\\img',picture_path))       
    else:
        dict2 = {(r_, g_, b_):picture_path}
        DataLirary.update(dict2)
        color_array[index,:]=[r_, g_, b_]

f=open(os.path.join('Font_colour','colour.txt'),'w')
for index,(r,g,b) in enumerate(color_array):
    f.write(pictures_path[index]+' '+str(r)+' '+str(g)+' '+str(b)+'\n')
f.close()