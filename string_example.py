"""kelime = input("Kelime giriniz: ")
ters_kelime = kelime[::-1]
print(ters_kelime)"""

#string slicing ---> kelime[başlangıç,bitiş,adım]

kelime = input("Bir kelime giriniz: ")
ters_kelime = ""

for harf in kelime:
    ters_kelime = harf + ters_kelime

print(ters_kelime)


