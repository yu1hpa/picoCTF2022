# unpackme.py
### Description
> Can you get the flag? Reverse engineer this Python program.

### Solution
Then you download the file from Description, you can get `"unpackme.flag.py"`.
Then you extract `python3`, you can find that to inputting password is required.
So, you can infer that you can get flag by getting correct password.
```
$ python3 unpackme.flag.py
What's the password? aaaa
That password is incorrect.
```

Then you look source code of `unpackme.flag.py`, it is written process that is decoded `payload`.
```python
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABiMD1GTI02ggXPJoc7SNUxSfcOTReBamq4D73v-JZC7Q3F78g3CThNcFp7xSBC31lzGmO2hKSKA1EZuSJoX8sJI1p_DjGY37P7OTv8LdbW6sWC74cdCb30I56XJIwOaavPmvJlDayDDwY_F-k6wbO9WCkaN76xjmIdV27IcE88hJlGGlwX_uyFPFQtLyHeoo_SVXnEmZ7wg_sncboA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```

You change `exec(plain.decode())` to `print(plain.decode())` of above program and execute this changed program. (I save changed source code as `print_unpackme.flag.py`.)
```
$ python3 print_unpackme.flag.py

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_45a1a353}')
else:
  print('That password is incorrect.')
```

According to above source code, the program compare inputted password and correct password `"battery horse"` and print flag if inputted password is matched with correct password.

Therefore, flag is `picoCTF{175_chr157m45_45a1a353}`.

### Writer
Yajirushi