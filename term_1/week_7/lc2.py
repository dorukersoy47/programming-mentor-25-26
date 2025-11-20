# Question: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)