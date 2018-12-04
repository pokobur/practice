class SampleClass:
    def set_name(self,x):
        self.name = x               # ｘに名前が入る
    def hello(self):                # selfを呼び出してｘを表示させている
        print("Hello, {0}".format(self.name))               
sample = SampleClass()
sample2 = SampleClass()

sample.set_name("python")
sample2.set_name("AI TV")
sample.hello()
sample2.hello()

         