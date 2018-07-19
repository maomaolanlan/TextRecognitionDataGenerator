# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:45:20 2018

@author: hubinbin
"""
import  codecs

DataSet_1 = set()
DataSet_2 = set()
f=codecs.open('Lipi.txt','r', encoding='utf-8')
line = f.readline()
while line:
    line=line.strip()
    if len(line):
        if line in DataSet_1:
            print('remove: '+line)      
        else:
            DataSet_1.add(line)
        DataSet_2.update(line)
    line = f.readline()
f.close()

f=codecs.open('Lipi_1.txt','w', encoding='utf-8')
for line in sorted(DataSet_1):
    f.write(line+'\n')
f.close()

f=codecs.open('Lipi_char.txt','w', encoding='utf-8')
for ch in sorted(DataSet_2):
    f.write(ch+'\n')
f.close()