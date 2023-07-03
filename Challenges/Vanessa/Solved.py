from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = base64.b64decode(b'VGhlX09wZXJhdG9yczIxMQ==')
iv = b'kRsKfm6P4mmp6CXS'    


with open('2.dat', 'r') as f:
    data = f.read()
bytes_string = bytes.fromhex(data)
cipher = AES.new(key, AES.MODE_CFB, iv)
plaintext = cipher.decrypt(bytes_string)
#plaintext = unpad(plaintext, AES.block_size)

for i in plaintext:
    print(i, end = " ") 