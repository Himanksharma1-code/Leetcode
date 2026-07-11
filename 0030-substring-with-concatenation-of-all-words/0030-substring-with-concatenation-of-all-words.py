from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = Counter(words)
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        result = []
        
        
        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()
            count = 0 
            
            while right + word_len <= n:
                word = s[right:right+word_len]
                right += word_len
                
                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == num_words:
                        result.append(left)
                        
                        left_word = s[left:left+word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    curr_count.clear()
                    count = 0
                    left = right
        
        return result