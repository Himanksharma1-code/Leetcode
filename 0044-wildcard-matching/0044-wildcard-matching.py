class Solution(object):
    def isMatch(self, s, p):
        s_idx, p_idx = 0, 0
        star_idx = -1
        s_match = 0
        
        while s_idx < len(s):
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                s_match = s_idx
                p_idx += 1
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_match += 1
                s_idx = s_match
            else:
                return False
                
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)