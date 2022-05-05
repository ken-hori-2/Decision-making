import random

from torch import randint

import numpy as np

List = [0.5,0.6,0.7,0.8,0.9,1.0, 1.5]
sNumbers = [0, 0, 0, 0]
for i in range(4):
    # sNumbers[i] = np.random.choice(List, 1, p=[0.10,0.15,0.20,0.25,0.20,0.10])
    sNumbers[i] = np.random.choice(List, 1, p=[0.10,0.10,0.20,0.20,0.20,0.10, 0.10])
print('sNumber:{}'.format(sNumbers))

x0 = 0
x1 = round(0.0,10)
x2 = round(0.0, 10)
X = [0, 0, 0, 0]

retry = 0
LM = 0
SUM = 0

for x in range(4):
    # for i in range(10):
    # List = [True, False]
    List2 = [1, 0]
    # LM = np.random.choice(List2, 1, p=[0.3, 0.7])
    # print('LM = {}'.format(LM))
    # while LM == 0:
        
    for i in range(100):
        x1 += round(0.10,1)
        #if a[x1] == 1:
        x1 = round(x1,1)
        print('x1={},{}回目'.format(x1,i+1))


        if sNumbers[x] <= x1:
            if sNumbers[x] >= 1.5:
                print('認知距離内では未発見')
                # x2 = round(1.0 - x1, 1)
                x2 = round(1.0, 1) #2.0
                X[x] = x2
                x0 = 0
                x1 = 0
                break
            a_lm = 1
            x0 = 1

            # x1 = round(x1,1)
            print('x1 = {}'.format(x1))
            # print('発見')

        if x0 == 1:
            x2 = 1.0 - x1
            x2 = round(x2,1)
            print('基準距離とのズレ:{}'.format(x2))

            LM = np.random.choice(List2, 1, p=[0.5, 0.5])
            print('LM = {}'.format(LM))
            
            if LM == 1:
                print('発見\n')
                x0 = 0
                x1 = 0
                X[x] = x2
                print('やり直し回数：{}\n'.format(retry))
                break
            else:
                print('リセット\n')
                x0 = 0
                x1 = 0
                retry += 1
                # i = 0

    SUM += X[x]

    SUM = round(SUM,1)
    
    # x0 = 0
    # x1 = 0
    # X[x] = x2
    print('sNumbers:{}'.format(sNumbers))
    print('ズレ　X[{}]:{}'.format(x,X[x]))
    print('ズレ　X:{}'.format(X))

    print('\nズレ　SUM:{}'.format(SUM))