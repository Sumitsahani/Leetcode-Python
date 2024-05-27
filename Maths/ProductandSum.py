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



def differenceOfSums(n,m):
        Divsum=0
        Nonsum=0
        for i in range(n+1):
            if i%m!=0:
                Nonsum+=i
            else:
                Divsum+=i
        return Nonsum-Divsum


print(differenceOfSums(10,3))


def numIdenticalPairs(nums):
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i !=j:
                    count+=1
        if count==0:
            return 0
        return int(count/2)


nums=[1,2,3,1,1,3]
print(numIdenticalPairs(nums))
    