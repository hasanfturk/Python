"""
sayi = 0
toplam = 0

while sayi<10:
    #print(sayi)
    toplam+=sayi
    sayi+=1

print(toplam)
"""

while True:
    sayi = int(input("Lütfen bir sayı giriniz (çıkmak için -1 giriniz.): "))

    if sayi == -1:
        print("Hoşçakalın...")
        break
    sayinin_karesi = sayi*sayi
    print(f"{sayi} sayısının karesi: {sayinin_karesi}")