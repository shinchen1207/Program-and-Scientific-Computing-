# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:20:07 2021

@author: joyce
"""

#hw2b.py
fo = open('hw2b.txt', 'w+')
fo.write('P[hPa] Theta[K] Q[g/kg]\n')



foReadData=open('hw2_data.txt', 'r')

Pass1=foReadData.readline()
Pass2=foReadData.readline()
Pass3=foReadData.readline()
Pass4=foReadData.readline()

for i in range(32):
    all=foReadData.readline()
    data=all.split()
    out=float(data[0])
    if out>=500:
        P=float(data[0])
        Theta=float(data[2])
        if float(data[1])<10:
            Q=" "+data[1]
        else:
            Q=data[1]
        fo.write('%6.1f  %6.3f   %s\n'%(P,Theta,Q))
fo.close()
foReadData.close()


