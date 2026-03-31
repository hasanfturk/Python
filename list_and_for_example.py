isimler = ["Ali", "Veli", "Ayşe"]

isimler.append("Zeynep")

isimler.sort()

print("Kayıtlı İsimler:")

for isim in isimler:
    if len(isim) > 4:
        print(isim + " (Uzun bir isim)")
    else:
        print(isim)

print("Toplam kişi sayısı:", len(isimler))