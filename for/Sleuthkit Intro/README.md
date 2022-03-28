# Sleuthkit Intro
### Description
> Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
> - Download disk image
> - Access checker program: nc saturn.picoctf.net 52279

### Solution
Then you download the file from Description, you can get `"disk.img.gz"`.
You are decompressed the file and get `disk.img` that is `.img` format.
```
$ file disk.img
disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,190,50), startsector 2048, 202752 sectors
```
According to Description, you can find flag by investigating size of Linux partition and inputing this size in checker.
`mmls` command is one of "The Sleuth kit" that is written problem title.
If you cannot use `mmls` command, you introduce "The Sleuth kit" in local environment.

You investigate size of Linux partition by using `mmls` command.
```
$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```

From the above, then you can find that size of Linux partition is `202752`, you access checker and input this size. 
Then, you can get flag.
```
$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```

Therefore, flag is `picoCTF{mm15_f7w!}`.
