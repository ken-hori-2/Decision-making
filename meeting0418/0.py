import random

from torch import randint

import numpy as np

List = [0.5,0.6,0.7,0.8,0.9,1.0, 1.5]

List_sub = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
sub = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    sub[i] = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])
print('sub:{}\n'.format(sub))


sNumbers = [0, 0, 0, 0]
sNumbers2 = [0, 0, 0, 0]

retry = 0
retry_SUM = 0
LM = 0
SUM = 0
diff = [0, 0, 0, 0]

for x in range(4):
    
    List2 = [1, 0]

    print('{}回目'.format(x+1))

    for i in range(100):
        
        LM = np.random.choice(List2, 1, p=[0.5, 0.5])
        print('LM = {}'.format(LM))
            
        if LM == 1:
            print('発見')
            
            print('やり直し回数：{}'.format(retry))
            # sNumbers2[x] = np.random.choice(List, 1, p=[0.10,0.10,0.20,0.20,0.20,0.10, 0.10])
            sNumbers2[x] = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])   

            diff[x] = abs(1.0 - sNumbers2[x])



            print(sNumbers2[x],diff[x])
            SUM += diff[x]
            if SUM >= 0.5:
                print('sum:{} 疑念!!!!!!!\n'.format(SUM))
                if diff[x] >= 0.2:
                    print('アーク:{} !!!!!!!!!!!!\n'.format(diff[x]))
            break
        else:
            if SUM >= 0.5:
                print('疑念0.5以上\n')
                # if diff[x] >= 0.2:
                #     print('!!!!!!!!!!!!')
            else:
                print('リセット')
            
            retry += 1

    retry_SUM += retry        
    retry = 0

    
    # SUM += diff[x]

    
    
    
    print('sNumbers:{}'.format(sNumbers2))
    print('ズレ:{}'.format(diff))
    

print('\n総和　SUM:{}'.format(SUM))

print('やり直し総回数:{}'.format(retry_SUM))