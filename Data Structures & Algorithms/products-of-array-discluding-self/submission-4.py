class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        arr = [1]*len(nums)
        for i in range(1,len(nums)):
            arr[i] = product 
            product *= nums[i]
        product = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            arr[i] *= product
            product *= nums[i]
        return arr