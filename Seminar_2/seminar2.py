n = int(input())
def func(n):
    for i in range(n):
        n = (-3)**i
        print(n)
    return n
func(n)