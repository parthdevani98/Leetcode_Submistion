class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        def reverse_array(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
                
        reverse_array(l = 0, r = len(nums) - 1)
        reverse_array(l = 0, r = k - 1)
        reverse_array(l = k, r = len(nums) - 1)
        
            