class Test:
    def __init__(self, num):
        self.num = num;
    
    def print_num(self):
        print('引数で渡された数字は{}です。'.format(self.num))
    
    class Test2(Test):
        def print_test2_info(self):
            print('このクラスはTestクラスを継承しています。')
            super().print_num() #親クラスのprint_numを呼び出す。

hoge = Test2(10)
hoge.print_test2_info()
