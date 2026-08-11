limit = input()
number = 1
total = 0
while number <= limit:
    if number % 2 == 0:
        total = total + number
print(f"Even Sum:", total)