ogrenciler={
    101:[85,90,78],
    102:[92,88,95],
    103:[75,54,70]
}

for okul_no,sinav_notlari in ogrenciler.items():
    print(f"Okul No: {okul_no}")
    sinav_no=1
    for notu in sinav_notlari:
        print(f"{sinav_no}. - Sınav Notu: {notu}")
        sinav_no+=1
    print()

