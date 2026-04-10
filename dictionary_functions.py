#dictionaries in python are mutable
"""
ogrenci_dict = {100:"Ali Kaya",101:"Zeynep Taş"}
ogrenci_dict[105] = "Kaan Çalışkan"

#ogrenci_dict.pop(101)            #del ogrenciler_dict[101]

ogrenci_dict[100] = "Fatma Kaya"

print(ogrenci_dict)
"""

example_dict = {100:"Ali Kaya", 101:"Zeynep Taş", 103:[30,90,20]}
print(example_dict[103][1])