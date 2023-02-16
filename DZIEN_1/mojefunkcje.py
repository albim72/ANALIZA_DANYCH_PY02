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

#przykład 4 - funckja lambda
print((lambda d:d+66)(4))
print((lambda d:d+66)(88.09))
print((lambda d,u:d+66*u)(-98,8))

b = lambda a,b,c=3:(a+b)/c
print(b(4,7,1))
print(b(9,3))


def multi(n):
    return lambda a:a*n

print(multi(9)(7))

num = [67,2,4,-5,18,90,111,0,-45,10,9,2,16,9,88]

nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

cube = list(map(lambda x:x**3,num))
print(cube)

def dodaj(x):
    return x+9

dziewiec = list(map(dodaj,num))
print(dziewiec)


#zbuduj nową listę która będzie się składała z wartości całkowitych z przedziału [1,100000] każda podniesiona do kwadratu
#list comprehension

kwadraty = [i**2 for i in range(1,100001)]
print(kwadraty)

def generuj_liste(pot,min,max):
    return [i**pot for i in range(min,max+1)]

pt = generuj_liste(5,109,88900)
print(pt)


#przykład 6
def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"Uczestnik konkursu -> {imie}, punkty: {punkty}"

def osoba(funkcje,*args):
    return funkcje(*args)

print(osoba(witaj,"Olga"))
print(osoba(konkurs,"Leon",33))


