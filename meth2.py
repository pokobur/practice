class Phone():

    os = ("Android⚡⚡")
    status = ("ただいま")

    def __init__(self):
        print(self.os)

    def call(self,real):
        print(self.real)
        print(self.status,end="")    # end="" ←改行なしコード
        print("～話し中～")
        
        
hoge = Phone()
hoge.call()
hoge.call("と見せかけて実は居留守")