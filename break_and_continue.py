"""for x in range(1,11):
    if x ==5:
        print("Döngü 'break' komutu ile devredışı bırakıldı.")
        break
    print(x)
    """

for sayi in range(1,8):
    if sayi == 3:
        continue #3 sayısı ekrana yazdırılmaz,döngü kaldığı yerden devam eder.
    print(sayi)