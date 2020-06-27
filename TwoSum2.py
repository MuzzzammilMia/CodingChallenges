#Solution for https://leetcode.com/problems/two-sum/
#Smarter Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        new = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            
            if temp in new:
                return [i, new[temp]]
            new[nums[i]] = i
            