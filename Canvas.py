from ctypes.wintypes import CHAR
from tkinter import Widget
import numpy as np
import os
import Donut

hight = 20
width = 20

dt_shape = Donut.step1 * Donut.step2

K = 200
z = 400

light_v = np.array([[1,-1,-1]]) / np.sqrt(3)
# light_str = [".,", "-~", "-+", "=!", "*#", "$@"]
light_str = [".,", "-~", "=!", "/%", "*#", "$@"]

def get_screen_x (n):
    x = K * n[0][0] // (K + n[2][0] + z)
    return x


def get_screen_y (n):
    y = K * n[1][0] // (K + n[2][0] + z)
    return y

def OutPut(n,v):
    pixel = np.zeros([hight,width],dtype=int)
    op = np.zeros([hight,width],dtype=int)
    minz = np.zeros([hight,width])
    for i in range (0,dt_shape):
        x = int (get_screen_x (n[i]) + hight / 2)
        y = int (get_screen_y (n[i]) + width / 2)
        lstr = 0
        pt = np.matmul(light_v,v[i])
        if pt > 0 :
            if pt < 0.259:
                lstr = 1
            elif pt < 0.5:
                lstr = 2
            elif pt < 0.707:
                lstr = 3
            elif pt < 0.867:
                lstr = 4
            elif pt < 0.966:
                lstr = 5
            elif pt < 1:
                lstr = 6
        if x < width and y< hight and x >= 0 and y >= 0:
            pixel [y][x] = 1

            if minz [y][x] == 0:
                minz [y][x] = n[i][2]
            if n[i][2] <= minz [y][x]:
                op [y][x] = lstr
                minz [y][x] = n[i][2]
    os.system ('cls')
    for y in range(0,hight):
        for x in range(0,width):
            if pixel [y][x] == 1 and op [y] [x] > 0:
                print (light_str[op [y] [x] - 1],end="")
            else:
                print ("  ",end = "")
        print ("")



