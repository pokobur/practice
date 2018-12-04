class User:
    def __init__(self, name):           # def __init__  コンストラクタ宣言記述。
        self.name = name            #インスタンス変数　self.name   nameが引数のnameに格納される。
        print ("コンストラクタが呼び出されました")

    def hello(self):
        print ("Hello, " + self.name)#　＋を使うパターン

aitv = User("AItv")         #インスタンス生成   self.nameが格納させる
py = User("python")

aitv.hello()
py.hello()

class pokemon:
    def __init__(self,char):
        self.char = char
    
    def printa(self):
        print("このポケモンは、{}です。" .format(self.char))#　{}.formatを使うパターン

pikachu = pokemon("ピカチュウ")
pikachu.printa()

class kami:
    def __init__(self,name,thing):
        self.name = name
        self.thing = thing
    def output(self):
        print("私は{0}だ。全て{1}する！".format(self.name,self.thing))

hoge = kami("神","破壊")
hoge.output()
