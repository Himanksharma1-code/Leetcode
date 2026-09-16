import collections

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams_map = collections.defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            anagrams_map[key].append(s)
            
        return list(anagrams_map.values())