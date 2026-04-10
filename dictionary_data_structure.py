#dict --> dictionary

ogrenciler_dict = {100:"Ali Kaya",101:"Zeynep Taş"}

#print(type(ogrenciler_dict))
#print(ogrenciler_dict)
#print(ogrenciler_dict[100])

deger = ogrenciler_dict.get(102)
if deger is None:
    print("Öğrenci okulda yok.")
else:
    print("Öğrenci mevcut.")

liste1 =list(ogrenciler_dict.keys())
print(liste1)

liste2 =list(ogrenciler_dict.values())
print(liste2)

#print(type(deger))

"""
ogrenci_numaralari = [100,101]
ogrenci_isimleri = ["Ali Kaya","Zeynep Taş"]
"""
