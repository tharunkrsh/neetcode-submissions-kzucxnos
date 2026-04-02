class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wap = {}
        complement = 0
        
        for i in range(len(nums)):
            wap[nums[i]]=i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in wap and wap[complement] != i:
                return [i, wap[complement]]
            
        