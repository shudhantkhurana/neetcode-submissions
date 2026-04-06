class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        prod = 1
        if zero_count == 0:
            for i in nums:
                prod *= i
            return [int(prod/i) for i in nums]
        elif zero_count == 1:
            zero_idx = nums.index(0)
            for i in range(len(nums)):
                if zero_idx != i:
                    prod *= nums[i]
            ans = [0]*len(nums)
            ans[zero_idx] = int(prod)
            return ans
        else:
            return [0]*len(nums)

