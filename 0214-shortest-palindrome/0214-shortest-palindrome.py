class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return ""

        rev_s = s[::-1]
        temp = s + "#" + rev_s
        
        lps = [0] * len(temp)
        for i in range(1, len(temp)):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j

        longest_prefix_len = lps[-1]
        add_front = rev_s[:len(s) - longest_prefix_len]
        return add_front + s