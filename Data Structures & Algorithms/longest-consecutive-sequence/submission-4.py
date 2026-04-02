class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums= set(nums)
        longest=0
        lens=[0]
        
        for num in nums:
            if num-1 not in setNums:
                longest=1

                while num+1 in setNums:
                    longest+=1
                    num+=1
            
            lens.append(longest)

        return max(lens)
                
            






        