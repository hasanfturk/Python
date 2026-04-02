"""from random import shuffle
from random import randint,also we can use them like these
"""

import random

sayi = random.randint(0,100)
print(sayi)

isimler = ["Ali","Nur","Cem","Alp"]

print("karıştırmadan önce: ",isimler)
print("liste karıştırılıyor...")
random.shuffle(isimler)
print("karıştırmadan sonra: ",isimler)
