import numpy as np

def Rx (i) -> np.array:
    R = np.array([
                [1, 0, 0], 
                [0, np.cos(i), -np.sin(i)],
                [0, np.sin(i), np.cos(i)]
                ])
    return R

def Ry (i) -> np.array: 
    R = np.array([
                [np.cos(i), 0, np.sin(i)], 
                [0, 1, 0],
                [-np.sin(i), 0, np.cos(i)]
                ])
    return R

def Rz (i) ->np.array:
    R = np.array([
                [np.cos(i), -np.sin(i), 0], 
                [np.sin(i), np.cos(i), 0], 
                [0, 0, 1]
                ])
    return R