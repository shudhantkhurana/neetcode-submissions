class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                zero_count += 1
            
        if zero_count > 1:
            return [0]*len(nums)

        if zero_count == 1:
            arr = []
            for i in nums:
                if i == 0:
                    arr.append(product)
                else:
                    arr.append(0)
            return arr

        if zero_count == 0:
            arr = []
            for i in nums:
                arr.append(product//i)
            return arr        