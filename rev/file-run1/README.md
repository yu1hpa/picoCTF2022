# file-run1
### Description
> A program has been provided to you, what happens if you try to run it on the command line? Download the program here.

### Solution
Then you download the file from Description, you can get `"run"`.
Then you investigate file format of the file, it is `ELF 64-bit`.
So, you can execute the file in Linux.
```
run: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=bf17de3a8e7529f0189e9ca5203fe1c26ffe47eb, for GNU/Linux 3.2.0, not stripped
```

Because the file isn't given execute permission, you give execute permission to the file by using `chmod` command.
```
$ ls -al run
-rw-rw-r-- 1 vagrant vagrant 16736 Mar 15 06:49 run
$ chmod +x run
$ ls -al run
-rwxrwxr-x 1 vagrant vagrant 16736 Mar 15 06:49 run
```

You execute the file, you can get flag.
```
$ ./run
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_2a4dec6a}
```

Therefore, flag is `picoCTF{U51N6_Y0Ur_F1r57_F113_2a4dec6a}`.