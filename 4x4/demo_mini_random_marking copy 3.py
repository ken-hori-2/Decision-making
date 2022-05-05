import numpy as np
import matplotlib.pyplot as plt
import random

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言
fig = plt.figure(figsize=(5, 5))
ax = plt.gca()

# 赤い壁を描く
plt.plot([1, 1], [0, 1], color='black', linewidth=2)
plt.plot([1, 2], [2, 2], color='black', linewidth=2)
plt.plot([2, 2], [2, 1], color='black', linewidth=2)
plt.plot([2, 3], [1, 1], color='black', linewidth=2)
plt.plot([3, 2], [3, 3], color='black', linewidth=2)

plt.plot([3, 3], [3, 2], color='black', linewidth=2)
plt.plot([3, 2], [2, 2], color='black', linewidth=2)
plt.plot([1, 1], [3, 2], color='black', linewidth=2)
plt.plot([3, 3], [1, 0], color='black', linewidth=2)

# 状態を示す文字S0～S8を描く
plt.text(0.5, 3.5, 'S0', size=14, ha='center')
plt.text(1.5, 3.5, 'S1', size=14, ha='center')
plt.text(2.5, 3.5, 'S2', size=14, ha='center')
plt.text(3.5, 3.5, 'S3', size=14, ha='center')
plt.text(0.5, 2.5, 'S4', size=14, ha='center')
plt.text(1.5, 2.5, 'S5', size=14, ha='center')
plt.text(2.5, 2.5, 'S6', size=14, ha='center')
plt.text(3.5, 2.5, 'S7', size=14, ha='center')
plt.text(0.5, 1.5, 'S8', size=14, ha='center')
plt.text(1.5, 1.5, 'S9', size=14, ha='center')
plt.text(2.5, 1.5, 'S10', size=14, ha='center')
plt.text(3.5, 1.5, 'S11', size=14, ha='center')
plt.text(0.5, 0.5, 'S12', size=14, ha='center')
plt.text(1.5, 0.5, 'S13', size=14, ha='center')
plt.text(2.5, 0.5, 'S14', size=14, ha='center')
plt.text(3.5, 0.5, 'S15', size=14, ha='center')
plt.text(1.5, 2.3, 'START', ha='center')
plt.text(2.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([1.5], [2.5], marker="o", color='g', markersize=60)

# 初期の方策を決定するパラメータtheta_0を設定

# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[np.nan, 1, 1, np.nan],  # s0
                    [np.nan, 1, 1, 1],  # s1
                    [np.nan, 1, np.nan, 1],  # s2
                    [np.nan, np.nan, 1, 1],  # s3
                    [1, np.nan, 1, np.nan],  # s4
                    [1, 1, np.nan, np.nan],  # s5
                    [np.nan, np.nan, np.nan, 1],  # s6
                    [1, np.nan, 1, np.nan],  # s7、※s8はゴールなので、方策はなし
                    [1, 1, 1, np.nan],  #s8
                    [np.nan, np.nan, 1, 1],  #s9
                    [np.nan, 1, np.nan, np.nan],  #s10
                    [1, np.nan, 1, 1],  #11
                    [1, np.nan, np.nan, np.nan],  #12
                    [1, 1, np.nan, np.nan],  #13
                    [np.nan, np.nan, np.nan, 1],
                    [1,np.nan,np.nan,np.nan]  #15
                    
                    #[np.nan, 1, np.nan, 1]  #14
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



[a, b] = theta_0.shape  # 行と列の数をa, bに格納
AA = np.nan_to_num(theta_0)  # nanを0に変換
Q = np.random.rand(a, b) * theta_0 * 0.1

print([a,b])
print(AA)

# 初期の方策pi_0を表示
pi_0
print(pi_0)
PI = pi_0
print(PI[1][0])
print(PI[1][1])

# 1step移動後の状態sを求める関数を定義

A = [0]*16
def get_next_s(pi, s):
    print('総和A[{}] = {}'.format(s,AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3]))
    direction = ["up", "right", "down", "left"]
    
    A[s] = 2
    print('A[s] = {},s = {},A = {}'.format(A[s],s,A))
    

    while(1):
        next_direction = np.random.choice(direction, p=pi[s, :])
        # pi[s,:]の確率に従って、directionが選択される

        if next_direction == "up":
            s_next = s - 4  # 上に移動するときは状態の数字が3小さくなる
            if A[s_next] < 2:
                break
            else:
                s_next = s
                if A[s-4] == 2 and AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3] <= 1:
                    print('行き止まり:{}'.format(s))
                    A[s-4] = 0
                else:
                    #Maze(s_next)
                    if AA[s][0] == 1: #↑

                        if A[s-4] <= 2:#上
                            A[s-4] = 0
                            pass #Maze(s-1)

                        
                    elif AA[s][1] == 1:#→

                        if A[s+1] < 2:#右
                            A[s+1] = 0
                            pass #Maze(s+1)
                    elif AA[s][2] == 1:#↓

                        if A[s+4] < 2:#下
                            A[s+4] = 0
                            pass #Maze(s-4)
                    elif AA[s][3] == 1:#←

                        if A[s-1] < 2:#左
                            A[s-1] = 0
                            pass #Maze(s+4)

                    #探索前に戻す
                    #A[s] = 0


                continue
        elif next_direction == "right":
            s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
            if A[s_next] < 2:
                break
            else:
                s_next = s
                if A[s+1] == 2 and AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3] <= 1:
                    print('行き止まり:{}'.format(s))
                    A[s+1] = 0
                else:
                    if AA[s][1] == 1:#→

                        if A[s+1] <= 2:#右
                            A[s+1] = 0
                            pass #Maze(s+1)
                

                continue
        elif next_direction == "down":
            s_next = s + 4  # 下に移動するときは状態の数字が3大きくなる
            if A[s_next] < 2:
                break
            else:
                s_next = s
                if A[s+4] == 2 and AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3] <= 1:
                    print('行き止まり:{}'.format(s))
                    A[s+4] = 0
                else:
                    if AA[s][2] == 1:#↓

                        if A[s+4] <= 2:#下
                            A[s+4] = 0
                            pass #Maze(s-4)
                

                continue
        elif next_direction == "left":
            s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる
            if A[s_next] < 2:
                break
            else:
                s_next = s
                if A[s-1] == 2 and AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3] <= 1:
                    print('行き止まり:{}'.format(s))
                    A[s-1] = 0
                else:
                    if AA[s][3] == 1:#←

                        if A[s-1] <= 2:#左
                            A[s-1] = 0
                            pass #Maze(s+4)
                

                continue
        
        NEXT = s_next
        A[s] = 0
        print('行き止まり:{}'.format(A[s]))
            #break

    
    #if A[next_s] < 2:

    #if A[NEXT-1] < 2:#左
    #    NEXT = NEXT-1 #Maze(next_s-1)
    #elif A[NEXT+1] < 2:#右
    #    NEXT = NEXT+1 #Maze(next_s+1)
    #elif A[NEXT-4] < 2:#上
    #    NEXT = NEXT-4 #Maze(next_s-4)
    #elif A[NEXT+4] < 2:#下
    #    NEXT = NEXT+4 #Maze(next_s+4)
    #else:
        #    A[next_s] = 2
    #    A[NEXT] = 0
    
    return s_next


#############
def Maze(x):
    #ゴールについた時点で終了
    if A[x] == 1:
        #print([(x, y), depth])
        exit()

    #探索済みとしてセット
    A[x] = 2
    #1秒ごとに図の更新
    #sleep(1)
    #track(PI, depth)

    #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
    if A[x-1] < 2:#左
        Maze(x-1)
    if A[x+1] < 2:#右
        Maze(x+1)
    if A[x-4] < 2:#上
        Maze(x-4)
    if A[x+4] < 2:#下
        Maze(x+4)

    #探索前に戻す
    A[x] = 0
#############

# 迷路内をエージェントがゴールするまで移動させる関数の定義


def goal_maze(pi):
    s = 5  # スタート地点
    state_history = [5]  # エージェントの移動を記録するリスト
    
    #result = Maze(5,0)
    i=0
    
    

    while (1):  # ゴールするまでループ
        next_s = get_next_s(pi, s)
        state_history.append(next_s)  # 記録リストに次の状態（エージェントの位置）を追加

        TEST = state_history
        print('確認:{},{},s_next:{}'.format(TEST,i,next_s))
        print('確認2:{}'.format(TEST[i+1]))

        


        if next_s == 14:  # ゴール地点なら終了
            break
        else:
            s = next_s
            i+=1

    return state_history


# 迷路内をゴールを目指して、移動
state_history = goal_maze(pi_0)


print(state_history)
print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")


# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML


def init():
    '''背景画像の初期化'''
    line.set_data([], [])
    return (line,)


def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    x = (state % 4) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y = 3.5 - int(state / 4)  # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=200, repeat=False)

HTML(anim.to_jshtml())
plt.show()