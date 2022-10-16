import numpy as np
import Rotation_matrix as Rm
import Donut
import Canvas as cv
import time

dt_shape = Donut.step1 * Donut.step2


k = 1

T = 240
T2 = 240

# x = np.array ([[1],[2],[3]])
# y = np.matmul(Rm.Ry(np.pi),x)
# a = list ([x,y])
# x.transpose()
donut,Normal_vector = Donut.get_donut ()
print (Normal_vector[2])

cv.OutPut(donut,Normal_vector)
for t in range(0,T):
        # donut = Donut.get_donut ()
        start = time.perf_counter()
        if t < T/2:
                for i in range(0,dt_shape):
                        # donut[i] = donut[i] - Donut.displacement_mat
                        donut[i] = np.matmul(Rm.Ry(4 * np.pi / T),donut[i])
                        Normal_vector [i] = np.matmul(Rm.Ry(4 * np.pi /T),Normal_vector [i])
                        # donut[i] = donut[i] + Donut.displacement_mat
        else:
                for i in range(0,dt_shape):
                        # donut[i] = donut[i] - Donut.displacement_mat
                        donut[i] = np.matmul(Rm.Rx(4 * np.pi /T),donut[i])
                        Normal_vector [i] = np.matmul(Rm.Rx(4 * np.pi /T),Normal_vector [i])
                        # donut[i] = donut[i] + Donut.displacement_mat
        cv.OutPut(donut,Normal_vector)
        if t % 5 == 0 :
                end = time.perf_counter()
                fps = 1 / (end - start)
        print ("fps=",fps)
        # time.sleep(fps/k)
for t in range(0,T2):
        start = time.perf_counter()
        for i in range(0,dt_shape):
                        # donut[i] = donut[i] - Donut.displacement_mat
                        donut[i] = np.matmul(Rm.Rx(2 * np.pi /T2),donut[i])
                        donut[i] = np.matmul(Rm.Ry(-2 * np.pi /T2),donut[i])
                        Normal_vector [i] = np.matmul(Rm.Rx(2 * np.pi / T2),Normal_vector [i])
                        Normal_vector [i] = np.matmul(Rm.Ry(-2 * np.pi / T2),Normal_vector [i])
                        # donut[i] = donut[i] + Donut.displacement_mat
        cv.OutPut(donut,Normal_vector)
        if t % 5 == 0 :
                end = time.perf_counter()
                fps = 1 / (end - start)
        print ("fps=",fps)
        # time.sleep(fps/k)



 