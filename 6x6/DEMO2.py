from time import sleep

#探索様子を追跡する関数（迷路の更新を出力する）
def track(maze, depth):
    draw = f"{depth}手目\n"
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] > 2:
                draw += "■ "    #壁
            elif maze[x][y] == 2:
                draw += "*  "    #探索済みの道
            elif maze[x][y] == 1:
                draw += "G  "   #ゴール位置
            else:
                draw += "　 "    #未探索の道

        draw += "\n"
    print(draw)

#探索関数：ゴールしたらそのときの位置・移動数を返す
def Maze(x, y, depth):
    i=0
    #ゴールについた時点で終了
    if maze[x][y] == 1:
        print([(x, y), depth])
        exit()

    #探索済みとしてセット
    maze[x][y] = 2
    #1秒ごとに図の更新
    sleep(0.5)
    track(maze, depth)

    #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
    if maze[x-1][y] < 2:#左
        Maze(x-1, y, depth + 1)
    if maze[x+1][y] < 2:#右
        Maze(x+1, y, depth + 1)
    if maze[x][y-1] < 2:#上
        Maze(x, y-1, depth + 1)
    if maze[x][y+1] < 2:#下
        Maze(x, y+1, depth + 1)

    #探索前に戻す
    maze[x][y] = 0
    i +=1
    print('探索前に戻る x,y:{},{},{}'.format(x,y,depth))

if __name__ == '__main__':
    #迷路作成
    maze = [
                [9, 9, 9, 9, 9, 9],
                [9, 0, 0, 0, 1, 9],
                [9, 0, 9, 0, 9, 9],
                [9, 0, 0, 9, 0, 9],
                [9, 0, 0, 0, 0, 9],
                [9, 9, 9, 9, 9, 9]
                ]

    result = Maze(4, 1, 0)  #探索