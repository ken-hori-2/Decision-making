import numpy as np
import matplotlib.pyplot as plt

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言
fig = plt.figure(figsize=(2, 7))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
#plt.text(0.5, 0.5, 'S0', size=14, ha='center')
#plt.text(0.5, 1.5, 'S1', size=14, ha='center')
#plt.text(0.5, 2.5, 'S2', size=14, ha='center')
#plt.text(0.5, 3.5, 'S3', size=14, ha='center')
#plt.text(0.5, 4.5, 'S4', size=14, ha='center')
#plt.text(0.5, 5.5, 'S5', size=14, ha='center')
#plt.text(0.5, 6.5, 'S6', size=14, ha='center')
#plt.text(0.5, 7.5, 'S7', size=14, ha='center')
#plt.text(0.5, 8.5, 'S8', size=14, ha='center')

plt.text(0.5, 0.3, 'START', ha='center')
#plt.text(4.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 1)
ax.set_ylim(0, 9)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [0.5], marker="o", color='g', markersize=30)

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
# 方策パラメータthetaを行動方策piに変換する関数の定義
[m, n] = theta_0.shape  # thetaの行列サイズを取得
pi_________sub = np.zeros((m, n))
for i in range(0, m):
        pi_________sub[i, :] = np.nansum(theta_0[i, :])  # 割合の計算


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

# 1step移動後の状態sを求める関数を定義

AA = np.nan_to_num(theta_0)

A = [0]*36
A[8]=1
state_history = [8]

def AAA(s,depth,pi):
    #print('総和A[{}] = {}'.format(s,AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3]))
    direction = ["up", "right", "down", "left"]
    next_direction = np.random.choice(direction, p=pi[s, :])
    
    if A[s] == 8 or depth >15: #14:  # ゴール地点なら終了
        print('終了!!!!')
        print('state_history={}'.format(state_history))
        excp = Exception()
        excp.value = state_history
        raise excp

    if A[s]!=5:

        if depth >= 3: #4:
            #s_next = s - 1
            A[s]=5
            state_history.append(s)
            return state_history
            #AAA(s_next,depth+1,pi)
    
    if next_direction == "up":
        s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
        state_history.append(s_next)
        print('depth {}'.format(depth))
        AAA(s_next,depth+1,pi)
    


    A[s] = 0 #1 #0
    state_history.append(s)
    return state_history
    



# 迷路内をエージェントがゴールするまで移動させる関数の定義

def AAA_top(s,depth,pi):
    try:
        AAA(s,depth,pi)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [0]  # エージェントの移動を記録するリスト
    
    

    state_history = AAA_top(s,0,pi)
    
    TEST = state_history
    #print('確認:{}'.format(TEST))
    
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
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state  + 0.5
    # y = (state % 9) + 0.5 # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=1000, repeat=False)

#HTML(anim.to_jshtml())
plt.show()