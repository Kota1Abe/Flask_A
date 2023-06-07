"""
from Crypto.Cipher import AES
import base64

message = "自分がしてほしいと思うことを人にもするように"
password = "kitazawayuuuhope"
iv = "l3je8dKLd3lFu31F"
mode = AES.MODE_CBC

def mkpad(s,size):
    s = s.encode("utf-8")
    pad = b' ' * (size - len(s) % size)
    return s + pad

def ench
"""

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def create_aes(password, iv):
    sha = SHA256.new()
    sha.update(password.encode())
    key = sha.digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encrypt(data, password):
    iv = Random.new().read(AES.block_size)
    return iv + create_aes(password, iv).encrypt(data)

def decrypt(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return create_aes(password, iv).decrypt(cipher)


import sys
import getpass

password = getpass.getpass('password> ')
password2 = getpass.getpass('confirm> ')
if password != password2:
    print('Passwords do not match.')
    sys.exit(0)

enc = encrypt(sys.stdin.buffer.read(), password)
sys.stdout.buffer.write(enc)

print(enc)

"""
password = getpass.getpass('password> ')
dec = decrypt(sys.stdin.buffer.read(), password)
sys.stdout.buffer.write(dec)"""