
# Sequences

To rephrase this problem, we can say that


<img src="https://latex.codecogs.com/svg.image?(a_0,a_1,a_2,a_3)=(1,2,3,4)\\a_n&space;=&space;55692a_{n-4}-9549a_{n-3}&plus;301a_{n-2}&plus;21a_{n-1}\;&space;(n\geq&space;4)\\a_{20000000}&space;\pmod{10^{10000}}&space;=&space;?"/>

If one tries to find the numbers up to N=20000000 in sequence, the computational complexity is O(N), and since 10000 digits must be kept, it is very time-consuming.

In fact, This Recurrence formula can be expressed as follows.

<img src="https://latex.codecogs.com/svg.image?\begin{pmatrix}21&301&space;&-9549&55692\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}&space;^{n-3}\begin{pmatrix}a_3\\a_2\\a_1\\a_0\end{pmatrix}=\begin{pmatrix}a_n\\a_{n-1}\\a_{n-2}\\a_{n-3}\\\end{pmatrix}"/>


There is a method to find a matrix to the Nth power with a computational complexity of O(log N).
This is an extension of fast modular exponentiation, which is used to compute powers in integers.

For more information, I think [khan academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation) is good to understand
    
<details>
<summary>日本語 (in Japanese)</summary>

問題を言い換えると，

<img src="https://latex.codecogs.com/svg.image?(a_0,a_1,a_2,a_3)=(1,2,3,4)\\a_n&space;=&space;55692a_{n-4}-9549a_{n-3}&plus;301a_{n-2}&plus;21a_{n-1}\;&space;(n\geq&space;4)\\a_{20000000}&space;\pmod{10^{10000}}&space;=&space;?"/>


という問題になります．
N=20000000まで順番に求めようとすると計算量がO(N)になり，桁数を10000桁保持しなければならないこともあり，非常に時間がかかります．



<img src="https://latex.codecogs.com/svg.image?\begin{pmatrix}21&301&space;&-9549&55692\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}&space;^{n-3}\begin{pmatrix}a_3\\a_2\\a_1\\a_0\end{pmatrix}=\begin{pmatrix}a_n\\a_{n-1}\\a_{n-2}\\a_{n-3}\\\end{pmatrix}"/>

行列をN乗を計算量O(log N)で求める方法があります．
これは，整数で累乗を計算する際に使われるFast modular exponentiationの拡張です．
![khan academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation)がわかりやすいです．

</details>


### solver
```python
import math
import hashlib
import sys
from tqdm import tqdm
import functools

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfe08b5f3b248ef7c32b")

def mat_mul(a, b) :
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= 10**10000
    return c


def mat_pow(x, n):
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1

    return y


d0 = 0
ret = [[4], [3], [2],[1]]
mat = [[21,301,-9549,55692], [1, 0, 0, 0], [0, 1, 0, 0],[0,0,1,0]]
#ret = mat_mul(mat_pow(mat, ITERS), ret)
#ret = [[1],[1]]
#mat = [[1,1], [1,0]]
ret = mat_mul(mat_pow(mat, ITRES), ret)
print(ret)


# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = A
    decrypt_flag(sol)
```




### Writer
[shiba28](https://twitter.com/Shibak3333n)
