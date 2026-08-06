limit = (input)
target = (input)
count = 0
target = 0
found = "No"
for i in range (1, limit+1):
    if i % 3 == 0:
        count += 1
        total += i
        if i == target:
            found = "Yes"
            print("Count:",count)
            print("Sum:",total)
            print("Target Found:",found)