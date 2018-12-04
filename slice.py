#スライスは文字列の中から指定した文字列を取り出すことができる
#文字列　a b c d e 　[0]=a, [1]=b, [2]=c, [3]=d, [4]=e
'''[start:end]startからend-1までも文字列を取り出すことができる。
   [start:]startから末尾まで,[:end]=先頭からend-1まで,[:]=全部, 
   [start:end:step]=先頭からstepごとにstartからend-1まで。Stepを-1すると逆になる。
'''

x = "abcde"
print(x[0:4])#abcd
print(x[2:])#cde
print(x[:3])#abc
print(x[:])#abcde
print(x[0:4:2])#ace
print(x[::-1])#edcba

