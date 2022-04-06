# File types
### Description
> This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from here.

### Solution
Then you download the file from Description, you can get `"Flag.pdf"` that extension is `.pdf` format.
Then you investigate the file's file format by `file` command, you can find that this file is not `.pdf` format, but `shell archive text` format.
```
$ file Flag.pdf
Flag.pdf: shell archive text
```
Therefore, the fils can execute on `shell` by giving execute permission.
Then you are executed `Flag.pdf`, you can get `flag` file newly.
```
$ chmod +x Flag.pdf
$ ./Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
$ ls
flag  Flag.pdf
```
Then you investigate the file's file format by `file` command, you can find the this file is `current ar archive` format. 
Because `ar archive` is file format that put together multiple file to one, you can get file that be archived by decompressing.
Then you are decompressed the file that giving extension of `ar archive` format, you can get `flag` file again.
```
$ ar -x flag.ar
$ ls
flag  flag.ar  Flag.pdf
$ file flag
flag: cpio archive
```
Because this `flag` file's file format is `cpio archive`, you are decompressed the file giving the extension.
Therefore, you can get `flag` file again. this `flag` file's file format is `bzip2 compressed data`.
```
$ cpio -idv < flag.cpio
flag
2 blocks
$ ls
flag  flag.ar  flag.cpio  Flag.pdf
$ file flag
flag: bzip2 compressed data, block size = 900k
```
Here, you can infer `flag` file that is outputed from `Flag.pdf` is file that compressed many times by various file format.
Then you repeat operation like before, you can get `flag` file that file format is `ASCII text` format.
```
ar(.ar) -> cpio(.cpio) -> bzip2(.bz2) -> gzip(.gz) -> lzip(.lz) -> LZ4(.lz4) -> LZMA(.lzma) -> lzop(.lzo) -> lzip(.lz) -> XZ(.xz) -> ASCII text
```
Then you look `flag` file, it looks like this.
```
$ cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37353137353362307d0a
```
You infer that the string in the file is converted to hex by ASCII code.
```python
l = "7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f6630725f3062326375723137795f37353137353362307d0a"

flag = ""
for i in range(len(l)//2):
    tmp_l = int(l[i*2:i*2+2], 16)
    flag += chr(tmp_l)

print(flag)
```
So, then you convert the string by ASCII code, you can get converted string `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_751753b0}`.
Therefore, flag is `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_751753b0}`.

### Writer
Yajirushi