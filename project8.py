kitaplar = [
    ("Şeker Portakalı",180),
    ("Simyacı",184),
    ("1984",352),
    ("Hayvan Çiftliği",152)
]

print("Sayfa sayısı 170'ten fazla olan kitaplar:")
toplam_sayfa=0
for kitap,sayfa in kitaplar:
    if sayfa>170:
        toplam_sayfa+=sayfa
        print(kitap)
        

print("Toplam sayfa sayısı: ",toplam_sayfa)