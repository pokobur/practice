from pathlib import Path

def main():
    #p.exists("hogetxt.txt", exist_ok=True)
    hoge = Path("/mnt/c/Users/pokob/Desktop/test.txt")#ファイルをオープンし、変数へ格納
    print(hoge.exists())#ファイル存在確認
    hoge.write_text("fugafugafuga")#ファイル書き込み
    print(hoge.read_text())#ファイル読み込み
    #writeFile = (p.open("/mnt/c/Users/pokob/Desktop/hogetxt.txt").write_text("hogetxt"))
    #print(writeFile)

main()
"""

"""
def substitute():
    hoge = Path("/mnt/c/Users/pokob/Desktop/test.txt")#ファイルを変数へ
    hoge.write_text("fugafuga")#ファイルへ書き込み
    print (hoge.read_text())#ファイルを読み込んで出力
substitute()


#指定したパスにファイルを作って文字列を書き込む処理
Path("/mnt/c/Users/pokob/Desktop/test.txt").write_text("fugafufga") 


