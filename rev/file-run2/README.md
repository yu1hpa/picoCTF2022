# file-run2
### Description
> Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program here.

### Solution
Then you download the file from Description, you can get `"run"`.
Then you investigate file format of the file, it is `ELF 64-bit`.
So, you can execute the file in Linux.
```
run: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=16b456a5446214803f67bcca54cf7e32f9ac5bd5, for GNU/Linux 3.2.0, not stripped
```

Because the file isn't given execute permission, you give execute permission to the file by using `chmod` command.
```
$ ls -al run
-rw-rw-r-- 1 vagrant vagrant 16816 Mar 15 06:55 run
$ chmod +x run
$ ls -al run
-rwxrwxr-x 1 vagrant vagrant 16816 Mar 15 06:55 run
```

According to Description, you have to input `"Hello!"` to command line arguments when you execute the file.
Then you input `"Hello!"` to command line arguments and execute the file, you can get flag.
```
$ ./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_0097836e}
```

Therefore, flag is `picoCTF{F1r57_4rgum3n7_0097836e}`.