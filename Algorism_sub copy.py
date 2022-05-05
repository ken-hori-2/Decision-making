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
fig = plt.figure(figsize=(1, 7))
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
D = 0
#judge = False
r1 = random.randint(0,1)
r2 = random.randint(0,1)


import random

def AAA(s,depth,i,j,S,S2,judge,judge1,judge2):
    direction = ["up", "right", "down", "left"]
    
    #if A[s] == 8 or i > 30: #14:  # ゴール地点なら終了
    if s == 8 or i > 30:
        print('終了!!!!')
        print('state_history={}'.format(state_history))
        excp = Exception()
        excp.value = state_history,S,S2,judge,judge1,judge2
        raise excp
    
    if i == 0:
        state_history[0]=0

        
    if depth > num[j]: #変更点　ずっと3進む

        
        #print([random.randint(0, 3+j) for i in range(5)])
        print('num[{}]={}'.format(j,num[j]))
        r = random.randint(0,num[j])
        print('r = {}'.format(r))

        # r = random.randint(0,1)
        
        # print('r = {}'.format(r))
        print('r1 = {}'.format(r1))
        print('r2 = {}'.format(r2))
        if num[j]==3:
            #if r == 1 and S == False:
            if S == False:
                if judge == True:
                    pass
                else:
                    s_next = s - 1
                    #depth = num[j]
                    #j -= 1
                    depth -= 1
                    if r1 == 1 :# and judge == False:
                        print('{}回目　r1 = True'.format(i))
                        S = True
                        judge = True
                        print('judge == {}'.format(judge))
                        print('S == {}'.format(S))
                    else:
                        print('{}回目　r1 = False'.format(i))
                    
                state_history.append(s_next)
                #state_history.append(s_next)    #追加した場所
                #####
                s_next = s
                state_history.append(s_next)
                AAA(s_next,depth+1,i+1,j+1,S,S2,judge,judge1,judge2)
            #if r == 2 and S == False:
            if S == False:
                s_next = s - 2
                #depth = num[j]
                #j -= 1
                depth -= 2
                S = True
                judge1 = True
                state_history.append(s_next)
                #state_history.append(s_next)    #追加した場所
                #####
                s_next = s
                state_history.append(s_next)
                AAA(s_next,depth+1,i+1,j+1,S,S2,judge,judge1,judge2)

                # if r == 3 :#and S == False:
                #     s_next = s - 3
                #     #depth = num[j]
                #     #j -= 1
                #     depth -= 3
                #     S = True
                #     state_history.append(s_next)
                #     s_next = s
                #     state_history.append(s_next)
                #     AAA(s_next,depth+1,i+1,j+1,S)
                # if r == 2:
                #     s_next = s - 2
                #     #depth = num[j]
                #     j -= 2
                #     depth -= 2
                #     S = False
                #     state_history.append(s_next)
        if num[j]==2:
            #if r == 1 and S2 == False:
            if S2 == False:
                if judge2 == True:
                    pass
                    #skip
                else:
                    s_next = s - 1
                    #depth = num[j]
                    #j -= 1
                    depth -= 1
                    if r2 == 1: # and judge == False:
                        #if r1 == 1:
                        print('r2 = True')
                        S2 = True
                        judge2 = True
                        print('judge == {}'.format(judge))
                        print('S2 == {}'.format(S))
                        #S2 = True
                state_history.append(s_next)
                #state_history.append(s_next)    #追加した場所
                #####
                s_next = s
                state_history.append(s_next)
                AAA(s_next,depth+1,i+1,j+1,S,S2,judge,judge1,judge2)
            #if r == 2 and S2 == False:
            if S2 == False:
                s_next = s - 2
                #depth = num[j]
                #j -= 1
                depth -= 2
                S2 = True
                state_history.append(s_next)
                #state_history.append(s_next)    #追加した場所
                #####
                s_next = s
                state_history.append(s_next)
                AAA(s_next,depth+1,i+1,j+1,S,S2,judge,judge1,judge2)
        else:


            s_next = s #- r #(3+j)  # 上に移動するときは状態の数字が3小さくなる
            state_history.append(s_next)
            depth = 0
            j=0
            #j+=1
            print('depth {}'.format(depth))
            print('i {}'.format(i))
            AAA(s_next,depth+1,i+1,j+1,S,S2,judge,judge1,judge2)
    s_next = s + 1  # 上に移動するときは状態の数字が3小さくなる


    state_history.append(s_next)#(s_next)
    
    print('depth {}'.format(depth))
    AAA(s_next,depth+1,i+1,j,S,S2,judge,judge1,judge2)

    
    


    A[s] = 0 #1 #0
    #print('再帰関数s={},A={}'.format(s,A))
    #print('再帰関数state_history={}'.format(state_history))
    state_history.append(s)
    return state_history,S,S2,judge,judge1,judge2


# 迷路内をエージェントがゴールするまで移動させる関数の定義

def AAA_top(s,depth,i,j,S,S2,judge,judge1,judge2):
    
    
    # depth = 0
    
    
    try:
        AAA(s,depth,i,j,S,S2,judge,judge1,judge2)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [8]  # エージェントの移動を記録するリスト
    i = 0
    j = 0
    judge = False
    judge1 = False
    judge2 = False
    S = False
    S2 = False
    state_history,S,S2,judge,judge1,judge2 = AAA_top(s,0,i,j,S,S2,judge,judge1,judge2)

    print('S1,S2 == {},{}'.format(S,S2))
    
    return state_history,S,S2,judge,judge1,judge2


# 迷路内をゴールを目指して、移動
state_history,S,S2,judge,judge1,judge2 = goal_maze(pi_0)

print('s={}'.format(state_history[0]))
#print(state_history)
print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")

print('judge == {}'.format(judge))
#print('S1,S2 == {},{}'.format(S,S2))


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
    # y = (state % 9) + 0.5 # y座標は3で割った商を2.5から引く
    if state == 3 and state_history[i-1]==4 and judge == True:
        line1.set_data(x+0.2,y)
    if state == 3 and state_history[i-1]==4 and judge1 == True:
        line2.set_data(x+0.2,y)
    elif state == 2 and state_history[i-1]==4:
        line1.set_data(x+0.2,y)
    elif state == 5 and state_history[i-1]==6 and judge2 == True:
        line2.set_data(x+0.2,y)
    elif state == 4 and state_history[i-1]==6:
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