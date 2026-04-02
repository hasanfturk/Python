"""kareler = []
for x in range(1,11):
    kareler.append(x**2)

print(kareler)


#list comprehension
kareler = [x**2 for x in range(1,11)]
print(kareler)"""



"""
sayilar = [1,2,3,4,5,6,7,8,9,10]
ciftler = []

for x in sayilar:
    if x %2 ==0:
        ciftler.append(x)

print(ciftler)

#list comprehension
ciftlerin_karesi = [x**2 for x in sayilar if x % 2== 0]
print(ciftlerin_karesi)
"""




#kelimeleri büyük harfli yapmak
kelimeler = ["python","java","c++","html"]
buyuk_harf = [kelime.upper() for kelime in kelimeler]
print(buyuk_harf)