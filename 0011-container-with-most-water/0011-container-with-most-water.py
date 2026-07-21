class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0

        while l<r:
            area=min(height[l],height[r]) * (r-l)
            res=max(area,res)
            
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna