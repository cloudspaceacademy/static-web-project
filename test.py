sum = 0
count = 0
number = 1

while count < 2010:
    if number % 2 != 0:
        sum += number
        count += 1
    number += 1

print("Sum of the first 20 odd numbers:", sum)