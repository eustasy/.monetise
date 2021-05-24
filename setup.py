import rsa

print('WARNING: The generation of static keys and parameters may take several minutes, and will consume a considerable amount of processing power. If not favourable on a production machine, new keys can be generated elsewhere and copied over a secure connection.')

(pubkey, privkey) = rsa.newkeys(2048)

privkey_file = open('privkey', 'w')
privkey_file.write(privkey.save_pkcs1().decode('utf-8'))
privkey_file.close()

pubkey_file = open('pubkey', 'w')
pubkey_file.write(pubkey.save_pkcs1().decode('utf-8'))
pubkey_file.close()

input('Complete. Press any key to close...') 
