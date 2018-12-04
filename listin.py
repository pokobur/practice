'''
lists = []
for i in range(10):
    lists.append(i)
print(lists)
'''
print([i for i in range(10)])       #リスト内包表記なら↑のプログラムを一行で書ける。
print([i*2 for i in range(10)])     #i＊2することで二倍のリストが作られる。

#集合リストでも作れる。
print({i*5 for i in range(10) if i%2==0})  #0~8までが5倍され、2で割られている。0*5, 2*5, 4*5......

#辞書リストでも作れる。　
print({i:i for i in range(10)})

