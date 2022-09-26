a = [1, 2, 3, 4, 5]

def f(a):
    a[0] = 0
    return(a)

b = f(a[:])
print(b)
print(a)