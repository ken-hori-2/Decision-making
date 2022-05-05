import numpy as np
import matplotlib.pyplot as plt
import random

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言
fig = plt.figure(figsize=(6, 6))
ax = plt.gca()

# 赤い壁を描く
#plt.plot([1, 1], [0, 1], color='black', linewidth=2)
#plt.plot([1, 2], [2, 2], color='black', linewidth=2)
#plt.plot([2, 2], [2, 1], color='black', linewidth=2)
#plt.plot([2, 3], [1, 1], color='black', linewidth=2)
#plt.plot([3, 2], [3, 3], color='black', linewidth=2)

plt.plot([1, 1], [4, 5], color='red', linewidth=2)
plt.plot([1, 2], [5, 5], color='red', linewidth=2)
plt.plot([2, 2], [4, 6], color='red', linewidth=2)
plt.plot([3, 3], [5, 6], color='red', linewidth=2)

plt.plot([3, 3], [3, 4], color='red', linewidth=2)
plt.plot([0, 1], [3, 3], color='red', linewidth=2)
plt.plot([2, 5], [3, 3], color='red', linewidth=2)
plt.plot([2, 2], [1, 3], color='red', linewidth=2)
plt.plot([1, 2], [2, 2], color='red', linewidth=2)

plt.plot([5, 5], [1, 3], color='red', linewidth=2)
plt.plot([4, 5], [1, 1], color='red', linewidth=2)
plt.plot([4, 4], [1, 2], color='red', linewidth=2)
plt.plot([3, 3], [1, 0], color='red', linewidth=2)


plt.plot([1, 1], [1, 1], color='red', linewidth=2)
plt.plot([3, 4], [2, 2], color='red', linewidth=2)
plt.plot([5, 6], [2, 2], color='red', linewidth=2)
plt.plot([4, 6], [4, 4], color='red', linewidth=2)
plt.plot([5, 5], [4, 5], color='red', linewidth=2)

plt.plot([4, 5], [5, 5], color='red', linewidth=2)
#plt.plot([4, 5], [1, 1], color='red', linewidth=2)
#plt.plot([4, 4], [1, 2], color='red', linewidth=2)
#plt.plot([3, 3], [1, 0], color='black', linewidth=2)

# 状態を示す文字S0～S8を描く
plt.text(0.5, 5.5, 'S0', size=14, ha='center')
plt.text(1.5, 5.5, 'S1', size=14, ha='center')
plt.text(2.5, 5.5, 'S2', size=14, ha='center')
plt.text(3.5, 5.5, 'S3', size=14, ha='center')
plt.text(4.5, 5.5, 'S4', size=14, ha='center')
plt.text(5.5, 5.5, 'S5', size=14, ha='center')
plt.text(0.5, 4.5, 'S6', size=14, ha='center')
plt.text(1.5, 4.5, 'S7', size=14, ha='center')
plt.text(2.5, 4.5, 'S8', size=14, ha='center')
plt.text(3.5, 4.5, 'S9', size=14, ha='center')
plt.text(4.5, 4.5, 'S10', size=14, ha='center')
plt.text(5.5, 4.5, 'S11', size=14, ha='center')
plt.text(0.5, 3.5, 'S12', size=14, ha='center')
plt.text(1.5, 3.5, 'S13', size=14, ha='center')
plt.text(2.5, 3.5, 'S14', size=14, ha='center')
plt.text(3.5, 3.5, 'S15', size=14, ha='center')

plt.text(4.5, 3.5, 'S16', size=14, ha='center')
plt.text(5.5, 3.5, 'S17', size=14, ha='center')
plt.text(0.5, 2.5, 'S18', size=14, ha='center')
plt.text(1.5, 2.5, 'S19', size=14, ha='center')
plt.text(2.5, 2.5, 'S20', size=14, ha='center')
plt.text(3.5, 2.5, 'S21', size=14, ha='center')
plt.text(4.5, 2.5, 'S22', size=14, ha='center')
plt.text(5.5, 2.5, 'S23', size=14, ha='center')
plt.text(0.5, 1.5, 'S24', size=14, ha='center')
plt.text(1.5, 1.5, 'S25', size=14, ha='center')
plt.text(2.5, 1.5, 'S26', size=14, ha='center')
plt.text(3.5, 1.5, 'S27', size=14, ha='center')
plt.text(4.5, 1.5, 'S28', size=14, ha='center')
plt.text(5.5, 1.5, 'S29', size=14, ha='center')
plt.text(0.5, 0.5, 'S30', size=14, ha='center')
plt.text(1.5, 0.5, 'S31', size=14, ha='center')

plt.text(2.5, 0.5, 'S32', size=14, ha='center')
plt.text(3.5, 0.5, 'S33', size=14, ha='center')
plt.text(4.5, 0.5, 'S34', size=14, ha='center')
plt.text(5.5, 0.5, 'S35', size=14, ha='center')


plt.text(2.5, 2.3, 'START', ha='center')
plt.text(5.5, 2.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([2.5], [2.5], marker="o", color='g', markersize=30)

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
                    [np.nan, np.nan, np.nan, 1],
                    [1,np.nan,np.nan,np.nan]  #15
                    
                    #[np.nan, 1, np.nan, 1]  #14
                    ])

                   # ↑、  →、  ↓、  ←         を表す
theta_0 = np.array([[np.nan, 1, 1, np.nan],  # s0
                    [np.nan, np.nan, np.nan, 1],  # s1
                    [np.nan, np.nan, 1, np.nan],  # s2
                    [np.nan, 1, 1, np.nan],  # s3
                    [np.nan, 1, np.nan, 1],  # s4
                    [np.nan, np.nan, 1, 1],  # s5
                    [1, np.nan, 1, np.nan],  # s6

                    [1, np.nan, 1, np.nan],  # s7、※ LandMark

                    [1, 1, 1, np.nan],  #s8
                    [1, 7, 1, 1],  #s9

                    [np.nan, 1, np.nan, np.nan],  #s10 ※ LandMark

                    [1, np.nan, np.nan, np.nan],  #11
                    [1, 1, np.nan, np.nan],  #12
                    [7, 1, 1, 1],  #13
                    [1, np.nan, np.nan, 1],
                    [1,1,np.nan,np.nan],  #15
                    
                    # ↑、  →、  ↓、  ←         を表す
                    [np.nan, 1, np.nan, 1],  # s16
                    [np.nan, np.nan, 1, 1],  # s17

                    [np.nan, 1, 1, np.nan],  # s18
                    [1, np.nan, np.nan, 1],  # s19

                    [np.nan, 1, 1, np.nan],  # s20                 ※ START

                    [np.nan, 1, np.nan, 1],  # s21
                    [np.nan, np.nan, 1, 1],  # s22

                    [1, np.nan, 1, np.nan],  # s23、                ※ GOAL

                    [1, np.nan, 1, np.nan],  #s24
                    [np.nan, np.nan, 1, 1],  #s25
                    [1, 1, 1, np.nan],  #s26
                    [np.nan, np.nan, 1, 1],  #27
                    [1, np.nan, np.nan, np.nan],  #28
                    [np.nan, np.nan, 1, np.nan],  #29
                    [1, 1, np.nan, np.nan],#30
                    [1,np.nan,np.nan,1],  #31
                    
                    [1,np.nan, np.nan, 1],  # s32
                    [1, 1, np.nan, np.nan],  # s33
                    [np.nan, 1, np.nan, 1],  # s34
                    [1, np.nan,np.nan, 1]  # s35
                   
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

# 1step移動後の状態sを求める関数を定義

A = [0]*36
A[23]=1

state_history = [20]  # エージェントの移動を記録するリスト
SSS = True



def AAA(s):
    #print('総和A[{}] = {}'.format(s,AA[s][0]+AA[s][1]+AA[s][2]+AA[s][3]))
    direction = ["up", "right", "down", "left"]
    
    

    #next_direction = np.random.choice(direction, p=PI[s, :])
    # pi[s,:]の確率に従って、directionが選択される
    #print('PI == {},{}'.format(PI,next_direction))
    
    if A[s] == 1: #14:  # ゴール地点なら終了
        print('終了!!!!')
        print('state_history={}'.format(state_history))
        excp = Exception()
        excp.value = state_history
        raise excp

    A[s] = 2
    print('A[{}] = {},A = {}'.format(s,A[s],A))

    #while A[s+4] != ~~ ここでランダムで選択した方向が2以外になるまで回し続ける

    #if AA[s-6][0]==7 or AA[s+1][1]==7:

    #################LandMark#####################
    #if AA[s][0]==7:
    #    s_next = s + 1  # 左に移動するときは状態の数字が1小さくなる
    #    state_history.append(s_next)
    #    print('ランドマーク発見!!!!s_next = {}'.format(s_next))
    #    AAA(s_next)
    #if AA[s][1]==7:
    #    s_next = s + 6  # 左に移動するときは状態の数字が1小さくなる
    #    state_history.append(s_next)
    #    print('ランドマーク発見!!!!s_next = {}'.format(s_next))
    #    AAA(s_next)


    #if next_direction == "up":
    if A[s-6] < 2 and AA[s][0]==1:
        s_next = s - 6  # 上に移動するときは状態の数字が3小さくなる
        state_history.append(s_next)
        print('111111111111111s_next = {}'.format(s_next))
        AAA(s_next)

    #if next_direction == "right":
    if AA[s][1]==1:
        if A[s+1] < 2:
            s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
            state_history.append(s_next)
            print('2222222222s_next = {}'.format(s_next))
            AAA(s_next)
    


    #if next_direction == "down":
    if AA[s][2]==1:
        if A[s+6] < 2:
            s_next = s + 6  # 下に移動すると
            state_history.append(s_next)
            print('33333333333333s_next = {}'.format(s_next))
            AAA(s_next)
    
    if A[s-1] < 2 and int(AA[s][3])==1:
        s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる
        state_history.append(s_next)
        print('44444444444444s_next = {}'.format(s_next))
        AAA(s_next)
    


    A[s] = 0 #1 #0
    print('再帰関数s={},A={}'.format(s,A))
    print('再帰関数state_history={}'.format(state_history))
    state_history.append(s)
    return state_history
    



# 迷路内をエージェントがゴールするまで移動させる関数の定義

def AAA_top(s):
    try:
        AAA(s)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 20  # スタート地点
    state_history = [20]  # エージェントの移動を記録するリスト
    
    

    state_history = AAA_top(s)
    
    TEST = state_history
    print('確認:{}'.format(TEST))
    
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
    line1.set_data([], [])
    line2.set_data([], [])
    return (line,)

# 現在地S0に緑丸を描画する
line1, = ax.plot([1.5], [2.5], marker="*", color='y', markersize=30)
line2, = ax.plot([1.5], [4.0], marker="d", color='r', markersize=10)

X = [0.]*1000
Y = [0.]*1000

TEST = []

def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    
    x = (state % 6) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y = 5.5 - int(state / 6)  # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    
    x2 = (state % 6) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y2 = 5.5 - int(state / 6)  # y座標は3で割った商を2.5から引く
    X[i] = x2
    Y[i] = y2
    
    #####################
    line1.set_data(X[:i], Y[:i])
    #####################
    #line2.set_data(x, y)
    ax.plot([1.5], [4.5], marker="d", color='r', markersize=20)
    ax.plot([4.5], [4.5], marker="d", color='r', markersize=20)
   
    return (line,) #あってもなくても変わらない


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=300, repeat=False)

HTML(anim.to_jshtml())
plt.show()