

try:            #ｴﾗｰが起きない場合実行 ＊一つ例外が発生するとそこで処理が止まる
    print (10/1)
    print(a)
    print("i"+ 1)

except ZeroDivisionError:         #例外発生時に実行
      print("０で割ってはいけません！")

#タプル型で例外を複数書くこともできる。
except (TypeError,NameError,NotADirectoryError):
    print("例外が発生しました")
    
