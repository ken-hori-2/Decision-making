import numpy as np
import matplotlib.pyplot as plt
import random

from numpy.core.defchararray import title

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言
fig = plt.figure(figsize=(6, 6))
ax = plt.gca()

# 赤い壁を描く
#plt.plot([1, 1], [0, 1], color='black', linewidth=2)
plt.plot([1, 2], [2, 2], color='black', linewidth=2)
#plt.plot([2, 2], [2, 1], color='black', linewidth=2)
#plt.plot([2, 3], [1, 1], color='black', linewidth=2)
plt.plot([3, 4], [5, 5], color='black', linewidth=2)

plt.plot([2, 3], [3, 3], color='black', linewidth=2)
plt.plot([1, 1], [3, 4], color='black', linewidth=2)
#plt.plot([0, 1], [4, 4], color='black', linewidth=2)
plt.plot([1, 2], [5, 5], color='black', linewidth=2)

plt.plot([2, 2], [4, 5], color='black', linewidth=2)
plt.plot([3, 3], [5, 6], color='black', linewidth=2)
plt.plot([4, 5], [3, 3], color='black', linewidth=2)
plt.plot([2, 3], [1, 1], color='black', linewidth=2)
plt.plot([2, 3], [4, 4], color='black', linewidth=2)

plt.plot([5, 5], [1, 3], color='black', linewidth=2)
plt.plot([5, 6], [1, 1], color='black', linewidth=2)
plt.plot([3, 3], [0, 1], color='black', linewidth=2)
plt.plot([2, 2], [1, 2], color='black', linewidth=2)


plt.plot([4, 4], [2, 3], color='black', linewidth=2)
plt.plot([3, 4], [2, 2], color='black', linewidth=2)
plt.plot([2, 2], [2, 3], color='black', linewidth=2)
plt.plot([4, 4], [3, 4], color='black', linewidth=2)
plt.plot([4, 4], [4, 5], color='black', linewidth=2)

plt.plot([2, 3], [5, 5], color='black', linewidth=2)
plt.plot([5, 5], [1, 2], color='black', linewidth=2)
plt.plot([0, 1], [2, 2], color='black', linewidth=2)
plt.plot([0, 1], [3, 3], color='black', linewidth=2)

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


plt.text(2.5, 3.3, 'STATE0', ha='center')
#plt.text(2.5, 5.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
# plt.tick_params(axis='both', which='both', bottom='off', top='off',
#                 labelbottom='off', right='off', left='off', labelleft='off')

# 現在地S0に緑丸を描画する
line, = ax.plot([2.5], [3.5], marker="o", color='g', markersize=30)


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
theta_0 = np.array([[np.nan, 1, 1, np.nan],  # s0
                    [np.nan, 1, np.nan, 1],  # s1
                    [np.nan, np.nan, 1, np.nan],  # s2
                    [np.nan, 1, 1, np.nan],  # s3
                    [1, np.nan, np.nan, np.nan],  # s4
                    [np.nan, np.nan, 1, 1],  # s5
                    [1, 1, np.nan, np.nan],  # s6

                    [np.nan, np.nan, 1, 1],  # s7、※ LandMark

                    [1, 1, 1, np.nan],  #s8
                    [1, 7, 1, 1],  #s9

                    [np.nan, 1, np.nan, np.nan],  #s10 ※ LandMark

                    [1, np.nan, np.nan, np.nan],  #11
                    [1, 1, np.nan, np.nan],  #12
                    [1, 1, np.nan, np.nan],  #13
                    [np.nan, 1, np.nan, 1],
                    [np.nan,np.nan,1,1],  #15
                    
                    # ↑、  →、  ↓、  ←         を表す
                    [np.nan, 1, np.nan, 1],  # s16
                    [np.nan, np.nan, 1, 1],  # s17

                    [np.nan, 1, 1, np.nan],  # s18
                    [1, np.nan, np.nan, 1],  # s19

                    [np.nan, 1, 1, np.nan],  # s20                 ※ START

                    [1, np.nan, np.nan, 1],  # s21
                    [np.nan, np.nan, 1, 1],  # s22

                    [1, np.nan, 1, np.nan],  # s23、                ※ GOAL

                    [1, np.nan, 1, np.nan],  #s24
                    [np.nan, np.nan, 1, 1],  #s25
                    [1, 1, np.nan, np.nan],  #s26
                    [np.nan, 1, np.nan, np.nan],  #27
                    [np.nan, 7, np.nan, 1],  #28
                    [np.nan, np.nan, 1, 1],  #29
                    [1, 1, np.nan, np.nan],#30
                    [1,np.nan,np.nan,1],  #31
                    
                    [1,np.nan, np.nan, 1],  # s32
                    [1, 1, np.nan, np.nan],  # s33
                    [np.nan, 1, np.nan, 1],  # s34
                    [np.nan, np.nan,np.nan, 1]  # s35
                   
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
A[2]=1

state_history = [14]  # エージェントの移動を記録するリスト
SSS = True

COST = 4
A_COST = [0]*36



def AAA(s,depth):
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

    if depth >= 3: #4:
        #excp = Exception()
        #excp.value = state_history
        #raise excp
        if AA[s][1]==7:
            #s_next = s + 6  # 左に移動するときは状態の数字が1小さくなる
            #state_history.append(s_next)
            #print('ランドマーク発見!!!!s_next = {}'.format(s_next))
            #AAA(s_next,depth+1)
            A[s] = 0 #1 #0
            print('コスト3以上　次LMの分岐でゴールから離れる　⇒　引き返す')
            #print('再帰関数state_history={}'.format(state_history))
            state_history.append(s)
            return state_history
        

















    A[s] = 2
    #print('A[{}] = {},A = {}'.format(s,A[s],A))

    #while A[s+4] != ~~ ここでランダムで選択した方向が2以外になるまで回し続ける

    #if AA[s-6][0]==7 or AA[s+1][1]==7:
    if AA[s][0]==7:
        s_next = s + 1  # 左に移動するときは状態の数字が1小さくなる
        state_history.append(s_next)
        print('ランドマーク発見!!!!s_next = {}'.format(s_next))
        AAA(s_next,depth+1)
    if AA[s][1]==7:
        s_next = s + 6  # 左に移動するときは状態の数字が1小さくなる
        state_history.append(s_next)
        print('ランドマーク発見!!!!s_next = {}'.format(s_next))
        AAA(s_next,depth+1)


    #if next_direction == "up":
    if A[s-6] < 2 and AA[s][0]==1:
        s_next = s - 6  # 上に移動するときは状態の数字が3小さくなる
        state_history.append(s_next)
        #print('111111111111111s_next = {}'.format(s_next))
        #print('COST -1 : {}'.format(COST))
        print('depth {}'.format(depth))
        AAA(s_next,depth+1)

    #if next_direction == "right":
    if AA[s][1]==1:
        if A[s+1] < 2:
            s_next = s + 1  # 右に移動するときは状態の数字が1大きくなる
            state_history.append(s_next)
            #print('2222222222s_next = {}'.format(s_next))
            #print('COST +1 : {}'.format(COST))
            print('depth {}'.format(depth))
            AAA(s_next,depth+1)
    


    #if next_direction == "down":
    if AA[s][2]==1:
        if A[s+6] < 2:
            s_next = s + 6  # 下に移動すると
            state_history.append(s_next)
            #print('33333333333333s_next = {}'.format(s_next))
            #print('COST +1 : {}'.format(COST))
            print('depth {}'.format(depth))
            AAA(s_next,depth+1)
    
    if A[s-1] < 2 and int(AA[s][3])==1:
        s_next = s - 1  # 左に移動するときは状態の数字が1小さくなる
        state_history.append(s_next)
        #print('44444444444444s_next = {}'.format(s_next))
        #print('COST -1 : {}'.format(COST))
        print('depth {}'.format(depth))
        AAA(s_next,depth+1)
    


    A[s] = 0 #1 #0
    #print('再帰関数s={},A={}'.format(s,A))
    #print('再帰関数state_history={}'.format(state_history))
    state_history.append(s)
    return state_history
    



# 迷路内をエージェントがゴールするまで移動させる関数の定義

def AAA_top(s,depth):
    try:
        AAA(s,depth)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 14  # スタート地点
    state_history = [14]  # エージェントの移動を記録するリスト
    
    

    state_history = AAA_top(s,0)
    
    TEST = state_history
    #print('確認:{}'.format(TEST))
    
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

#def init():
'''背景画像の初期化'''
line1, = ax.plot([1.5], [2.5], marker="*", color='y', markersize=30)
# line.set_data([], [])
# line1.set_data([], [])
ax.plot([1.0], [3.5], marker="d", color='r', markersize=20)
ax.plot([0.0], [4.5], marker="d", color='r', markersize=20)
ax.plot([4.0], [3.5], marker="d", color='b', markersize=20)
ax.plot([5.0], [1.5], marker="d", color='b', markersize=20)

ax.plot([0.5], [3.5], marker="s", color='k', markersize=50)
ax.plot([2.5], [4.5], marker="s", color='k', markersize=50)
ax.plot([3.5], [0.5], marker="s", color='k', markersize=50)


X = [0.]*1000
Y = [0.]*1000


def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    
    x2 = (state % 6) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y2 = 5.5 - int(state / 6)  # y座標は3で割った商を2.5から引く
    X[i] = x2
    Y[i] = y2
    
    #####################
    line1.set_data(X[:i], Y[:i])
    #p1.set_data((position_x[:i],position_y[:i]))
    #####################

    # if len(imgs)>0:
    #     imgs.pop().remove()
    # H, xedge, yedge = np.histogram2d(position_x[:i], position_y[:i],bins=(xedges, yedges))
    # img = ax.imshow(H.T, interpolation='nearest', origin='lower',
    #     extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], vmin=H_min, vmax=H_max)
    # imgs.append(img)



   
    return (line, ) #あってもなくても変わらない




#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, frames=len(
    state_history), interval=1000, repeat=False)

HTML(anim.to_jshtml())
plt.show()





xlim= ax.set_xlim(0, 6)#ax.get_xlim()
ylim= ax.set_ylim(0, 6)#ax.get_ylim()
from mpl_toolkits.axes_grid1 import make_axes_locatable

for i in range(len(state_history)):
    state = state_history[i]  # 現在の場所を描く
    x2 = (state % 6) + 0.5  # 状態のx座標は、3で割った余り+0.5
    y2 = 5.5 - int(state / 6)  # y座標は3で割った商を2.5から引く
    position_x = np.cumsum(x2)  #累積和 x
    position_y = np.cumsum(y2)  #累積和 y
    X[i] = x2
    Y[i] = y2

# 描画範囲の設定と目盛りを消す設定



xedges = np.linspace(xlim[0],xlim[1],10)
yedges = np.linspace(ylim[0],ylim[1],10)
xedges,yedges



#np.histogram2dでヒストグラムデータを求める。Hが各区画における頻度のデータとなる。
H, xedge, yedge = np.histogram2d(position_x, position_y,bins=(xedges, yedges))


#頻度データHは.Tで転置させることでランダムウォークとの位置関係が一致する。
#カラーバーはmake_axes_locatableで設置する。
fig, ax = plt.subplots(figsize=(6,6))
im = ax.imshow(H.T, interpolation='nearest', origin='lower',
          extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
plt.colorbar(im, cax=cax)
#fig.savefig("2Drandomwalk_heatmap.png", dpi=100,transparent = False, bbox_inches = 'tight')
#plt.show()
H_max = H.max()
H_min = H.min()


fig, axes = plt.subplots(figsize=(6,6))
#ax = axes.ravel()
#p1, = ax.plot([], [],'o-',color='C3',alpha=0.5)
#return (line,)

# ax[0].grid()
# ax[0].set(xlim=xlim, ylim=ylim)
# ax[0].set_xlabel('x')
# ax[0].set_ylabel('y')

imgs = []
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
plt.colorbar(im, cax=cax)



def update(i):
    line1.set_data((X[:i],Y[:i]))
    
    if len(imgs)>0:
        imgs.pop().remove()
    H, xedge, yedge = np.histogram2d(position_x[:i], position_y[:i],bins=(xedges, yedges))
    img = ax.imshow(H.T, interpolation='nearest', origin='lower',
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], vmin=H_min, vmax=H_max)
    imgs.append(img)
    return fig,


ani = animation.FuncAnimation( #fig, update, 500,interval=200, blit=True)
    # #ani.save('rw2d_anim_heatmap.mp4', writer="matplotlib.animation.PillowWriter",dpi=100)
    # HTML(ani.to_html5_video())
    # #HTML(ani.to_jshtml())
    # plt.show()


    fig, update, frames=500, interval=200, repeat=False)

HTML(ani.to_jshtml())
plt.show()
