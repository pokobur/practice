#無名関数について
#変数名 = lambda 引数１: 式

func = lambda i : i*i
print(func(10))             #10が呼び出されてiに入り結果をfunc返す。


#関数を使って書くとこうなる.
def func(i):
    return i*i
print(func(10))