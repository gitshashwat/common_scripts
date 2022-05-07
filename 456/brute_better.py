'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        curmin = nums[0] #we decide to take a minimum to reduce the complexity of the brute force soln from O(N^3) to O(N^2)
        for j in range(1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[k]>curmin and nums[j]>nums[k]:
                    return True
            curmin = min(curmin, nums[j])
        return False
        
