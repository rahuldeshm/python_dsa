# max in array
a = [3, 5, 3, 6, 2, 9]
max = a[0]
for i in a:
    if (i > max):
        max = i
print("max", i)

# Prime numbers.
n = 10
k = 0
j = 2
c = True
primes = []
while k < n:
    for i in range(2, j):
        if (j % i == 0):
            c = False
            break
    if c:
        primes.append(j)
        k += 1
    else:
        c = True
    j += 1
print("Primes", primes)

# SubArrays
a = [2, 3, 4, 5, 6]
i = 1
while i < len(a)+1:
    j = i
    while j < len(a)+1:
        k = i-1
        while k < j:
            print(a[k], end="")
            k += 1
        print("")
        j += 1
    i += 1
