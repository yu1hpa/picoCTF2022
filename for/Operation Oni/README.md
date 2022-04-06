# Operation Oni
### Description
> Download this disk image, find the key and log into the remote machine.
> - Download disk image
> - Remote machine: ssh -i key_file -p ***** ctf-player@saturn.picoctf.net

### Solution
Then you download the file from Description, you can get `"disk.img.gz"`.
You are decompressed the file and get `disk.img`.
```
$ file disk.img
disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,223,19), startsector 2048, 204800 sectors; partition 2 : ID=0x83, start-CHS (0xc,223,20), end-CHS (0x1d,81,52), startsector 206848, 264192 sectors
```
You confirm status of partition of `disk.img` by `mmls` command.
```
$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```
Then you mount this partition of `Linux(0x83)` of number 003, you can confirm status of root directory of `disk.img`. 
`offset=105906176` is product offset of `Start` of number 003 and `sector size`.
```
$ sudo mount -o loop,offset=105906176 disk.img /mnt/
$ ls /mnt
bin   dev  home  lost+found  mnt  proc  run   srv  tmp  var
boot  etc  lib   media       opt  root  sbin  sys  usr
```
Then you look `/root/` of mounted image, you can find `.ash_history` and `.ssh/`.
```
$ sudo ls -al /mnt/root/
total 4
drwx------  3 root root 1024 Oct  6 14:30 .
drwxr-xr-x 21 root root 1024 Oct  6 14:28 ..
-rw-------  1 root root   36 Oct  6 14:31 .ash_history
drwx------  2 root root 1024 Oct  6 14:30 .ssh
```
Then you look `.ash_history`, you find that ssh secret key is created.
```
$ sudo cat root/.ash_history
ssh-keygen -t ed25519
ls .ssh/
halt
```
Then you look `.ssh/`, you find two files: secret key (`id_ed25519`) and public key (`id_ed25519.pub`).
```
$ sudo ls -al /mnt/root/.ssh/
total 4
drwx------ 2 root root 1024 Oct  6 14:30 .
drwx------ 3 root root 1024 Oct  6 14:30 ..
-rw------- 1 root root  411 Oct  6 14:30 id_ed25519
-rw-r--r-- 1 root root   96 Oct  6 14:30 id_ed25519.pub
$ sudo cat /mnt/root/.ssh/id_ed25519
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
...
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```
If you find secret key, you can access purpose server.
`id_ed25519` save to key_file and You access server that shown Description by key_file.
At this time, if key_file can edit, you cannot access the server.
So, you need to change key_file's permission for removing edit permission of owned group and other users.
```
$ sudo cat /mnt/root/.ssh/id_ed25519 > key_file
$ chmod 600 key_file
$ ls -al key_file
-rw------- 1 vagrant vagrant 411 Mar 21 02:50 key_file
```
Then you access the server and look `flag.txt`, you can find flag.
```
$ ssh -i key_file -p ***** ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1017-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_d6570e30}
```
Therefore, flag is `picoCTF{k3y_5l3u7h_d6570e30}`.

### Writer
Yajirushi