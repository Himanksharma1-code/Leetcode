class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        furthest = 0
        
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = furthest
                
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps