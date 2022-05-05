# 使用するパッケージの宣言
import numpy as np
import matplotlib.pyplot as plt
import random
#get_ipython().run_line_magic('matplotlib', 'inline')

# 図を描く大きさと、図の変数名を宣言
fig = plt.figure(figsize=(20, 20))
ax = plt.gca()

# 状態を示す文字S0～S99を描く
plt.text(0.5, 9.5, 'S0', size=14, ha='center')
plt.text(1.5, 9.5, 'S1', size=14, ha='center')
plt.text(2.5, 9.5, 'S2', size=14, ha='center')
plt.text(3.5, 9.5, 'S3', size=14, ha='center')
plt.text(4.5, 9.5, 'S4', size=14, ha='center')
plt.text(5.5, 9.5, 'S5', size=14, ha='center')
plt.text(6.5, 9.5, 'S6', size=14, ha='center')
plt.text(7.5, 9.5, 'S7', size=14, ha='center')
plt.text(8.5, 9.5, 'S8', size=14, ha='center')
plt.text(9.5, 9.5, 'S9', size=14, ha='center')

plt.text(0.5, 8.5, 'S10', size=14, ha='center')
plt.text(1.5, 8.5, 'S11', size=14, ha='center')
plt.text(2.5, 8.5, 'S12', size=14, ha='center')
plt.text(3.5, 8.5, 'S13', size=14, ha='center')
plt.text(4.5, 8.5, 'S14', size=14, ha='center')
plt.text(5.5, 8.5, 'S15', size=14, ha='center')
plt.text(6.5, 8.5, 'S16', size=14, ha='center')
plt.text(7.5, 8.5, 'S17', size=14, ha='center')
plt.text(8.5, 8.5, 'S18', size=14, ha='center')
plt.text(9.5, 8.5, 'S19', size=14, ha='center')

plt.text(0.5, 7.5, 'S20', size=14, ha='center')
plt.text(1.5, 7.5, 'S21', size=14, ha='center')
plt.text(2.5, 7.5, 'S22', size=14, ha='center')
plt.text(3.5, 7.5, 'S23', size=14, ha='center')
plt.text(4.5, 7.5, 'S24', size=14, ha='center')
plt.text(5.5, 7.5, 'S25', size=14, ha='center')
plt.text(6.5, 7.5, 'S26', size=14, ha='center')
plt.text(7.5, 7.5, 'S27', size=14, ha='center')
plt.text(8.5, 7.5, 'S28', size=14, ha='center')
plt.text(9.5, 7.5, 'S29', size=14, ha='center')


plt.text(0.5, 6.5, 'S30', size=14, ha='center')
plt.text(1.5, 6.5, 'S31', size=14, ha='center')
plt.text(2.5, 6.5, 'S32', size=14, ha='center')
plt.text(3.5, 6.5, 'S33', size=14, ha='center')
plt.text(4.5, 6.5, 'S34', size=14, ha='center')
plt.text(5.5, 6.5, 'S35', size=14, ha='center')
plt.text(6.5, 6.5, 'S36', size=14, ha='center')
plt.text(7.5, 6.5, 'S37', size=14, ha='center')
plt.text(8.5, 6.5, 'S38', size=14, ha='center')
plt.text(9.5, 6.5, 'S39', size=14, ha='center')

plt.text(0.5, 5.5, 'S40', size=14, ha='center')
plt.text(1.5, 5.5, 'S41', size=14, ha='center')
plt.text(2.5, 5.5, 'S42', size=14, ha='center')
plt.text(3.5, 5.5, 'S43', size=14, ha='center')
plt.text(4.5, 5.5, 'S44', size=14, ha='center')
plt.text(5.5, 5.5, 'S45', size=14, ha='center')
plt.text(6.5, 5.5, 'S46', size=14, ha='center')
plt.text(7.5, 5.5, 'S47', size=14, ha='center')
plt.text(8.5, 5.5, 'S48', size=14, ha='center')
plt.text(9.5, 5.5, 'S49', size=14, ha='center')

plt.text(0.5, 4.5, 'S50', size=14, ha='center')
plt.text(1.5, 4.5, 'S51', size=14, ha='center')
plt.text(2.5, 4.5, 'S52', size=14, ha='center')
plt.text(3.5, 4.5, 'S53', size=14, ha='center')
plt.text(4.5, 4.5, 'S54', size=14, ha='center')
plt.text(5.5, 4.5, 'S55', size=14, ha='center')
plt.text(6.5, 4.5, 'S56', size=14, ha='center')
plt.text(7.5, 4.5, 'S57', size=14, ha='center')
plt.text(8.5, 4.5, 'S58', size=14, ha='center')
plt.text(9.5, 4.5, 'S59', size=14, ha='center')

plt.text(0.5, 3.5, 'S60', size=14, ha='center')
plt.text(1.5, 3.5, 'S61', size=14, ha='center')
plt.text(2.5, 3.5, 'S62', size=14, ha='center')
plt.text(3.5, 3.5, 'S63', size=14, ha='center')
plt.text(4.5, 3.5, 'S64', size=14, ha='center')
plt.text(5.5, 3.5, 'S65', size=14, ha='center')
plt.text(6.5, 3.5, 'S66', size=14, ha='center')
plt.text(7.5, 3.5, 'S67', size=14, ha='center')
plt.text(8.5, 3.5, 'S68', size=14, ha='center')
plt.text(9.5, 3.5, 'S69', size=14, ha='center')


plt.text(0.5, 2.5, 'S70', size=14, ha='center')
plt.text(1.5, 2.5, 'S71', size=14, ha='center')
plt.text(2.5, 2.5, 'S72', size=14, ha='center')
plt.text(3.5, 2.5, 'S73', size=14, ha='center')
plt.text(4.5, 2.5, 'S74', size=14, ha='center')
plt.text(5.5, 2.5, 'S75', size=14, ha='center')
plt.text(6.5, 2.5, 'S76', size=14, ha='center')
plt.text(7.5, 2.5, 'S77', size=14, ha='center')
plt.text(8.5, 2.5, 'S78', size=14, ha='center')
plt.text(9.5, 2.5, 'S79', size=14, ha='center')

plt.text(0.5, 1.5, 'S80', size=14, ha='center')
plt.text(1.5, 1.5, 'S81', size=14, ha='center')
plt.text(2.5, 1.5, 'S82', size=14, ha='center')
plt.text(3.5, 1.5, 'S83', size=14, ha='center')
plt.text(4.5, 1.5, 'S84', size=14, ha='center')
plt.text(5.5, 1.5, 'S85', size=14, ha='center')
plt.text(6.5, 1.5, 'S86', size=14, ha='center')
plt.text(7.5, 1.5, 'S87', size=14, ha='center')
plt.text(8.5, 1.5, 'S88', size=14, ha='center')
plt.text(9.5, 1.5, 'S89', size=14, ha='center')

plt.text(0.5, 0.5, 'S90', size=14, ha='center')
plt.text(1.5, 0.5, 'S91', size=14, ha='center')
plt.text(2.5, 0.5, 'S92', size=14, ha='center')
plt.text(3.5, 0.5, 'S93', size=14, ha='center')
plt.text(4.5, 0.5, 'S94', size=14, ha='center')
plt.text(5.5, 0.5, 'S95', size=14, ha='center')
plt.text(6.5, 0.5, 'S96', size=14, ha='center')
plt.text(7.5, 0.5, 'S97', size=14, ha='center')
plt.text(8.5, 0.5, 'S98', size=14, ha='center')
plt.text(9.5, 0.5, 'S99', size=14, ha='center')

plt.text(0.5, 9.3, 'START', ha='center')
plt.text(9.5, 0.3, 'GOAL', ha='center')

# 赤い壁を描く
plt.plot([1, 2], [9, 9], color='red', linewidth=2)
plt.plot([3, 3], [4, 9], color='red', linewidth=2)
plt.plot([4, 5], [6, 6], color='red', linewidth=2)
plt.plot([4, 9], [4, 4], color='red', linewidth=2)
plt.plot([3, 9], [4, 4], color='red', linewidth=2)
plt.plot([4, 9], [6, 6], color='red', linewidth=2)
plt.plot([5, 5], [4, 5], color='red', linewidth=2)
plt.plot([6, 6], [5, 6], color='red', linewidth=2)
plt.plot([7, 7], [4, 5], color='red', linewidth=2)
plt.plot([8, 8], [5, 6], color='red', linewidth=2)
plt.plot([0, 3], [9, 9], color='red', linewidth=2)
plt.plot([9, 9], [0, 4], color='red', linewidth=2)
plt.plot([9, 9], [6, 9], color='red', linewidth=2)
plt.plot([4, 4], [6, 9], color='red', linewidth=2)
plt.plot([4, 9], [9, 9], color='red', linewidth=2)

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [9.5], marker="o", color='g', markersize=30)

# 初期の方策を決定するパラメータtheta_0を設定
# 行は状態0～98、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[np.nan, 1, np.nan, np.nan],  # s0
                    [np.nan, 1, np.nan, 1],  # s1
                    [np.nan, 1, np.nan, 1],  # s2
                    [np.nan, 1, 1, 1],  # s3
                    [np.nan, 1, np.nan, 1],  # s4
                    [np.nan, 1, np.nan, 1],  # s5
                    [np.nan, 1, np.nan, 1],  # s6
                    [np.nan, 1, np.nan, 1],  # s7
                    [np.nan, 1, np.nan, 1],  # s8
                    [np.nan, np.nan, 1, 1],  # s9
                    [np.nan, np.nan, np.nan, np.nan],  # s10
                    [np.nan, np.nan, np.nan, np.nan],  # s11
                    [np.nan, np.nan, np.nan, np.nan],  # s12
                    [1, np.nan, 1, np.nan],  # s13
                    [np.nan, np.nan, np.nan, np.nan],  # s14
                    [np.nan, np.nan, np.nan, np.nan],  # s15
                    [np.nan, np.nan, np.nan, np.nan],  # s16
                    [np.nan, np.nan, np.nan, np.nan],  # s17
                    [np.nan, np.nan, np.nan, np.nan],  # s18
                    [1, np.nan, 1, np.nan],  # s19
                    [np.nan, np.nan, np.nan, np.nan],  # s20
                    [np.nan, np.nan, np.nan, np.nan],  # s21
                    [np.nan, np.nan, np.nan, np.nan],  # s22
                    [1, np.nan, 1, np.nan],  # s23
                    [np.nan, np.nan, np.nan, np.nan],  # s24
                    [np.nan, np.nan, np.nan, np.nan],  # s25
                    [np.nan, np.nan, np.nan, np.nan],  # s26
                    [np.nan, np.nan, np.nan, np.nan],  # s27
                    [np.nan, np.nan, np.nan, np.nan],  # s28
                    [1, np.nan, 1, np.nan],  # s29
                    [np.nan, np.nan, np.nan, np.nan],  # s30
                    [np.nan, np.nan, np.nan, np.nan],  # s31
                    [np.nan, np.nan, np.nan, np.nan],  # s32
                    [1, np.nan, 1, np.nan],  # s33
                    [np.nan, np.nan, np.nan, np.nan],  # s34
                    [np.nan, np.nan, np.nan, np.nan],  # s35
                    [np.nan, np.nan, np.nan, np.nan],  # s36
                    [np.nan, np.nan, np.nan, np.nan],  # s37
                    [np.nan, np.nan, np.nan, np.nan],  # s38
                    [1, np.nan, 1, np.nan],  # s39
                    [np.nan, np.nan, np.nan, np.nan],  # s40
                    [np.nan, np.nan, np.nan, np.nan],  # s41
                    [np.nan, np.nan, np.nan, np.nan],  # s42
                    [1, 1, 1, np.nan],  # s43
                    [np.nan, 1, 1, 1],  # s44
                    [np.nan, np.nan, 1, 1],  # s45
                    [np.nan, 1, 1, np.nan],  # s46
                    [np.nan, np.nan, 1, 1],  # s47
                    [np.nan, 1, 1, np.nan],  # s48
                    [1, np.nan, 1, 1],  # s49
                    [np.nan, np.nan, np.nan, np.nan],  # s50
                    [np.nan, np.nan, np.nan, np.nan],  # s51
                    [np.nan, np.nan, np.nan, np.nan],  # s52
                    [1, 1, np.nan, np.nan],  # s53
                    [1, np.nan, np.nan, 1],  # s54
                    [1, 1, np.nan, np.nan],  # s55
                    [1, np.nan, np.nan, 1],  # s56
                    [1, 1, np.nan, np.nan],  # s57
                    [1, 1, np.nan, 1],  # s58
                    [1, np.nan, 1, 1],  # s59
                    # 行は状態0～7、列は移動方向で↑、→、↓、←を表す
                    [np.nan, np.nan, np.nan, np.nan],  # 60
                    [np.nan, np.nan, np.nan, np.nan],  # s61
                    [np.nan, np.nan, np.nan, np.nan],  # s62
                    [np.nan, np.nan, np.nan, np.nan],  # s63
                    [np.nan, np.nan, np.nan, np.nan],  # s64
                    [np.nan, np.nan, np.nan, np.nan],  # s65
                    [np.nan, np.nan, np.nan, np.nan],  # s66
                    [np.nan, np.nan, np.nan, np.nan],  # s67
                    [np.nan, np.nan, np.nan, np.nan],  # s68
                    [1, np.nan, 1, np.nan],  # s69
                    [np.nan, np.nan, np.nan, np.nan],  # s70
                    [np.nan, np.nan, np.nan, np.nan],  # s71
                    [np.nan, np.nan, np.nan, np.nan],  # s72
                    [np.nan, np.nan, np.nan, np.nan],  # s73
                    [np.nan, np.nan, np.nan, np.nan],  # s74
                    [np.nan, np.nan, np.nan, np.nan],  # s75
                    [np.nan, np.nan, np.nan, np.nan],  # s76
                    [np.nan, np.nan, np.nan, np.nan],  # s77
                    [np.nan, np.nan, np.nan, np.nan],  # s78
                    [1, np.nan, 1, np.nan],  # s79
                    [np.nan, np.nan, np.nan, np.nan],  # s80
                    [np.nan, np.nan, np.nan, np.nan],  # s81
                    [np.nan, np.nan, np.nan, np.nan],  # s82
                    [np.nan, np.nan, np.nan, np.nan],  # s83
                    [np.nan, np.nan, np.nan, np.nan],  # s84
                    [np.nan, np.nan, np.nan, np.nan],  # s85
                    [np.nan, np.nan, np.nan, np.nan],  # s86
                    [np.nan, np.nan, np.nan, np.nan],  # s87
                    [np.nan, np.nan, np.nan, np.nan],  # s88
                    [1, np.nan, 1, np.nan],  # s89
                    [np.nan, np.nan, np.nan, np.nan],  # s90
                    [np.nan, np.nan, np.nan, np.nan],  # s91
                    [np.nan, np.nan, np.nan, np.nan],  # s92
                    [np.nan, np.nan, np.nan, np.nan],  # s93
                    [np.nan, np.nan, np.nan, np.nan],  # s94
                    [np.nan, np.nan, np.nan, np.nan],  # s95
                    [np.nan, np.nan, np.nan, np.nan],  # s96
                    [np.nan, np.nan, np.nan, np.nan],  # s97
                    [np.nan, np.nan, np.nan, np.nan],  # s98
                    ])


# 方策パラメータtheta_0をランダム方策piに変換する関数の定義


def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''

    [m, n] = theta.shape  # thetaの行列サイズを取得
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # 割合の計算

    pi = np.nan_to_num(pi)  # nanを0に変換

    return pi

# ランダム行動方策pi_0を求める
pi_0 = simple_convert_into_pi_from_theta(theta_0)

print(pi_0)


def get_next_s(pi, s):
    direction = ["up", "right", "down", "left"]

    a = random.randint(1,2)
    b = random.randint(1,2)
    if a == 1:
        if b == 1:
         #continue
         print("pass")
         pass
        elif pi[s,1]!=0 : # and s+3
            print('右　優先')
            print("{}:右に行く:{}".format(s,pi[s,1]))
            s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
            return s_next
        elif pi[s,2]!=0:
            print("{}:下に行く:{}".format(s,pi[s,2]))
            s_next = s + 10  # 下に移動するときは状態の数字が3大きくなる
            return s_next
    else:
        if b == 1:
         #continue
         print("pass")
         pass
        elif pi[s,2]!=0:
            print('下　優先')
            print("{}:下に行く:{}".format(s,pi[s,2]))
            s_next = s + 10  # 下に移動するときは状態の数字が3大きくなる
            return s_next
        elif pi[s,1]!=0:
            print("{}:右に行く:{}".format(s,pi[s,1]))
            s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
            return s_next


    next_direction = np.random.choice(direction, p=pi[s, :])
    # pi[s,:]の確率に従って、directionが選択される

    # 行動から次の状態を決める
    if next_direction == "up":
        s_next = s - 10  # 上に移動するときは状態の数字が3小さくなる
    elif next_direction == "right":
        s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
    elif next_direction == "down":
        s_next = s + 10  # 下に移動するときは状態の数字が3大きくなる
    elif next_direction == "left":
        s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる

    return s_next

# 迷路内をエージェントがゴールするまで移動させる関数の定義


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = [0]  # エージェントの移動を記録するリスト

    while (1):  # ゴールするまでループ
        next_s = get_next_s(pi, s)
        state_history.append(next_s)  # 記録リストに次の状態（エージェントの位置）を追加

        if next_s == 99:  # ゴール地点なら終了
            break
        else:
            s = next_s

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
    # 背景画像の初期化
    line.set_data([], [])
    return (line,)


def animate(i):
    # フレームごとの描画内容
    state = state_history[i] # 現在の場所を描く
    x = (state % 10) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y = 9.5 - int(state / 10)  # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=200, repeat=False)

HTML(anim.to_jshtml())
plt.show()