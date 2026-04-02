#öğrencilerin isimleri ve numaraları sıra ile verilmiştir.en büyük ve en küçük numaralı öğrenciyi bulup ekrana yazdırınız.
"""
isimler = ["Ali","Ece","Kaan","Mete","Batu","Veli","Ayşe"]
numaralar = [145 ,178, 164, 175, 185, 180, 134]

max_numara = 0
max_ogrenci = ""

for i in range(len(numaralar)):   # 0 1 2 3 4 5 6
    if numaralar[i] > max_numara:
        max_numara = numaralar[i]
        max_ogrenci = isimler[i]

print("En büyük okul numarası: ",max_numara)
print("En büyük numaraya sahip öğrenci: ",max_ogrenci)



min_numara = 10**5
min_ogrenci = ""

for k in range(len(numaralar)):
    if numaralar[k]<min_numara:
        min_numara = numaralar[k]
        min_ogrenci = isimler[k]

print("En küçük okul numarası: ",min_numara)
print("En küçük okul numarasına sahip öğrenci : ",min_ogrenci)
"""


isimler = ["Ali","Ece","Kaan","Mete","Batu","Veli","Ayşe"]
numaralar = [145 ,178, 164, 175, 185, 180, 134]

max_numara = max(numaralar)
max_index = numaralar.index(max_numara)
max_ogrenci = isimler [max_index]
print("en yüksek numara: ",max_numara,"ogrenci: ",max_ogrenci)


min_numara = min(numaralar)
min_index = numaralar.index(min_numara)
min_ogrenci = isimler [min_index]
print("en küçük numara: ",min_numara,"ogrenci: ",min_ogrenci)











