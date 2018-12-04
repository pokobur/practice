class Phone():
    
    status = ("ただいま")

    def __init__(self,os):
        print("OSは、",end="")
        self.os = os
    
    def cell(self):
        print(self.status,end="")
        print("～話し中～")

hoge = Phone("Android⚡⚡")    #引数は初期化メソッドの第二引数(os)に入る
print(hoge.os)

hoge.cell()