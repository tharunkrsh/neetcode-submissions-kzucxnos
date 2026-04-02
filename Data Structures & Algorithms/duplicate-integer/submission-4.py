class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedd=sorted(nums)
        for i in range(len(nums)-1):
            if sortedd[i]==sortedd[i+1]:
                return True
        return False
                