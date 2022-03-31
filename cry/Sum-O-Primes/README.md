# Sum-O-Primes

### Solution
The problem is simple: from the values of <img src="https://latex.codecogs.com/svg.image?n=pq"> and <img src="https://latex.codecogs.com/svg.image?x=p&plus;q" /> The problem is to solve RSA.

When recovering the RSA cipher, the value needed is the key <img src="https://latex.codecogs.com/svg.image?d"/> for the recovery, and
<img src="https://latex.codecogs.com/svg.image?d=e^{-1}&space;\pmod{(p-1)(q-1)}"/>


 This can be obtained from <img src="https://latex.codecogs.com/svg.image?n"/> and <img src="https://latex.codecogs.com/svg.image?x"/>.


<img src="https://latex.codecogs.com/svg.image?(p-1)(q-1)&space;=&space;pq&space;-&space;p&space;-&space;q&space;&plus;&space;1&space;=&space;pq&space;-&space;(p&plus;q)&space;&plus;&space;1&space;=&space;n&space;-&space;x&space;&plus;&space;1" />


<details>
<summary>日本語 (in Japanese)</summary>

この問題は，シンプルで，<img src="https://latex.codecogs.com/svg.image?n=pq">と<img src="https://latex.codecogs.com/svg.image?x=p&plus;q" />の値からRSAを解く問題です．

RSA暗号を復元するときに必要な値は復元のための鍵<img src="https://latex.codecogs.com/svg.image?d"/>であり，
<img src="https://latex.codecogs.com/svg.image?d=e^{-1}&space;\pmod{(p-1)(q-1)}"/>
で求めることができます．
つまり，<img src="https://latex.codecogs.com/svg.image?(p-1)(q-1)"/>が求まれば良く，これは<img src="https://latex.codecogs.com/svg.image?n"/>と<img src="https://latex.codecogs.com/svg.image?x"/>から求めることができます．

<img src="https://latex.codecogs.com/svg.image?(p-1)(q-1)&space;=&space;pq&space;-&space;p&space;-&space;q&space;&plus;&space;1&space;=&space;pq&space;-&space;(p&plus;q)&space;&plus;&space;1&space;=&space;n&space;-&space;x&space;&plus;&space;1" />


</details>

### solver
```python
from Crypto.Util.number import *

x = (omitted)
n = 
c = 
e = 65537

"""
n = pq
p * q
p + q
pq - (p+q) +1
(p-1)(q-1)
"""

phi = n-x+1
d=pow(e,-1,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
```


