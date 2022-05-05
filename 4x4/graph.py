url = 'https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/location.txt'

# URL によるリソースへのアクセスを提供するライブラリをインポートする。
#import urllib # Python 2 の場合
import urllib.request # Python 3 の場合
# 指定したURLからリソースをダウンロードし、名前をつける。
#urllib.urlretrieve(url, 'location.txt') # Python 2 の場合
urllib.request.urlretrieve(url, 'location.txt') # Python 3 の場合