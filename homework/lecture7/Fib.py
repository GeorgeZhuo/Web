# this is the python code to generate fibonacci numbers

def Fib(x):
    list = []
    a, b = 0, 1
    i = 0
    while i < x:
        a, b = b, a + b
        list.append(b)
    list.reverse()
    return list
