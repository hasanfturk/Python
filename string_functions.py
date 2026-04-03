#metin = "Merhaba Python"

#upper and lower
#print(metin.upper())
#print(metin.lower())

#capitalize and title
#print(metin.capitalize())
#print(metin.title())

#strip lstrip rstrip
"""metin = "    Merhaba Python"
print(metin.strip())"""

#replace
"""metin = "Elma sağlıklıdır,her gün Elma yiyin."
yeni_metin = metin.replace("Elma","Muz")
print(yeni_metin)"""

#split  metin.split(",") vb. şekilde de kullanılabilir
"""metin = "Merhaba Dünya,    Python"
liste = metin.split()
print(liste)"""

#join
"""liste = ["merhaba","python","programlama"]
birlesik = " , ".join(liste)
print(birlesik)"""

#find
metin = "Selam, Python öğren ,Python kullan"
print(metin.find("Python"))
