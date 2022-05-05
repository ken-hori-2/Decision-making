from unittest import result
import numpy as np
import matplotlib.pyplot as plt
import random

from numpy.core.defchararray import title
#from pyrsistent import T
from pytest import skip
from torch import ne

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言

# # 現在地S0に緑丸を描画する
# line, = ax.plot([2.5], [3.5], marker="o", color='g', markersize=30)
fig = plt.figure(figsize=(2, 7))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
plt.text(0.5, 4.5, 'Node\n(事前情報)', size=8, ha='center')
plt.text(0.5, 6.5, 'Node\n(事前情報)', size=8, ha='center')

plt.text(0.5, 1.3, 'Node', ha='center')
#plt.text(4.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 1)
ax.set_ylim(0, 9)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [0.5], marker="^", color='y', markersize=20)
line1, = ax.plot([0.5], [0.5], marker=">", color='r', markersize=20)
line2, = ax.plot([0.5], [0.5], marker=">", color='b', markersize=20)

# 初期の方策を決定するパラメータtheta_0を設定

# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[1, np.nan, np.nan, np.nan],  # s0
                    [1, np.nan, np.nan, np.nan],  # s1
                    [1, np.nan, np.nan, np.nan],  # s2
                    [1, np.nan, np.nan, np.nan],  # s3
                    [1, np.nan, np.nan, np.nan],  # s4
                    [1, np.nan, np.nan, np.nan],  # s5
                    [1, np.nan, np.nan, np.nan],  # s6

                    [1, np.nan, np.nan, np.nan],  # s7、※ LandMark

                    [1, np.nan, np.nan, np.nan]  #s8

                    ])

# 方策パラメータthetaを行動方策piに変換する関数の定義


def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''

    [m, n] = theta.shape  # thetaの行列サイズを取得
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # 割合の計算

    pi = np.nan_to_num(pi)  # nanを0に変換

    return pi


# 初期の方策pi_0を求める
pi_0 = simple_convert_into_pi_from_theta(theta_0)


# 初期の方策pi_0を表示
pi_0
# print(pi_0)
PI = pi_0

# 1step移動後の状態sを求める関数を定義

A = [0]*19
# A[8]=8
# A[15]=8

state_history = [8]  # エージェントの移動を記録するリスト

num=[3,2,1]
num=[3,1,1]
D = 0

import random
# r1 = random.randint(0,1)
# r2 = random.randint(0,1)
List_sub = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
# diff = [0, 0, 0, 0, 0, 0, 0, 0]
SUM = 0
# SUM_change = [0,0,0,0,0]
SUM_change = np.zeros(shape=(30))
# TEST = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Diff2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

TEST = np.zeros(shape=(30))
diff = np.zeros(shape=(30))
Diff2 = np.zeros(shape=(30))

def AAA(s,depth,i,j,S,S2,S3,S4,judge1,judge2,judge3,judge4, SUM):
    direction = ["up", "right", "down", "left"]
    
    #if A[s] == 8 or i > 30: #14:  # ゴール地点なら終了
    if s == 8 or i > 100:
        
        if SUM <= 0.5:
            print('\n疑念0.5以下')
            print('diff:{}'.format(diff))
            print('sum:{}\n'.format(SUM))
            print('j={} TEST = {}'.format(j,TEST))
            print('Diff2:{}'.format(Diff2))

            print('終了!!!!')
            print('state_history={}'.format(state_history))
            SUM_change[2]=SUM
            print('SUM_change:{}\n'.format(SUM_change))

            excp = Exception()
            excp.value = state_history,judge1,judge2,judge3,judge4, SUM
            raise excp
        else:
            print('\n疑念0.5以上')
            print('diff:{}'.format(diff))
            print('sum:{}\n'.format(SUM))
            print('j={}'.format(j))

            if judge1 == True:
                SUM_change[1]=SUM
                print('SUM_change:{}\n'.format(SUM_change))
            else:
                SUM_change[0]=SUM
                print('SUM_change:{}\n'.format(SUM_change))
            s_next = 0 #s - 8 #1
            #depth = num[j]
            #j -= 1
            depth = 0    #1

            # i = 0        試しにコメントアウト

            SUM = 0
            j = 0
            # state_history.append(s_next) 　　　　試しにコメントアウト

            judge1 = True
            AAA(s_next,depth,i,j,S,S2,S3,S4,judge1,judge2,judge3,judge4, SUM)

    
    # if i == 0:
    #     state_history[0] = 0    ##################試しにコメントアウト#######################

        
    if depth > num[j]: #変更点　ずっと3進む

        
        #print([random.randint(0, 3+j) for i in range(5)])
        print('{}回目　num[{}]={} s={}'.format(i,j,num[j],s))
        
        if num[j]==3:
            # if S == False:#     and S2 == False:
                test = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])

                TEST[i] = test  
                Diff2[i] = abs(1.0 - test)
                Diff2[i+1] = abs(1.0 - test)  

                # diff[x] = abs(1.0 - sNumbers2[x])
                diff[j] = abs(1.0 - test)

                SUM += diff[j]
                
                # if r1 == 1:
                # judge1 = True     試しにコメントアウト

                print('j = {}'.format(j))
                print('test:{}   diff:{}'.format(test,diff))
                S = True
                s_next = s #+ 3
                state_history.append(s_next)
                #state_history.append(s_next)    #追加した場所
                #####
                #s_next = s
                #state_history.append(s_next)
                depth = 0
                AAA(s_next,depth,i+1,j+1,S,S2,S3,S4,judge1,judge2,judge3,judge4, SUM)
                
                
        elif num[j]==1:#2:
            # if S3 == False :
                test = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])
                TEST[i] = test 
                Diff2[i] = abs(1.0 - test)
                Diff2[i+1] = abs(1.0 - test)    

                # diff[x] = abs(1.0 - sNumbers2[x])
                diff[j] = abs(1.0 - test)
                print('test2:{}   diff2:{}'.format(test,diff))

                SUM += diff[j]
                
                # if r2 == 1:
                judge3 = True
                s_next = s #+ 2

                print('j = {}'.format(j))
                S3 = True
                #state_history.append(s_next)
                #state_history.append(s_next)    #追加した場所
                #####
                #s_next = s
                depth = 0
                state_history.append(s_next)
                AAA(s_next,depth,i+1,j+1,S,S2,S3,S4,judge1,judge2,judge3,judge4, SUM)
                


    s_next = s + 1  # 上に移動するときは状態の数字が3小さくなる

    # SUM += diff[j]


    state_history.append(s_next)#(s_next)
    
    print('depth {}'.format(depth))
    AAA(s_next,depth+1,i+1,j,S,S2,S3,S4,judge1,judge2,judge3,judge4, SUM)

    
    A[s] = 0 #1 #0
    #print('再帰関数s={},A={}'.format(s,A))
    #print('再帰関数state_history={}'.format(state_history))
    state_history.append(s)
    return state_history,judge1,judge2,judge3,judge4, SUM


# 迷路内をエージェントがゴールするまで移動させる関数の定義
def AAA_top(s,depth):
    i = 0
    j = 0
    # depth = 0
    S = False
    S2 = False
    S3 = False
    S4 = False
    judge1 = False
    judge2 = False
    judge3 = False
    judge4 = False

    SUM = 0
    try:
        AAA(s,depth,i,j,S,S2,S3,S4,judge1,judge2,judge3,judge4, SUM)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [8]  # エージェントの移動を記録するリスト
    state_history,judge1,judge2,judge3,judge4, SUM = AAA_top(s,0)
    
    return state_history,judge1,judge2,judge3,judge4, SUM


# 迷路内をゴールを目指して、移動
state_history,judge1,judge2,judge3,judge4, SUM = goal_maze(pi_0)

#print('s={}'.format(state_history[0]))
#print(state_history)
print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")

#print('S = {},{},{},{}'.format(S,S2,S3,S4))
print('judge = {},{},{},{}'.format(judge1,judge2,judge3,judge4))


# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map


def init():
    '''背景画像の初期化'''
    line.set_data([], [])
    
    return (line,)

# 現在地S0に緑丸を描画する
#line1, = ax.plot([1.5], [2.5], marker="*", color='y', markersize=30)
#line2, = ax.plot([1.5], [4.0], marker="d", color='r', markersize=10)


def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state  + 0.5

    plt.title('data={:.2f}'.format(i))
    # plt.title('δstress={}'.format(SUM))
    plt.title('δstress={:.2f}'.format(TEST[i-1]))
    # plt.title('ΣSUM1={}\nΣSUM2={}\nΣSUM3={}\nΔδstress={}'.format(SUM_change[0],SUM_change[1],SUM_change[2], Diff2[i]))
    plt.title('Σ1={:.2f}\nΣ2={:.2f}\nΣ3={:.2f}\nΔstress={:.2f}'.format(SUM_change[0],SUM_change[1],SUM_change[2], Diff2[i]))

    # plt.text(0.5, 8.5, 'δstress={}'.format(TEST[i]), size=10, ha='center')
    
    # y = (state % 9) + 0.5 # y座標は3で割った商を2.5から引く


    # if state == 4 and state_history[i+1]==5 and judge1 == True:
    #     line1.set_data(x+0.2,y)
    #     # elif state == 2 and state_history[i-1]==3 and judge2 == True:
    #     #     line1.set_data(x+0.2,y)
    # elif state == 6 and state_history[i+1]==7 and judge3 == True:
    #     line2.set_data(x+0.2,y)
    # elif state == 8 and state_history[i-1]==7 and judge4 == True:
    #     line2.set_data(x+0.2,y)
    # else:
    #     line1.set_data(0.5,-0.5)
    #     line2.set_data(0.5,-0.5)
    # line.set_data(x, y)
    # return (line,)

    if state == 4:
        line1.set_data(x+0.2,y)
    elif state == 6:
        line2.set_data(x+0.2,y)
    elif state == 8:
        line2.set_data(x+0.2,y)
    else:
        line1.set_data(0.5,-0.5)
        line2.set_data(0.5,-0.5)
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=1000, repeat=False)

HTML(anim.to_jshtml())
plt.show()





# results = np.zeros(shape=(30))
# for y in SUM_change:
#     results[y] = SUM_change[y]



# from openpyxl import Workbook

# from openpyxl.chart import PieChart, Reference, Series

# wb = Workbook()
# ws = wb.active
# cs = wb.create_chartsheet()

# rows = [
#     ["Step数", str(len(state_history) - 1)],
#     ["Bob", 3],
#     ["合計", results],
#     # ["合計2",results.append(y) for y in SUM_change],
#     # ["SUM1回目", SUM[0][0]],
#     # ["SUM2回目", SUM[1]],
#     # ["SUM3回目", SUM[2]],
# ]

# for row in rows:
#     ws.append(row)


# chart = PieChart()
# labels = Reference(ws, min_col=1, min_row=1, max_row=3)
# data = Reference(ws, min_col=2, min_row=1, max_row=3)
# chart.series = (Series(data),)
# chart.title = "PieChart"

# cs.add_chart(chart)

# wb.save("/Users/ken/Desktop/10_micromouseAstar3X/Excel/demo2.xlsx")