class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


arr = [Employee("rahul", 120000), Employee("yash", 130000),
       Employee("yash", 220000), Employee("sandesh", 110000)]


# def comparec(a, b):
#     if (a.name < b.name):
#         return True
#     if (a.name == b.name):
#         if (a.salary < b.salary):
#             return True
#         else:
#             False
#     else:
#         return False


# for i in range(len(arr)):
#     for j in range(1, len(arr)-i):
#         if comparec(arr[j], arr[j-1]):
#             temp = arr[j]
#             arr[j] = arr[j-1]
#             arr[j-1] = temp
a = sorted(arr, key=lambda x: (x.name, x.salary))
for k in a:
    print(k.name, k.salary)
