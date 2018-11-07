from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = Counter(t)
        counter = len(counts)
        
        start = 0
        end = 0
        shortest_len = float('inf')
        shortest = ''
        
        while end < len(s):
            end_char = s[end]
            if end_char in counts:
                counts[end_char] -= 1
                if counts[end_char] == 0:
                    counter -= 1
            end += 1
            
            while counter == 0:
                if (end - start) < shortest_len:
                    shortest = s[start:end]
                    shortest_len = end - start
                    
                start_char = s[start]
                if start_char in counts:
                    counts[start_char] += 1
                    if counts[start_char] > 0:
                        counter += 1
                start += 1
        return shortest
