# Bbbbloat
### Description
> Can you get the flag? Reverse engineer this binary.

### Solution
Then you download the file from Description, you can get `"bbbbloat"` that is `ELF 64-bit` format.
```
$ file bbbbloat
bbbbloat: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7a84389cb2bf31311778992121916d06a92bf701, for GNU/Linux 3.2.0, stripped
```

Then you give execute permission to the file and execute the file, you find that to input number is required. So, you can infer that you can get flag by getting correct number.
```
$ ./bbbbloat
What's my favorite number? 39
Sorry, that's not it!
```

You analyze the file using `radare2` etc.
```
$ r2 bbbbloat
[0x00001160]> aaa
[0x00001160]> afl
0x00001160    1 46           entry0
0x000010d0    1 11           sym.imp.free
0x000010e0    1 11           sym.imp.putchar
0x000010f0    1 11           sym.imp.puts
0x00001100    1 11           sym.imp.strlen
0x00001110    1 11           sym.imp.__stack_chk_fail
0x00001120    1 11           sym.imp.printf
0x00001130    1 11           sym.imp.fputs
0x00001140    1 11           sym.imp.__isoc99_scanf
0x00001150    1 11           sym.imp.strdup
0x00001307    6 675          main
0x00001240    5 137  -> 60   entry.init0
0x00001200    5 57   -> 54   entry.fini0
0x000010c0    1 11           fcn.000010c0
0x00001190    4 41   -> 34   fcn.00001190
0x00001249   10 190          fcn.00001249
0x00001000    3 27           fcn.00001000
```

According to `afl`, because you can find address of main function, you can do reverse assembly of main function.
```
[0x00001160]> s main
[0x00001307]> pdf
            ; DATA XREF from entry0 @ 0x1181
┌ 675: int main (int argc, char **argv);
│           ; var char **var_50h @ rbp-0x50
│           ; var int64_t var_44h @ rbp-0x44
│           ; var int64_t var_40h @ rbp-0x40
│           ; var int64_t var_3ch @ rbp-0x3c
│           ; var char *ptr @ rbp-0x38
│           ; var int64_t var_30h @ rbp-0x30
│           ; var int64_t var_28h @ rbp-0x28
│           ; var int64_t var_20h @ rbp-0x20
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t canary @ rbp-0x8
│           ; arg int argc @ rdi
│           ; arg char **argv @ rsi
│           0x00001307      f30f1efa       endbr64
│           0x0000130b      55             push rbp
 ...
│           0x000013c6      89c8           mov eax, ecx
│           0x000013c8      8945c4         mov dword [var_3ch], eax
│           0x000013cb      488d3d320c00.  lea rdi, str.Whats_my_favorite_number__ ; 0x2004 ; "What's my favorite number? " ; const char *format
│           0x000013d2      b800000000     mov eax, 0
│           0x000013d7      e844fdffff     call sym.imp.printf         ; int printf(const char *format)
│           0x000013dc      c745c4783000.  mov dword [var_3ch], 0x3078 ; 'x0'
│           0x000013e3      8145c49ec213.  add dword [var_3ch], 0x13c29e ; [0x13c29e:4]=0
│           0x000013ea      816dc4a83000.  sub dword [var_3ch], 0x30a8 ; [0x30a8:4]=-1
│           0x000013f1      d165c4         shl dword [var_3ch], 1
│           0x000013f4      8b45c4         mov eax, dword [var_3ch]
 ...
│           0x00001446      488d45c0       lea rax, [var_40h]
│           0x0000144a      4889c6         mov rsi, rax
│           0x0000144d      488d3dcc0b00.  lea rdi, [0x00002020]       ; "%d" ; const char *format
│           0x00001454      b800000000     mov eax, 0
│           0x00001459      e8e2fcffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x0000145e      c745c4783000.  mov dword [var_3ch], 0x3078 ; 'x0'
 ...
│           0x000014c1      29c7           sub edi, eax
│           0x000014c3      89f8           mov eax, edi
│           0x000014c5      8945c4         mov dword [var_3ch], eax
│           0x000014c8      8b45c0         mov eax, dword [var_40h]
│           0x000014cb      3d87610800     cmp eax, 0x86187
│       ┌─< 0x000014d0      0f85ad000000   jne 0x1583
│       │   0x000014d6      c745c4783000.  mov dword [var_3ch], 0x3078 ; 'x0'
 ...
│       ┌─< 0x000015a1      7405           je 0x15a8
│       │   0x000015a3      e868fbffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from main @ 0x15a1
│       └─> 0x000015a8      c9             leave
└           0x000015a9      c3             ret
```

Then you do reverse assembly of main function, you can be read that input number is stored to `[var_40h] = $rbp-0x40` and in address `0x000014cb`, the number is compared with `0x86187`.
Therefore, you can find that correct number is `0x86187 = 549255(10)`.

Then you execute the file and input `549255`, you can get flag.
```
$ ./bbbbloat
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_d059b523}
```

Therefore, flag is `picoCTF{cu7_7h3_bl047_d059b523}`.