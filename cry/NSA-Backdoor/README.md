# NSA-Backdoor


```python
from Crypto.Util.number import *

n = 0x71c27455f38b75f08868b5965d7afba3d81bff38f3b63271ad9250b9d7dc8c909d3555593c2eff9c27a3c259f8e95da41d55544a362494476141c8ccb93fc7d9019d965a20e16d55daf57b5663ede8d5ad97b7be239ecacb2636621ef997854f18f6da1394101dfb8229a2253dbc3ffc995cc6197bd85455f6178c14dbb9a611b3b42530fcdc5c36c5f63fd3796efdfc440a76cf966ff8c56e7e55872a57aa3a335c2b10a82421bcd1cd0d238496f2830d6524f6ba8e9890e30c4e6ad11df8948f4b428d8089a5d9455baca34cee61cb238042bcf8293aab13595aeb90fedabf23b1d0e82c6882824aa0f78c2208de641d9592a170ed839728f6c7e6b6bdf831
y = 0x2560971fdf742d398ae3e677082ab950e99edde5577abcc4d704d65577ec287169d209f2033c82e7574f7e6c27540bb07416cd12b5fca1bb5c7ae23e80bb00b81a5c49116fa3cca6ab72f4a56b2bf0d51c58eedb918faa1e88d6fddb7dd358c1cdaa6e61964284014919662f75adaad5065a3633067b2297cd4657d39c8e2cdb02fd80ba33447abb8bfcd4dd68166f487094108afe5b4378f5f6eb9209f503b718dec9c841089551db648f5b5a84357b2319eb1b27935c3bc47c645f732d36cfffcb0e7f1c8ec5859413e6d62f7ed9af27f4712ca91bbdb9526ea19414c82090a52a78e6bbc2a756b5756017ee08326cd7b1d5dd9fff6afb12bcb93fb541a542

print(f'n = {n}')
print(f'c = {y}')

"""

if __name__ == '__main__':

    N = n

    L=100000
    a=2
    aM = 2
    for p in range(2,L+1):
        if not isPrime(p):
            continue
        Mp = p
        while Mp*p <= L:
            Mp*=p
        #a^m mod Nの計算（素数pごとに計算）
        aM = pow(aM, Mp, N)

    g = GCD(aM-1, N)
    print(g)
"""
p=133120514134071565184901374403906104857402594315193452979400334844456988039351029748429497538981454221984106135005043996378098395846705709422658663585864970394230279241392567216599860405945469882804839379543093459226432299183847151658790842646530907008354991523758458009950957111989465047584759069188272154703
q=107878320716069936845347261730222923402619282584236808136469656719645067255143372538361375857163594280233925663413568686520703251291382637679919197208920902793419007945364505474185442005931731898039583502138819092649272834779913753377381462765827012568092442233669634217190652686190269458879367972776287369087
assert p*q==n
phi=[2, 2, 10369, 11437, 11969, 12491, 33343, 34369, 34687, 34939, 35969, 36467, 36709, 36919, 36973, 36997, 37361, 37379, 37561, 38867, 40897, 41203, 41593, 41801, 42221, 43189, 43481, 43951, 44029, 44953, 45161, 45751, 46649, 46703, 47017, 47221, 49409, 49499, 49783, 50321, 50539, 52081, 53077, 53299, 54367, 54601, 54829, 55147, 55399, 55457, 55661, 56039, 56237, 56267, 56299, 57089, 57373, 57637, 57731, 58897, 59753, 60223, 60733, 61673, 61781, 62459, 62969, 63781, 63901, 64399, 65551, 67651, 68207, 68947, 72287, 74653, 74857, 75011, 77081, 77153, 77239, 78467, 78691, 78877, 81343, 83701, 85009, 88037, 88117, 88397, 89269, 89363, 89477, 90403, 90901, 91009, 94057, 95701, 98387, 100853, 104161, 105097, 106657, 107021, 109121, 109807, 110681, 111599, 112901, 113797, 114883, 115163, 115727, 116009, 117037, 117413, 118799, 120413, 123229, 123973, 124067, 124427, 
125863, 125887, 126631, 127481, 128311, 129671, 129793, 130589]
m=1
for i in phi:
    m*=i
assert m==(p-1)*(q-1)

g=3

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0

# V = [(X_i, Y_i), ...]: X_i (mod Y_i)
def remainder(V,W):
    x = 0; d = 1
    for i in range(len(V)):
        X=V[i]
        Y=W[i]
        g, a, b = extgcd(d, Y)
        x, d = (Y*b*x + d*a*X) // g, d*(Y // g)
        x %= d
    return x, d



# Baby-step giant-step
def baby_step_giant_step(g, y, p, q):
    m = int(q**0.5 + 1)
    
    # Baby-step
    baby = {}
    b = 1
    for j in range(m):
        baby[b] = j
        b = (b * g) % p

    # Giant-step
    gm = pow(inverse(g, p), m, p)
    giant = y
    for i in range(m):
        if giant in baby:
            x = i*m + baby[giant]
            print("Found:", x)
            return x
        else:
            giant = (giant * gm) % p
    print ("not found")
    return -1


# Pohlig-Hellman algorithm
def pohlig_hellman(p1,p2, g, y, Q):
    print ("[+] Q:", Q)
    X = []
    for q in Q:
        x = baby_step_giant_step(pow(g,((p1-1)*(p2-1))//q,p1*p2), pow(y,((p1-1)*(p2-1))//q,p1*p2), p1*p2, q)
        X.append(x)
    print ("[+] X:", X)
    x ,d= remainder(X,Q)
    return x,d


x,d = pohlig_hellman(p,q, g, y, phi)
print(long_to_bytes(x))
print(long_to_bytes(d))
```


### Writer
[shiba28](https://twitter.com/Shibak3333n)

