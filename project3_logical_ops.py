sayi = int(input("Bir tamsayı giriniz: "))

if sayi % 2 != 0 and sayi > 20:
    print(f"{sayi} 20'den büyük tek sayıdır.")
else:
    print(f"{sayi} istenilen kriterleri karşılamıyor.")

    sayi = int(input("Bir tamsayı giriniz: "))


"""
if sayi % 2 != 0 and sayi > 20:
    print(sayi, " 20'den büyük tek sayıdır.")
else:
    print(sayi, " istenilen kriterleri karşılamıyor.")
    """