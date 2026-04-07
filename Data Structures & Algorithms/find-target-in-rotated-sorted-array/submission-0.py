class Solution:
    def binary_search(self,nums,start,end,target):
        while start<=end:
            mid = (start+end)//2
            print(start, mid, end)
            if nums[mid]==target: return mid
            elif nums[mid] < target: 
                start = mid+1
                print(start, mid, end)
            else: 
                end = mid-1
                print(start, mid, end)
        return -1


    def search(self, nums: List[int], target: int) -> int:


        l,r=0,len(nums)-1
            
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]: l=mid+1
            else: r = mid
        pivot = l   
        l,r= 0,len(nums)-1
        if nums[pivot] <= target <= nums[r]:
            return self.binary_search(nums,pivot,r,target)
        else:
            return self.binary_search(nums,l,pivot-1,target)


        