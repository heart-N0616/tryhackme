"""
�t�@�C���_�E�����[�_�[
"""
import requests

url ="https://"
r=requests.get(url,allow_redirects=True)
open('�t�@�C����.png','wb').write(r.content)

