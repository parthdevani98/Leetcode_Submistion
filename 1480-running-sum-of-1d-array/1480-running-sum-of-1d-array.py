class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []  # Initialize an empty list to store the running sum.
        current_sum = 0  # Initialize a variable to keep track of the current sum.

        for num in nums:
            current_sum += num  # Add the current number to the current sum.
            running_sum.append(current_sum)  # Append the current sum to the running_sum list.

        return running_sum
            