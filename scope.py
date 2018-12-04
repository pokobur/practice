
msg = "message"

def sample():
    msg = "関数が呼び出されました。"
    print (msg)
    print (msg)
sample()
print(msg)


mas = "come"
def sample():
   # mas = "emoc"
    print (mas)
sample()      #ローカル変数がないため、グローバル変数が呼び出させる。
print (mas)   #グローバル変数呼び出し。


mis = "hoge"
def sample():
    mis = "egoh"
    print(mis)
sample()        #ローカル変数呼び出し
print (mis)     #グローバル変数呼び出さし


kis = "ruru"
def sample():
    global kis        #グローバル変数をローカル変数に書き換える 
    kis = "urur"
    print (kis)
sample()
print (kis)

