import rsa
from base64 import b64encode

with open('privkey', mode='rb') as privkey_file:
    keydata = privkey_file.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)

data = 'user@email.com'
signature = rsa.sign(data.encode('utf-8'), privkey, 'SHA-512')

print(data + '\n' + b64encode(signature).decode('ascii'))
# This prints the following:
# user@email.com
# ejp2RYhgI5p43n80BB311Ck32umDmqoezLkfOJmqIgNvHfux9Wm8bYtZJIAciet/Ef0ORo49JHr6zYwnTq6g7w==
