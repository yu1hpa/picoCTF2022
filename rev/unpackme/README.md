# unpackme
### Description
> Can you get the flag? Reverse engineer the binary.

### Solution
Then you download the file from Description, you can get `"unpackme-upx"` that is `ELF 64-bit` format.
```
$ file unpackme-upx
unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
```

Then you give execute permission to the file and execute it, you can find that to inputting number is required. So, you can infer that you can get flag by getting correct number.
```
$ ./unpackme-upx
What's my favorite number? 39
Sorry, that's not it!
```

From file name, hint and `strings` command, you can infer that `unpackme-upx` is compressed data by UPX(The Ultimate Packer for eXecutables).
For this reason, it is difficult to analyze the file if you keep on like that.
That's why you should analyze file that is decompressed by `upx` command.
```
$ upx -d unpackme-upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2018
UPX 3.95        Markus Oberhumer, Laszlo Molnar & John Reiser   Aug 26th 2018

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1002408 <-    379108   37.82%   linux/amd64   unpackme-upx

Unpacked 1 file.
```

You do reverse assembly of `main()` function by using `radare2` etc.
```
[0x00401c90]> s main
[0x00401e73]> pdf
            ; DATA XREF from entry0 @ 0x401cb1
┌ 246: int main (int argc, char **argv);
│           ; var char **var_50h @ rbp-0x50
│           ; var int64_t var_44h @ rbp-0x44
│           ; var int64_t var_3ch @ rbp-0x3c
│           ; var int64_t var_38h @ rbp-0x38
│           ; var int64_t var_30h @ rbp-0x30
│           ; var int64_t var_28h @ rbp-0x28
│           ; var int64_t var_20h @ rbp-0x20
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t var_14h @ rbp-0x14
│           ; var int64_t var_8h @ rbp-0x8
│           ; arg int argc @ rdi
│           ; arg char **argv @ rsi
│           0x00401e73      f30f1efa       endbr64
│           0x00401e77      55             push rbp
 ...
│           0x00401ec6      66c745ec4e00   mov word [var_14h], 0x4e    ; 'N' ; 78
│           0x00401ecc      488d3d31110b.  lea rdi, str.Whats_my_favorite_number__ ; 0x4b3004 ; "What's my favorite number? " ; int64_t arg1
│           0x00401ed3      b800000000     mov eax, 0
│           0x00401ed8      e813ef0000     call sym.__printf
│           0x00401edd      488d45c4       lea rax, [var_3ch]
│           0x00401ee1      4889c6         mov rsi, rax
│           0x00401ee4      488d3d35110b.  lea rdi, [0x004b3020]       ; "%d" ; const char *format
│           0x00401eeb      b800000000     mov eax, 0
│           0x00401ef0      e88bf00000     call sym.__isoc99_scanf     ; int scanf(const char *format)
│           0x00401ef5      8b45c4         mov eax, dword [var_3ch]
│           0x00401ef8      3dcb830b00     cmp eax, 0xb83cb
│       ┌─< 0x00401efd      7543           jne 0x401f42
│       │   0x00401eff      488d45d0       lea rax, [var_30h]
 ...
│       └─> 0x00401f67      c9             leave
└           0x00401f68      c3             ret
```

According the disassembler, you can be read that input number is stored to `[var_3ch] = $rbp-0x3c` and in address `0x00401ef8`, the number is compared with `0xb83cb`.
Therefore, you can find that correct number is `0xb83cb = 754635(10)`.

Then you execute the file and input `754635`, you can get flag.
```
$ ./unpackme-upx
What's my favorite number? 754635
picoCTF{up><_m3_f7w_2fce46e8}
```

Therefore, flag is `picoCTF{up><_m3_f7w_2fce46e8}`.
