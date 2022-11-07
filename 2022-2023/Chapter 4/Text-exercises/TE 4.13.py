n = 6
sum = 0
for x in range(1, n):
    if n % x == 0:
        sum += x
print(sum == n)