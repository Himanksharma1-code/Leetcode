class Solution(object):
    def permute(self, nums):
        result = []
        
        def backtrack(current_path, used):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_path.append(nums[i])
                    
                    backtrack(current_path, used)
                    
                    current_path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return result