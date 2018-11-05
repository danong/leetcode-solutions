class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        char_map = {} # key: char, val: idx
        max_seen = 0
        start_idx = 0
        
        for end_idx, val in enumerate(s):
            if val in char_map:
                start_idx = max(start_idx, char_map[val] + 1)
            char_map[val] = end_idx
            max_seen = max(max_seen, end_idx - start_idx + 1)
        
        return max_seen
