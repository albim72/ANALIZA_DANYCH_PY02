print("pierwsza linia na dobry początek")

#komentarz podstawowy
"""
komentarz wieloliniowy dokumentacyjny
"""
'''
komentarz wieloliniowy
'''

a = 77
print(a)
print(type(a))

b = "to jest tekst"
print(b)
print(type(b))

c = b
d = b

b = 6.88
print(b)
print(type(b))

print(c)
print(type(c))

d = 45544

print(c)
print(type(c))


g:float = 9.99

print(g)
print(type(g))

g = True
print(g)
print(type(g))

#kolekcje -> lista
imiona = ["Jan","Leon","Olga","Nadia","Tomasz","Jan","Ola","Magda","Jan"]
print(imiona)

print(imiona[0])
print(imiona[1])
print(imiona[-1])
print(imiona[-2])
print(imiona[2:5])
print(imiona[4:])
print(imiona[:5])
print(imiona.count("Jan"))
print(imiona.index("Leon"))
imiona.append("Roman")
print(imiona)
imiona.insert(3,"Jarosław")
print(imiona)

imiona.remove("Jan")
print(imiona)

del imiona[5]
print(imiona)
print(imiona[0])
print(imiona[0][1])

s = "lajkonik"
print(s[1])
print(s[:3])

print(s[::-1])
print(s[2:6:2])

parzystepoz = imiona[::2]
print(parzystepoz)

nparz = imiona[1::2]
print(nparz)

print(imiona)
print(sorted(imiona))

print(imiona)

imiona.sort(reverse=True)
print(imiona)




