class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i, h in enumerate(heights):
            j = i+1
            while j < len(heights):
                area=min([h, heights[j]])*(j-i)
                print(h, heights[j], i, j, area)
                if area>maxA:
                    maxA=area
                j+=1
            print('I is now', i+1)
        return maxA            



        