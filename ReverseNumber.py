num = 45763
reverse = 0
while num > 0:
    reverse = (reverse * 10) + num % 10
    num = num / 10
    num = int(num)
print(reverse)
