kitap1 =("Simyacı",184)
kitap2 =("Şeker Portakalı",180)

kitaplar = [("Simyacı",184),("Şeker Portakalı",180)]

print(type(kitaplar))

toplam = 0
for kitap_adi,sayfa_sayisi in kitaplar:
    toplam =toplam + sayfa_sayisi

print("Toplam sayfa sayısı: ",toplam)
