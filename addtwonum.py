class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if j>i:
                    p=target - nums[i]
                    if nums[j] == p:
                        a=j
                        b=i
                        break            
        return ([b,a])
                    
