import math

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

#przykład 2
def liczymy(a,b=1,c=6):
    return math.sqrt(a*b*c)

print(liczymy(2,5,4))
print(liczymy(3,3,3))
print(liczymy(6,7.7))
print(liczymy(6,7.7,3))
print(liczymy(8))
print(liczymy(2.2,c=16))

#przykład 3
def rank(*lang,nrrank,**inne):
    print(f"ranking języków programowania nr {nrrank} -> miejsce pierwsze: {lang[0]}, drugie: {lang[1]}, trzecie {lang[2]}")

rank("Python","Java","C++",nrrank=23)
rank("Python","Java","JavaScript","C++","Go",nrrank=27,ver="5.5")

