grade1 = float(input("first grade: "))
grade2 = float(input("second grade: "))
grade3 = float(input("third grade: "))

mean = (grade1 + grade2 + grade3)/3

rounded_mean = round(mean,1)
print(f"Ortalama: {rounded_mean}")
