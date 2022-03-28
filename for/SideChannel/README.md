# SideChannel
### Description
> There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? Download the PIN checker program here pin_checker Once you've figured out the PIN (and gotten the checker program to accept it), connect to > the master server using nc saturn.picoctf.net 52026 and provide it the PIN to get your flag.

### Solution
Then you download the file from Description, you can get `"pin_checker"` that is `ELF 32-bit` format.
```
$ file pin_checker
pin_checker: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped
```

Then you give execute permission and execute the file, you are required 8 digit PIN.
```
$ ./pin_checker
Please enter your 8-digit PIN code:
39393939
8
Checking PIN...
Access denied.
```

According to Problem title and hint, you can find that you use time-based side-channel attack for finding pin.
time-based side-channel attack is method that you infer true input by execute time of various input.

This method have to mesure accurate execute time of program. 
Therefore, you should use `inscount0` of `intel Pin`.
This can count instruction number of times that is executed in a program.
If you want to introduce `intel Pin`, you refer to document of `intel Pin`. ([intel Pin 3.21 User Guide Introduction](https://software.intel.com/sites/landingpage/pintool/docs/98484/Pin/html/))

You investigate instruction number of times that is executed by using `inscount0`.
instruction number of times is written to inscount.out that is made in same directory.
```
$ ~/pin-3.22/pin -t ~/pin-3.22/source/tools/ManualExamples/obj-ia32/inscount0.so -- ./pin_checker
Please enter your 8-digit PIN code:
00000000
8
Checking PIN...
Access denied.
$ cat inscount.out
Count 53424457
```
This operation repeat while change 1st digit 0 to 9 and you compare instruction number of times.
| input    | count     |
| ----     | ----      |
| 00000000 | 53424457  |
| 10000000 | 60613313  |
| 20000000 | 66364397  | 
| 30000000 | 66843654  |
| 40000000 | 132505188 |
| 50000000 | 61092570  |
| 60000000 | 61571827  |
| 70000000 | 62530341  |
| 80000000 | 61092570  |
| 90000000 | 62051134  |

You look this table and find that instruction number of time of the number whose 1st digit is 4 is increase about 60000000 compared to others number.
From this, you infer that this algorithm of program becomes as follows.

- Compared digit one by one from the left.
- If compared digit match correct digit, compared digit move next digit.
- Else, this program is end.

Therefore, you should doing that you fix 1st digit to 4 and change 2nd digit 0 to 9 and investigate instruction number of times by this input.

Then you investigate instruction number of times and infer PIN of 6 digit fron the left, you can find this PIN of 6 digit from the left is `483905`.
Because `inscount0` of `intel Pin` is take long time, you may be okay brute-force attack to the program if you can find PIN of about 6 digit from the left.

Using number `483905`, you do brute-force attack of last 2 digits.
```python
from pwn import *

def brute():
    ans_l = ""

    for i in range(99):
        l = "483905" + str(i).zfill(2)
        print(l)
        target = process("./pin_checker")
        print(target.recvline())
        print(l)
        target.sendline(l)
        print(target.recvline())
        print(target.recvline())
        ans = target.recvline()
        print(ans)
        target.close()
        if ans != b"Access denied.\n":
            ans_l = l
            break
    return ans_l

l = brute()
print(l)
```

Then you execute this code, you can find correct PIN.
```
...
[+] Starting local process './pin_checker': pid 49252
b'Please enter your 8-digit PIN code:\n'
48390513
b'8\n'
b'Checking PIN...\n'
b'Access granted. You may use your PIN to log into the master server.\n'
[*] Stopped process './pin_checker' (pid 49252)
48390513
```

Therefore, you can find correct PIN is `48390513`.
If you input this number in the program, you can find this number is correct.
```
$ ./pin_checker
Please enter your 8-digit PIN code:
48390513
8
Checking PIN...
Access granted. You may use your PIN to log into the master server.
```

Then you access server that shown Description and input correct PIN, you can get flag.
```
$ nc saturn.picoctf.net 52026
Verifying that you are a human...
Please enter the master PIN code:
48390513
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_6e11b28e}
```

Therefore, flag is `picoCTF{t1m1ng_4tt4ck_6e11b28e}`