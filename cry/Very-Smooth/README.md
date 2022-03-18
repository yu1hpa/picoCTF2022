# basic-file-exploit

### Description
> Forget safe primes... Here, we like to live life dangerously... >:)

### Solution
First, we try [factordb](http://factordb.com/), but this dosen't work.
so now look at how to make $p$ and $q$.
there is DEGUB in ``gen.py``, let's run this.

<details><summary>Result</summary><div>
```python
p_factors = [
    2,
    9277,
    16057,
    33223,
    33961,
......
    61837,
    61961,
    62743,
    63577,
    65407,
]

q_factors = [
    2,
    33161,
    48751,
    67391,
    67399,
......
    126227,
    127163,
    127607,
    128047,
]
```
</div></details>



プログラムも合わせて見ると，$p$と$q$は小さな素数の積に$1$を足して作られていることがわかります(もし$1$を足しても素数にならなければ作り直している)．また，$p$と$q$で使われている素数の範囲も異なっています．この状況に対して，$p-1$法という素因数分解の手法が使えます．

$p-1$法は，互いに素な$a,p$で，フェルマーの小定理$a^{p-1} = 1 \pmod p$が成り立つことを使います．

$p-1$の倍数である適当な数$ M $を持ってきて，[tex: a^M  を計算すれば， $ a^M = 1 \pmod p $ が成り立ち， $ a^M-1 $ が $ p $ の倍数となります．

つまり，適当な$ M $を設定することで，$ a^M-1 $と$ n $の最大公約数が$ p $となります．

今回は，$p-1$が$10^5$未満の素数の積によって生成されていることから，$M$を$10^5$以下の素数の積として，$a$は$2$を選びます．
$M$の値は小さな素数の積であれば何でもいいわけではなく，もし$M$を$1.5\times 10^5$程度までの素数の積にしてしまうと，$M$が$(p-1)(q-1)$の倍数になってしまい，
$ a^{(p-1)(q-1)} =a^M = 1 \pmod n$が成り立つため，$n$と$a^M-1$の最大公約数が$n$になってしまいます．

この問題を解くにあたって下記の記事を参考にさせていただきました．
[https://wacchoz.hatenablog.com/entry/2019/01/20/120000:embed:cite]

<details><summary>ソルバ</summary><div>
```
from Crypto.Util.number import *


n = #省略
c = #
e = 0x10001

a = 2
b = 1
for i in range(2,100000):
    if isPrime(i):
        b*=i
ab =pow(a,b,n)

p = GCD(ab-1,n)
q=n//p

phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
```
</div></details>


### Writer
[yu1hpa](https://twitter.com/Shibak3333n)