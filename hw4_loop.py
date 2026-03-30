start_number = int(input("Start number: "))
finish_number = int(input("Finish number :"))

odd_total = 0

print("Odd numbers:")
for sayi in range(start_number,finish_number+1):
    if sayi % 2 !=0:
        print(sayi)
        odd_total+=sayi


print("Total of odd numbers: ",odd_total)

