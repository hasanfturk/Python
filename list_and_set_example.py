#list and set example
# #verilen listedeki tekrar eden elemanları silip aynı isimde ancak bu sefer içinde tekrar eden eleman olmayan bir liste haline dönüştürünüz.

numbers_list =  [1,2,3,2,4,5,3,6,2,7,5,8]
numbers_set = set(numbers_list)

print(numbers_set)

numbers_list = list(numbers_set)
print(numbers_list)