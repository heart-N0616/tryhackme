"""
ハッシュクラッカー


Pyfiglet インストール
sudo apt install python3-pyfiglet


"""

import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("HASH CRACKER for MD5")
print(ascii_banner)

wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('ENTER HASH to be Cracked: '))

with open(wordlist_location,'r') ads file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password :' + line.strip())
            exit(0)

