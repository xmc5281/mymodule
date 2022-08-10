def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))


def printFibo(n):
    for i in range(n):
        print(fibo(i))


__version__ = '0.1'
