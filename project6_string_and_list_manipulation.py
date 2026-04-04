cumle = input("Bir cümle giriniz: ")
harf = input("Sorgulamak istediğiniz harfi girin: ")

harf=harf.lower()

kelimeler = cumle.split()
sayac = 0

for kelime in kelimeler:
    if harf in kelime.lower():
        sayac+=1

print(f"'{harf}' harfi {sayac} defa cümlede geçiyor.")