import numpy as np
import Rotation_matrix as Rm

# displacement_mat = np.array([[0],[0],[300]])

R1 = 20
R2 = 10

step1 = 32
step2 = 64

def get_donut ():
    donut = list (range(0,step1 * step2))
    Normal_vector = list (range(0,step1 * step2))
    cle = list(range(0,step1))
    cle_nv = list(range(0,step1))
    for j in range (0,step1):
        a = 2 * (j + 1) * np.pi / step1
        dot = np.array ([
                        [0],
                        [R1+ R2 * np.cos(a)],
                        [R2 * np.sin(a)]
                        ])
        nv = np.array ([
                        [0],
                        [np.cos(a)],
                        [np.sin(a)]
                        ])
        cle [j] = dot
        cle_nv [j] = nv
        
    for i in range(0,step2):
        b = 2 *  (i + 1) * np.pi / step2
        cle2 = list (range(0,step1))
        cle_nv2 = list (range(0,step1))
        for j in range (0,step1):
            cle2 [j] = np.matmul(Rm.Rz (b),cle[j])
            cle_nv2[j] = np.matmul(Rm.Rz (b),cle_nv[j])
            donut[step1 * i + j] = cle2 [j]
            Normal_vector [step1 * i + j] = cle_nv2[j]
    return donut,Normal_vector
    # for i in range (0,step2):
    #     b = 2 *  (i + 1) * np.pi / step2
    #     for j in range (0,step1):
    #         a = 2 * (j + 1) * np.pi / step1
    #         dot = np.array ([
    #                         [R1 * np.cos(b) + R2 * np.cos(a) * np.cos(b)],
    #                         [R2 * np.sin(a)],
    #                         [-(R1 * np.sin(b) + R2 * np.cos(a) * np.cos(b))]
    #                         ])
    #         donut [step1 * i + j] = dot
    # return donut