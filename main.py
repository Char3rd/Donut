import numpy as np
import Rotation_matrix as Rm
import Donut
import Canvas as cv
import time

dt_shape = Donut.step1 * Donut.step2


k = 1

T = 240
T2 = 240

donut,Normal_vector = Donut.get_donut ()
print (Normal_vector[2])

cv.OutPut(donut,Normal_vector)
for t in range(0,T):
        start = time.perf_counter()
        if t < T/2:
                for i in range(0,dt_shape):
                        donut[i] = np.matmul(Rm.Ry(4 * np.pi / T),donut[i])
                        Normal_vector [i] = np.matmul(Rm.Ry(4 * np.pi /T),Normal_vector [i])
        else:
                for i in range(0,dt_shape):
                        donut[i] = np.matmul(Rm.Rx(4 * np.pi /T),donut[i])
                        Normal_vector [i] = np.matmul(Rm.Rx(4 * np.pi /T),Normal_vector [i])
        cv.OutPut(donut,Normal_vector)
        if t % 5 == 0 :
                end = time.perf_counter()
                fps = 1 / (end - start)
        print ("fps=",fps)
for t in range(0,T2):
        start = time.perf_counter()
        for i in range(0,dt_shape):
                        donut[i] = np.matmul(Rm.Rx(2 * np.pi /T2),donut[i])
                        donut[i] = np.matmul(Rm.Ry(-2 * np.pi /T2),donut[i])
                        Normal_vector [i] = np.matmul(Rm.Rx(2 * np.pi / T2),Normal_vector [i])
                        Normal_vector [i] = np.matmul(Rm.Ry(-2 * np.pi / T2),Normal_vector [i])
        cv.OutPut(donut,Normal_vector)
        if t % 5 == 0 :
                end = time.perf_counter()
                fps = 1 / (end - start)
        print ("fps=",fps)


 
