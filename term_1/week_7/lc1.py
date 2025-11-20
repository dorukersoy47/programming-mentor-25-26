# QUESTION: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0 
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0