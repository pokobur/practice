
#---------------------------------------------

hoge = "hello,world!"
print (hoge)
#---------------------------------------------
def world():
    hoge = "hello,world!!"
    print (hoge)
world()

#---------------------------------------------
def hello(hoge = "hello,world!!!"):
    print ("{0}".format(hoge))
hello()

#---------------------------------------------
hoge = "hello,world!!!!"
def hogehoge():

    print (hoge)
hogehoge()


#---------------------------------------------
def hoge(name = "Taro",age = 20):
    print("name {0} age ({1})".format(name ,age))
hoge()
hoge("kiro")
hoge(age = (21) , name = "miko" )
