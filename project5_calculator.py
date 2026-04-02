while True:
    print("""        1.Toplama
        2.çıkarma
        3.Çarpma
        4.Bölme
        5.Çıkış    """)
    
    secenek = int(input("İşlem numarası giriniz(1-5): "))

    if secenek == 5:
        print("Programdan çıkılıyor...")
        break

    if secenek==1:
        sayi1 =int(input("ilk sayıyı giriniz: "))
        sayi2 =int(input("ikinci sayıyı giriniz: "))
        toplam =sayi1+sayi2
        print(f"Toplam: {toplam}")

    if secenek==2:
        sayi3 =int(input("ilk sayıyı giriniz: "))
        sayi4 =int(input("ikinci sayıyı giriniz. "))
        sonuc =sayi3-sayi4
        print(f"Cevap: {sonuc}")
    if secenek==3:
        sayi5 =int(input("ilk sayıyı giriniz: "))
        sayi6 =int(input("ikinci sayıyı giriniz. "))
        carpim =sayi5*sayi6
        print(f"Çarpım: {carpim}")
    if secenek==4:
        sayi7 =int(input("ilk sayıyı giriniz: "))
        sayi8 =int(input("ikinci sayıyı giriniz. "))
        if sayi8==0:
            print("Bölen kısmına '0' girdiniz,hatalı işlem,tekrar deneyiniz.")   
            continue
        bolum=sayi7/sayi8
        print("Sonuç: ",bolum)
            


print("Hoşçakalın...")