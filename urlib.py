import urllib.request


url = " http://www.tuis.ac.jp/common/image/logo-pc.gif"

savename = "tuis.png"

png = urllib.request.urlopen(url).read()

with open(savename,mode="wb") as f:
    f.write(png)
    print("保存しました")
