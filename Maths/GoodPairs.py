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