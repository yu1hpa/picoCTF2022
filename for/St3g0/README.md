# St3g0
### Description
> Download this image and find the flag.
> - Download image

### Solution
Then you download the file from Description, you can get `"pico.flag.png"` that is `.png` format.
```
$ file pico.flag.png
pico.flag.png: PNG image data, 585 x 172, 8-bit/color RGBA, non-interlaced
```
Then you open the file by `eog` etc, you can find that image of the file is logo of "picoCTF".
But, flag isn't written in the state of visible in this image.
![St3g0](St3g0.png)

Here, you can infer that `"St3g0"` in problem title is similar `"$t3g0"` which is delimited string used LSB Image Steganography.
LSB Image Steganography is method that string which you want to hide convert binary and embed in LSB, which is RGB Least significant bit of `.png` format.
For the reason, you can find flag by doing that LSB of each RGB take out and convert to character every 8bit.

This operation describe by `python3` etc. (this write-up is using `python3`.)
```python
# decode.py
import numpy as np
from PIL import Image

# RGB[0~256] -> 8bit
def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))
    # print(array) # [[ 0 1 1 0] [ 1 0 0 0 ] ...]
    total_pixels = array.size//4 # row size = number of LSB
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(3):
            hidden_bits += bin(array[p][q])[-1] # take out LSB

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)] # take out every 8bit and save in list

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0": # end condition
            break
        else:
            message += chr(int(hidden_bits[i], 2)) # convert character from integer

    print(message)

Decode("./pico.flag.png")
```

Then you execute this code, you can get flag.
```
$ python3 decode.py
picoCTF{7h3r3_15_n0_5p00n_f2f7a0e5}$t3g0
```

Therefore, flag is `picoCTF{7h3r3_15_n0_5p00n_f2f7a0e5}`.

### Reference
[LSB Image Steganography Using Python](https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2)
### Writer
Yajirushi