def smallestEvenMultiple(n):
    if n%2==0:
        return n
    else:
        return n+n
print(smallestEvenMultiple(5))
