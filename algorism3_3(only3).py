import numpy as np
import matplotlib.pyplot as plt
import random

from numpy.core.defchararray import title

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言

# # 現在地S0に緑丸を描画する
# line, = ax.plot([2.5], [3.5], marker="o", color='g', markersize=30)
fig = plt.figure(figsize=(1, 7))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
#plt.text(0.5, 0.5, 'S0', size=14, ha='center')
#plt.text(0.5, 1.5, 'S1', size=14, ha='center')
#plt.text(0.5, 2.5, 'S2', size=14, ha='center')
#plt.text(0.5, 3.5, 'S3', size=14, ha='center')
plt.text(0.5, 4.5, 'Node\n(事前情報)', size=8, ha='center')
#plt.text(0.5, 5.5, 'S5', size=14, ha='center')
#plt.text(0.5, 6.5, 'S6', size=14, ha='center')
#plt.text(0.5, 7.5, 'S7', size=14, ha='center')
#plt.text(0.5, 8.5, 'S8', size=14, ha='center')

plt.text(0.5, 1.3, 'Node', ha='center')
#plt.text(4.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 1)
ax.set_ylim(0, 9)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [0.5], marker="^", color='y', markersize=20)

# 初期の方策を決定するパラメータtheta_0を設定

# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_1 = np.array([[np.nan, 1, 1, np.nan],  # s0
                    [7, 1, 1, 1],  # s1
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
                    [np.nan, 1, np.nan, 1],
                    [1,np.nan,np.nan,np.nan]  #15
                    
                    #[np.nan, 1, np.nan, 1]  #14
                    ])

                   # ↑、  →、  ↓、  ←         を表す
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

[a, b] = theta_0.shape  # 行と列の数をa, bに格納
AA = np.nan_to_num(theta_0)  # nanを0に変換
Q = np.random.rand(a, b) * theta_0 * 0.1

# print([a,b])
# print('AA={}'.format(AA))

# 初期の方策pi_0を表示
pi_0
# print(pi_0)
PI = pi_0

# 1step移動後の状態sを求める関数を定義

A = [0]*19
A[8]=8
A[15]=8

state_history = [8]  # エージェントの移動を記録するリスト
# SSS = True

# COST = 4
# A_COST = [0]*36

import random

def AAA(s,depth,i,j):
    direction = ["up", "right", "down", "left"]
    
    if A[s] == 8 or i > 30: #14:  # ゴール地点なら終了
        print('終了!!!!')
        print('state_history={}'.format(state_history))
        excp = Exception()
        excp.value = state_history
        raise excp

    if depth > 3:#3+j: #4:              変更点　ずっと3進む

        
        print([random.randint(0, 3+j) for i in range(5)])
        r = random.randint(0,3+j)
        print('r = {}'.format(r))
        s_next = s - r #(3+j)  # 上に移動するときは状態の数字が3小さくなる
        state_history.append(s_next)
        depth = 0
        #j+=1
        print('depth {}'.format(depth))
        print('i {}'.format(i))
        AAA(s_next,depth+1,i+1,j+1)
        
    #     #if AA[s][1]==7:
            
    #         A[s] = 0 #1 #0
    #         print('コスト3以上　次LMの分岐でゴールから離れる　⇒　引き返す')
    #         state_history.append(s)
    #         return state_history
        
        
    #A[s] = 2
    
    # if AA[s][0]==7:
    #     s_next = s + 1  # 左に移動するときは状態の数字が1小さくなる
    #     state_history.append(s_next)
    #     print('ランドマーク発見!!!!s_next = {}'.format(s_next))
    #     AAA(s_next,depth+1)
    # if AA[s][1]==7:
    #     s_next = s + 6  # 左に移動するときは状態の数字が1小さくなる
    #     state_history.append(s_next)
    #     print('ランドマーク発見!!!!s_next = {}'.format(s_next))
    #     AAA(s_next,depth+1)


    #if next_direction == "up":
    # if A[s-6] < 2 and AA[s][0]==1:
    #if AA[s][0]==1:
    s_next = s + 1  # 上に移動するときは状態の数字が3小さくなる
    state_history.append(s_next)
    
    print('depth {}'.format(depth))
    AAA(s_next,depth+1,i+1,j)

    #if next_direction == "right":
    # if AA[s][1]==1:
    #     if A[s+1] < 2:
    #         s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
    #         state_history.append(s_next)
            
    #         print('depth {}'.format(depth))
    #         AAA(s_next,depth+1)
    


    #if next_direction == "down":
    # if AA[s][2]==1:
    #     if A[s+6] < 2:
    #         s_next = s + 6  # 下に移動すると
    #         state_history.append(s_next)
            
    #         print('depth {}'.format(depth))
    #         AAA(s_next,depth+1)
    
    # if A[s-1] < 2 and int(AA[s][3])==1:
    #     s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる
    #     state_history.append(s_next)
        
    #     print('depth {}'.format(depth))
    #     AAA(s_next,depth+1)
    


    A[s] = 0 #1 #0
    #print('再帰関数s={},A={}'.format(s,A))
    #print('再帰関数state_history={}'.format(state_history))
    state_history.append(s)
    return state_history


# 迷路内をエージェントがゴールするまで移動させる関数の定義

def AAA_top(s,depth):
    i = 0
    j = 0
    try:
        AAA(s,depth,i,j)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [0]  # エージェントの移動を記録するリスト
    state_history = AAA_top(s,0)
    
    return state_history


# 迷路内をゴールを目指して、移動
state_history = goal_maze(pi_0)


#print(state_history)
print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")


# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map


def init():
    '''背景画像の初期化'''
    line.set_data([], [])
    #line1.set_data([], [])
    #line2.set_data([], [])
    #TXT.set_text = ([])
    return (line,)

# 現在地S0に緑丸を描画する
#line1, = ax.plot([1.5], [2.5], marker="*", color='y', markersize=30)
#line2, = ax.plot([1.5], [4.0], marker="d", color='r', markersize=10)

X = [0.]*1000
Y = [0.]*1000

X2 = [0.]*1000
Y2 = [0.]*1000


TEST = []
TXT = 0

total_reward = 0.0
#TXT = ax.text(1.5, 6.3, "reward/sec:" + str(1.0), fontsize=20)

#total_reward += 1*1.0
#ax.text(X[i]+1.0, Y[i]-1.0, "total reward: {:.1f}".format(total_reward), fontsize=8)



# def animate(i):
#     '''フレームごとの描画内容'''
#     state = state_history[i]  # 現在の場所を描く
    
#     x = (state % 6) + 0.5  # 状態のx座標は、3で割った余り+0.5
#     y = 5.5 - int(state / 6)  # y座標は3で割った商を2.5から引く
#     line.set_data(x, y)
    
#     x2 = (state % 6) + 0.5  # 状態のx座標は、3で割った余り+0.5
#     y2 = 5.5 - int(state / 6)  # y座標は3で割った商を2.5から引く
#     X[i] = x2
#     Y[i] = y2
    
#     #####################
#     line1.set_data(X[:i], Y[:i])
#     #####################
#     #line2.set_data(x, y)
#     ax.plot([1.0], [3.5], marker="d", color='r', markersize=20)
#     ax.plot([0.0], [4.5], marker="d", color='r', markersize=20)
#     ax.plot([4.0], [3.5], marker="d", color='b', markersize=20)
#     ax.plot([5.0], [1.5], marker="d", color='b', markersize=20)

#     # ax.plot([0.5], [3.5], marker="s", color='k', markersize=50)
#     # ax.plot([2.5], [4.5], marker="s", color='k', markersize=50)
#     # ax.plot([3.5], [0.5], marker="s", color='k', markersize=50)

#     X2[i] = x2  #-0.2
#     Y2[i] = y2-0.3

    
   
#     return (line, TXT) #あってもなくても変わらない
def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state  + 0.5
    # y = (state % 9) + 0.5 # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    return (line,)

#def reward_per_sec():
#        return -1.0 #- self.puddle_depth*self.puddle_coef




#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=1000, repeat=False)

HTML(anim.to_jshtml())
plt.show()








class test(): ###puddleingoreagent3
    def __init__(self, time_interval, nu, omega, estimator, puddle_coef=100): #KfAgentのinitの引数にpuddle_coef追加
        super().__init__(time_interval, nu, omega, estimator)
        
        self.puddle_coef = puddle_coef
        self.puddle_depth = 0.0
        self.total_reward = 0.0
        
    def reward_per_sec(self):
        return -1.0 - self.puddle_depth*self.puddle_coef

    def decision(self, observation=None):
        self.estimator.motion_update(self.prev_nu, self.prev_omega, self.time_interval) 
        self.prev_nu, self.prev_omega = self.nu, self.omega
        self.estimator.observation_update(observation)
        
        self.total_reward += self.time_interval*self.reward_per_sec()
        
        return self.nu, self.omega
        
    def draw(self, ax, elems): 
        super().draw(ax, elems)
        x, y, _ = self.estimator.pose
        elems.append(ax.text(x+1.0, y-0.5, "reward/sec:" + str(self.reward_per_sec()), fontsize=8))
        elems.append(ax.text(x+1.0, y-1.0, "total reward: {:.1f}".format(self.total_reward), fontsize=8))