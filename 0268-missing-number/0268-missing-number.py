class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash = [False] * (len(nums) + 1)
        for i in range(len(nums)):
            hash[nums[i]] = 1
        for i in range(len(nums) + 1):
            if hash[i] == 0:
                return i
        
        