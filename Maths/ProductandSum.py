import math
def subtractProductAndSum(n):
    product=1
    sum=0
    while n > 0:
        digit = n % 10
        product *= digit
        sum += digit
        n //= 10
    
    return product - sum


print(subtractProductAndSum(234))
    