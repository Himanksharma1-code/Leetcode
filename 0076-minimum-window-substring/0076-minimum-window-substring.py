from collections import Counter


class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window_counts = {}
        formed = 0

        ans = float("inf"), None, None
        left = 0

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if (
                char in target_counts
                and window_counts[char] == target_counts[char]
            ):
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                left_char = s[left]
                window_counts[left_char] -= 1
                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]