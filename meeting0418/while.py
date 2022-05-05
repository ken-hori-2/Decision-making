counter = 1 # 現在、何回目かを記録する変数

while counter <= 10:  # counterの値が10以下なら繰り返す
    text = input("数字を入力してください")
    
    # if 入力された文字が ''なら
    if text == '':
        print("入力が無効です")
        # ループの先頭に戻る
        continue

    # 入力された文字が '999' なら
    if text == '999':
        # ループを中断する
        print("中断します")
        break

    number = int(text) # 入力した文字列を数値に変換する
    print(counter, "回目:", number * number) # 入力した数値の2乗を表示する
    counter = counter + 1  # counter の値に 1 を加算する

print("終了しました")