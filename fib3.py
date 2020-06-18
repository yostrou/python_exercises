def fib3(n):
    """
    Recursive implementation of Fibonacci, where each number is sum
    of the previous three numbers
    """

    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2) + fib3(n - 3)


# Prints 1, 3, 17, and 57.
print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(9))
