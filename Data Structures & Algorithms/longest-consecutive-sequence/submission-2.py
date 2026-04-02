class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        s=set()
        s.add(0)
        for num in nums:
            if (num-1) not in numset:
                count=1
                while (num+1) in numset:
                    count+=1
                    num+=1
                s.add(count)
            continue

        
        return max(s)