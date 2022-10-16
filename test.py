from manimlib import *
import numpy as np


class MyScene (Scene):
    def construct(self):
        
        R1 = 3
        R2 = 1.75

        step1 = 4
        step2 = 32
        def Rz (i) ->np.array:
            R = np.array([
                        [np.cos(i), -np.sin(i), 0], 
                        [np.sin(i), np.cos(i), 0], 
                        [0, 0, 1]
                        ])
            return R
        def get_donut ():
            donut = list (range(0,step1 * step2))
            cle = list(range(0,step1))
            for j in range (0,step1):
                a = 2 * (j + 1) * np.pi / step1
                dot = np.array ([
                                [0],
                                [R1+ R2 * np.cos(a)],
                                [R2 * np.sin(a)]
                                ])
                cle [j] = dot
            for i in range(0,step2):
                b = 2 *  (i + 1) * np.pi / step2
                cle2 = list (range(0,step1))
                for j in range (0,step1):
                    cle2 [j] = np.matmul(Rz (b),cle[j])
                    donut[step1 * i + j] = cle2 [j]
            return donut

            # for i in range (0,step2):
            #     b = 2 *  (i + 1) * np.pi / step2
            #     for j in range (0,step1):
            #         a = 2 * (j + 1) * np.pi / step1
            #         # dot = np.array ([
            #         #                 [R1 * np.cos(b) + R2 * np.cos(a) * np.cos(b)],
            #         #                 [R2 * np.sin(a)],
            #         #                 [-(R1 * np.sin(b) + R2 * np.cos(a) * np.cos(b))]
            #         #                 ])
            #         dot = np.array ([
            #                         [-(R1 * np.sin(b) + R2 * np.cos(a) * np.cos(b))],
            #                         [R1 * np.cos(b) + R2 * np.cos(a) * np.cos(b)],
            #                         [R2 * np.sin(a)]
            #                         ])
            #         donut [step1 * i + j] = dot
            # return donut

        donut = get_donut ()
        dot = VGroup()
        for i in range (0,step1 * step2):
            dot1 = Dot ()
            dot.move_to (np.transpose(donut[i]))
            dot = VGroup (dot,dot1)
        dot.move_to (np.array([0,0,0]))
        self.add (dot)