# for i in range(5):
#     # for j in range(5-i):
#     print("*"*(5-i))
#     # print("")
# i = 0
# while i < 5:
#     print("*"*(5-i))
#     i += 1

# for i in range(5, -5, -1):
#     if (i > 0):
#         print(i*"*")
#     else:
#         print((-i+1)*"*")

for i in range(1, 6):
    # print(f'{"*"*i}{" "*(6-i-1)}{"*"*i}')
    for j in range(i):
        print("*", end="")
    for k in range(6-i-1):
        print(" ", end="")
    for l in range(i):
        print("*", end="")
    print("")
