'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
'''


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curmin = nums[0]
        for k in range(1,len(nums)):
            while len(stack)>0 and nums[k]>=stack[-1][0]:
                stack.pop()
            if len(stack)>0 and nums[k]>stack[-1][1]:
                return True
            
            stack.append((nums[k], curmin))
            curmin = min(curmin, nums[k])
        return False
        
