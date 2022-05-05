# 使用するパッケージの宣言
import numpy as np
import matplotlib.pyplot as plt
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
line, = ax.plot([0.5], [9.5], marker="o", color='g', markersize=60)

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


# 初期の行動価値関数Qを設定

[a, b] = theta_0.shape  # 行と列の数をa, bに格納
Q = np.random.rand(a, b) * theta_0 * 0.1
# *theta0をすることで要素ごとに掛け算をし、Qの壁方向の値がnanになる


# ε-greedy法を実装


def get_action(s, Q, epsilon, pi_0):
    direction = ["up", "right", "down", "left"]

    # 行動を決める
    if np.random.rand() < epsilon:
        # εの確率でランダムに動く
        next_direction = np.random.choice(direction, p=pi_0[s, :])
    else:
        # Qの最大値の行動を採用する
        next_direction = direction[np.nanargmax(Q[s, :])]

    # 行動をindexに
    if next_direction == "up":
        action = 0
    elif next_direction == "right":
        action = 1
    elif next_direction == "down":
        action = 2
    elif next_direction == "left":
        action = 3

    return action


def get_s_next(s, a, Q, epsilon, pi_0):
    direction = ["up", "right", "down", "left"]
    next_direction = direction[a]  # 行動aの方向

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


# Q学習による行動価値関数Qの更新


def Q_learning(s, a, r, s_next, Q, eta, gamma):

    if s_next == 99:  # ゴールした場合
        Q[s, a] = Q[s, a] + eta * (r - Q[s, a])

    else:
        Q[s, a] = Q[s, a] + eta * (r + gamma * np.nanmax(Q[s_next,: ]) - Q[s, a])

    return Q



# Q学習で迷路を解く関数の定義、状態と行動の履歴および更新したQを出力


def goal_maze_ret_s_a_Q(Q, epsilon, eta, gamma, pi):
    s = 0  # スタート地点
    a = a_next = get_action(s, Q, epsilon, pi)  # 初期の行動
    s_a_history = [[0, np.nan]]  # エージェントの移動を記録するリスト

    while (1):  # ゴールするまでループ
        a = a_next  # 行動更新

        s_a_history[-1][1] = a
        # 現在の状態（つまり一番最後なのでindex=-1）に行動を代入

        s_next = get_s_next(s, a, Q, epsilon, pi)
        # 次の状態を格納

        s_a_history.append([s_next, np.nan])
        # 次の状態を代入。行動はまだ分からないのでnanにしておく

        # 報酬を与え,　次の行動を求めます
        if s_next == 99:
            r = 1  # ゴールにたどり着いたなら報酬を与える
            a_next = np.nan
        else:
            r = 0
            a_next = get_action(s_next, Q, epsilon, pi)
            # 次の行動a_nextを求めます。

        # 価値関数を更新
        Q = Q_learning(s, a, r, s_next, Q, eta, gamma)

        # 終了判定
        if s_next == 99:  # ゴール地点なら終了
            break
        else:
            s = s_next

    return [s_a_history, Q]

# Q学習で迷路を解く

eta = 0.1  # 学習率
gamma = 0.9  # 時間割引率
epsilon = 0.5  # ε-greedy法の初期値
v = np.nanmax(Q, axis=1)  # 状態ごとに価値の最大値を求める
is_continue = True
episode = 1

V = []  # エピソードごとの状態価値を格納する
V.append(np.nanmax(Q, axis=1))  # 状態ごとに行動価値の最大値を求める

while is_continue:  # is_continueがFalseになるまで繰り返す
    print("エピソード:" + str(episode))

    # ε-greedyの値を少しずつ小さくする
    epsilon = epsilon / 2

    # Q学習で迷路を解き、移動した履歴と更新したQを求める
    [s_a_history, Q] = goal_maze_ret_s_a_Q(Q, epsilon, eta, gamma, pi_0)

    # 状態価値の変化
    new_v = np.nanmax(Q, axis=1)  # 状態ごとに行動価値の最大値を求める
    print(np.sum(np.abs(new_v - v)))  # 状態価値関数の変化を出力
    v = new_v
    V.append(v)  # このエピソード終了時の状態価値関数を追加

    print("迷路を解くのにかかったステップ数は" + str(len(s_a_history) - 1) + "です")

    # 100エピソード繰り返す
    episode = episode + 1
    if episode > 100:
        break



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
    state = s_a_history[i][0]  # 現在の場所を描く
    x = (state % 10) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y = 9.5 - int(state / 10)  # y座標は3で割った商を2.5から引く
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    s_a_history), interval=200, repeat=False)

HTML(anim.to_jshtml())
plt.show()