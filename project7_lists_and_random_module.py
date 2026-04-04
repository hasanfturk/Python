import random

sicakliklar=[]
for i in range(7):
    sayi =random.randint(1,35)
    sicakliklar.append(sayi)

print("Haftalık Sıcaklık Değerleri:",sicakliklar)

toplam=sum(sicakliklar)
ortalama=toplam/len(sicakliklar)

print(f"Haftalık Ortalama: {ortalama:.2f}")