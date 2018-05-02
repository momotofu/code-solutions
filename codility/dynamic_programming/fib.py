# top-down approach
def fib(n, lookup):
    """
    Fib using a lookup / momoization
    """
    # Base case
    if n == 0 or n == 1:
        lookup[n] = n

    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    # Return the value corresponding to n
    return lookup[n]

# bottom-up approach
def fib_bu(n):
    # array declaration
    f = [0]*(n + 1)

    # base case assignment
    f[1] = 1

    # calculating the fibonacci and storing the values
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f
