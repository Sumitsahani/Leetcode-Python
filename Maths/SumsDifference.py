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