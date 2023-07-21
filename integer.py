# n = 123
# while n > 0:
#     b = n % 10  # Reminder in integer
#     n = n//10  # Division in integer
#     print(b)

n = 133226
# c = n
# b = len(str(n))
# a = []
# while n > 0:
#     a.append((n % 10)**b)
#     n = n//10
# sum = 0
# for i in a:
#     sum += i
# print("armstrong number") if c == sum else print("not armstrong number")

a = 0
while n > 0:
    a = a*10 + n % 10
    n = n//10

print(a)
