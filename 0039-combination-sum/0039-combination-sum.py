class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(i, current_combination, total):
            if total == target:
                result.append(list(current_combination))
                return
            
            if i >= len(candidates) or total > target:
                return
            
            current_combination.append(candidates[i])
            backtrack(i, current_combination, total + candidates[i])
            
            current_combination.pop()
            backtrack(i + 1, current_combination, total)
            
        backtrack(0, [], 0)
        return result