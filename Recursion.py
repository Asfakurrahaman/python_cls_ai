
def Recursion(num):
    if num == 1:
        return 1
    else:
        return num * Recursion(num - 1)

Result = Recursion(num=5)
print(Result)