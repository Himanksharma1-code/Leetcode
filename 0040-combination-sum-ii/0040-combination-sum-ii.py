class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(start_idx, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            for j in range(start_idx, len(candidates)):
                if candidates[j] > remaining_target:
                    break
                
                if j > start_idx and candidates[j] == candidates[j - 1]:
                    continue
                
                current_combination.append(candidates[j])
                backtrack(j + 1, current_combination, remaining_target - candidates[j])
                current_combination.pop()
                
        backtrack(0, [], target)
        return result