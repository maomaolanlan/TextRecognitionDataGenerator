# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:24:53 2018

@author: hubinbin
"""
import os
import sys
import  codecs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './TextRecognitionDataGenerator')))

from TextRecognitionDataGenerator.data_generator import FakeTextDataGenerator

# 生产图片输出路径
out_path = 'Lipi\\out'
# 字体文件路径
fonts_path = 'Lipi\\Font'
# 背景图片路径
backgrounds_path='Lipi\\Font_background\\img'
# 字体颜色文件
font_colour_path=os.path.join('Lipi\\Font_colour','colour.txt')
# 生产图片所需文本信息
txt_path='Lipi\\Lipi_1.txt'

# 判断当前字符串是否包含中文字符
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def main():
    try:
        os.mkdir(out_path)
    except:
        pass
    
    #读取文字颜色信息和字体信息
    font_list = os.listdir(fonts_path)
    background_list = os.listdir(backgrounds_path)
    f=open(font_colour_path,'r')
    line = f.readline()
    color_list=[]
    while line:
        if len(line):
            tmp=line.split()[1:4]
            color_list.append((int(tmp[0]), int(tmp[1]), int(tmp[2]), 255))
        line = f.readline()
    f.close()
    
    #读取文本信息
    f=codecs.open(txt_path,'r', encoding='utf-8')
    strings=f.readlines()
    f.close()
    
    for index,string in enumerate(strings):
        save_path=os.path.join(out_path,str(index))
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        for i,font in enumerate(font_list):
            for j,color in enumerate(color_list):
                for k,background in enumerate(background_list):
                    if check_contain_chinese(string) and font != 'black3.OTF':
                        break
                    if not check_contain_chinese(string) and font == 'black3.OTF':
                        break
                    FakeTextDataGenerator.generate(
                        index=i*len(background_list)*len(color_list)+j*len(background_list)+k,
                        text=string,
                        font=os.path.join(fonts_path,font),
                        out_dir=save_path,
                        height =32,
                        extension='png',
                        skewing_angle=0,
                        random_skew=False,
                        blur=0,
                        random_blur=False,
                        background_type=3,
                        distorsion_type=2,
                        distorsion_orientation=1,
                        is_handwritten=False,
                        name_format=2,
                        text_color=color,
                        text_mode='RGBA',
                        background_path=os.path.join(backgrounds_path,background)
                    )

if __name__ == '__main__':
    main()