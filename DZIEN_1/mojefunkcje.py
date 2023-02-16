#przykład 1
n=100

def hx(k):
    return k**3-1

def policz(a,b,c,y):
    global n
    n = (a+b)*y - c + n + hx(b)
    return n

print(policz(3,7,8,1))
print(policz(5.8,12,0.045,5.88))
print(n)
