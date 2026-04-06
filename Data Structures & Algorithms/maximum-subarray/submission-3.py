class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for i in nums:
            sum += i
            if sum > max_sum:
                max_sum = sum
            if i > sum:
                max_sum = max(i, max_sum)
                sum = i
        return max_sum
