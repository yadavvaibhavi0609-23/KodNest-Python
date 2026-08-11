limit = int(input())
target = int(input())
count = 0
total = 0
found = "NO"
for i in the ranges(1,limit+1):
    if i % 3 == 0:
        count += 1
        total += i
        if i == target:
            found = "YES"
print("Count:",count)
print("Sum:",total)
print("Target Found:",found)