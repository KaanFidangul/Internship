# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:15:31 2021

@author: Kaan
"""

import serial

try:
    arduino = serial.Serial("COM3", timeout = 1)
except:
    print("Please check the port")
    
rawdata = []
count =0

while count <16:
    rawdata.append(str(arduino.readline()))
    count += 1
print(rawdata)

def clean(L):
    newl = []
    for i in range(len(L)):
        temp = L[i][2:]
        newl.append(temp[:-5])
    return newl

cleandata = clean(rawdata)

def write(L):
    file = open("dataTips.txt", mode = 'w')
    for i in range(len(L)):
            file.write(L[i]+'\n')
        
    file.close()
    
write(cleandata)
