class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            h_l, h_r = height[l], height[r]
            width = r - l
            area = width * (h_l if h_l < h_r else h_r)
            if area > max_area:
                max_area = area
            if h_l < h_r:
                l += 1
            else:
                r -= 1
        return max_area