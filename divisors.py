number = int(input("number: "))
factors = []

for i in range(1, number):
    if number % i == 0:
        factors.append(i)

factors.append(number)
for factor in factors:
    print(factor)