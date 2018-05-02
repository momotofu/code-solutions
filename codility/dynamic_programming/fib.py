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
