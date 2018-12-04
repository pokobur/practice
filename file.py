'''
ファイルを開く　open(ファイル名、文字コード）←引数
ファイル読み書き　read() / write()
ファイルを閉じる　close()
'''
sample_file = open("read.txt",mode="w",encoding="UTF-8")  #mode="w"はファイルを上書きするという意味。

sample_file.write("I am a god!\n")
sample_file.write("kamikamikamikami\n")
sample_file.close()


sample_file = open("read.txt",encoding="UTF-8")

read_file = sample_file.read()
sample_file.close()
print(read_file)



