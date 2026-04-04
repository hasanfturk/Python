cumle = input("Lütfen bir cümle giriniz: ")

cumle = cumle.upper()
print(cumle)

kelimeler = cumle.split()
print(kelimeler)

kelimeler.reverse()
print(kelimeler)

yeni_cumle = " ".join(kelimeler)
print(yeni_cumle)