class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        maxL=height[l]
        maxR=height[r]
        res = 0

        while l < r:
            if maxL<=maxR:
                l += 1
                res += maxL - height[l] if maxL - height[l] > 0 else 0
                maxL = max(maxL, height[l])
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r] if maxR - height[r] > 0 else 0
        
        return res

        