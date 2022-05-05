import numpy as np
import matplotlib.pyplot as plt
import random

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言
fig = plt.figure(figsize=(9, 1))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
plt.text(0.5, 0.5, 'S0', size=14, ha='center')
plt.text(1.5, 0.5, 'S1', size=14, ha='center')
plt.text(2.5, 0.5, 'S2', size=14, ha='center')
plt.text(3.5, 0.5, 'S3', size=14, ha='center')
plt.text(4.5, 0.5, 'S4', size=14, ha='center')
plt.text(5.5, 0.5, 'S5', size=14, ha='center')
plt.text(6.5, 0.5, 'S6', size=14, ha='center')
plt.text(7.5, 0.5, 'S7', size=14, ha='center')
plt.text(8.5, 0.5, 'S8', size=14, ha='center')

plt.text(4.5, 0.3, 'START', ha='center')
plt.text(0.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 9)
ax.set_ylim(0, 1)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([4.5], [0.5], marker="o", color='g', markersize=30)

# 初期の方策を決定するパラメータtheta_0を設定

# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[np.nan, 1, np.nan, np.nan],  # s0
                    [np.nan, 1, np.nan, 1],  # s1
                    [np.nan, 1, np.nan, 1],  # s2
                    [np.nan, 1, np.nan, 1],  # s3
                    [np.nan, 1, np.nan, 1],  # s4
                    [np.nan, 1, np.nan, 1],  # s5
                    [np.nan, 1, np.nan, 1],  # s6

                    [np.nan, 1, np.nan, 1],  # s7、※ LandMark

                    [np.nan, np.nan, np.nan, 1]  #s8

                    ])

# 方策パラメータthetaを行動方策piに変換する関数の定義
[m, n] = theta_0.shape  # thetaの行列サイズを取得
pi_________sub = np.zeros((m, n))
for i in range(0, m):
        pi_________sub[i, :] = np.nansum(theta_0[i, :])  # 割合の計算


def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''

    beta = 1.0

    [m, n] = theta.shape  # thetaの行列サイズを取得
    pi = np.zeros((m, n))
                                                           #exp_theta = np.exp(beta * theta)  # thetaをexp(theta)へと変換
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # 割合の計算
                                                           #pi[i, :] = exp_theta[i, :] / np.nansum(exp_theta[i, :])

    pi = np.nan_to_num(pi)  # nanを0に変換

    return pi


# 初期の方策pi_0を求める
pi_0 = simple_convert_into_pi_from_theta(theta_0)

[a, b] = theta_0.shape  # 行と列の数をa, bに格納
AA = np.nan_to_num(theta_0)  # nanを0に変換

# 初期の方策pi_0を表示
pi_0
print('PI_Softmax=\n{}'.format(pi_0))
PI = pi_0







def get_action_and_next_s(pi, s):
    direction = ["up", "right", "down", "left"]
    # pi[s,:]の確率に従って、directionが選択される
    next_direction = np.random.choice(direction, p=pi[s, :])

    if next_direction == "right":
        action = 1
        s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
    elif next_direction == "left":
        action = 3
        s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる

    print('##########################MAKING_ACTION:{},\npi_0:\n{}'.format(next_direction,pi_0))
    
    return [action, s_next]











# 1step移動後の状態sを求める関数を定義

A = [0]*9
A[0]=1

state_history = [4]  # エージェントの移動を記録するリスト

def AAA(s):
    
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
    #print('A[{}] = {},A = {}'.format(s,A[s],A))






    theta=theta_0
    


    #if next_direction == "right":
    if AA[s][1]==1:
        if A[s+1] < 2:
            s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
            state_history.append(s_next)
            #print('2222222222s_next = {}'.format(s_next))


            # 方策の更新
            # new_theta = update_theta(theta_0, pi_0, state_history)
            # pi = softmax_convert(new_theta)
            # print(pi)
            eta = 0.1 # 学習率
            T = len(state_history) - 1  # ゴールまでの総ステップ数

            [m, n] = theta.shape  # thetaの行列サイズを取得
            delta_theta = theta.copy()  # Δthetaの元を作成、ポインタ参照なので、delta_theta = thetaはダメ
            #print('theta================\n{}'.format(theta))

            #if not(np.isnan(theta[s,1])):  # thetaがnanでない場合
            if pi_0[s,1]>0.1:
                pi_0[s,1]=pi_0[s,1]-0.1
                #print('pi_0[{},1]={}'.format(s,pi_0[s,1]))
                
                #pi_0[i,3]=pi_0[i,3]+0.1

                pi_0[s,3]=1-pi_0[s,1]
                #print('pi___________sub={}'.format(pi_________sub))
                #print('pi_0={}'.format(pi_0))

            #theta = theta + eta * delta_theta

            new_theta=pi_0
            print('new_theta=\n{}'.format(new_theta))



            [action, next_s] = get_action_and_next_s(pi_0, s)
            #PI=new_theta



            # beta = 1.0
            # [m, n] = new_theta.shape  # thetaの行列サイズを取得
            # pi = np.zeros((m, n))

            # exp_theta = np.exp(beta * new_theta)  # thetaをexp(theta)へと変換
            # print('exp_theta=\n{}'.format(exp_theta))

            # for i in range(0, m):
                
            #     pi[i, :] = exp_theta[i, :] / np.nansum(exp_theta[i, :])
            #     # softmaxで計算の場合

            # pi = np.nan_to_num(pi_0)  # nanを0に変換
            # print('#################=\n{}'.format(pi))

            AAA(s_next)
    


    if A[s-1] < 2 and int(AA[s][3])==1:
        s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる
        state_history.append(s_next)
        #print('44444444444444s_next = {}'.format(s_next))
        AAA(s_next)
    


    A[s] = 0 #1 #0
    #print('再帰関数s={},A={}'.format(s,A))
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
    s = 4  # スタート地点
    state_history = [4]  # エージェントの移動を記録するリスト

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
    return (line,)

# 現在地S0に緑丸を描画する
line1, = ax.plot([1.5], [0.5], marker="*", color='y', markersize=30)

X = [0.]*1000
Y = [0.]*1000

def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    
    x = (state % 9) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y = 0.5  # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    
    x2 = (state % 9) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y2 = 0.5  # y座標は3で割った商を2.5から引く
    X[i] = x2
    Y[i] = y2
    
    #####################
    line1.set_data(X[:i], Y[:i])
    #####################

    return (line,) #あってもなくても変わらない


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=1000, repeat=False)

HTML(anim.to_jshtml())
plt.show()