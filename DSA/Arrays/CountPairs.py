from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        
        return count
sol = Solution()
nums1 = [-1, 1, 2, 3, 1]
target1 = 2
print(sol.countPairs(nums1, target1))

nums2 = [-6, 2, 5, -2, -7, -1, 3]
target2 = -2
print(sol.countPairs(nums2, target2))
