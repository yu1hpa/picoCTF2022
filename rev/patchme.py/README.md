# patchme.py
### Description
> Can you get the flag? Run this Python program in the same directory as this encrypted flag.

### Solution
Then you download the file from Description, you can get `"patchme.flag.py"` and `"flag.txt.enc"`. You put `patchme.flag.py` and `flag.txt.enc` on same directory and execute `patchme.flag.py` by using `python3`. Then you execute the python file, you find that to inputting password is required. So, you can infer that you can get flag by getting correct password.
```
$ ls
flag.txt.enc  patchme.flag.py
$ python3 patchme.flag.py
Please enter correct password for flag: aaaa
That password is incorrect
```

Then you look source code of `patchme.flag.py`, you can find that inputted password is compared with correct password in if statement of `level_1_pw_check()`.
```
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")
```

In `python3`, because connection of strings can do by `+` operator, you just connect strings that is connected with `+` operator. You can find that correct password is `ak98-=90adfjhgj321sleuth9000` by above operation.
Then you execute `patchme.flag.py` and input correct password, you can get flag.
```
$ python3 patchme.flag.py
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_68aa6913}
```

Therefore, flag is `picoCTF{p47ch1ng_l1f3_h4ck_68aa6913}`.