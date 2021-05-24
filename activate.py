import rsa
from base64 import b64encode

with open('privkey', mode='rb') as pubkey_file:
    keydata = pubkey_file.read()
pubkey = rsa.PrivateKey.load_pkcs1(keydata)

try:
    rsa.verify(data.encode('utf-8'), signature, pubkey)
except rsa.VerificationError:
    # invalid license key - refuse to start
else:
    # start application
