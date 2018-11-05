from collections import Counter, defaultdict


def counter_to_tuple(counter):
    chars = [0] * 26
    for char, count in counter.items():
        chars[ord(char) - ord('a')] = count
    return tuple(chars)


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for word in strs:
            wc = Counter(word)
            anagrams[counter_to_tuple(wc)].append(word)
        return [group for group in anagrams.values()]
            
