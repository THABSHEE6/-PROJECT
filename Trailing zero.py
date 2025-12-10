num = int(input("Enter a number: "))
count = 0

temp = num

while temp % 10 == 0:
    count += 1
    temp //= 10

print("Trailing zeros:", count)
