"""
ファイルダウンローダー
"""
import requests

url ="https://"
r=requests.get(url,allow_redirects=True)
open('ファイル名.png','wb').write(r.content)

