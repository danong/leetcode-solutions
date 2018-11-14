class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        word_dict = set(wordDict)
        # too slow
        results = []
        # def backtrack(temp, start):
        #     if start == len(s):
        #         results.append(' '.join(temp))
        #         return
        #
        #     for i in range(start + 1, len(s) + 1):
        #         if s[start:i] in word_dict:
        #             temp.append(s[start:i])
        #             backtrack(temp, i)
        #             temp.pop()
        #
        # backtrack([], 0)
        # return results

        cache = {len(s): [' ']}

        def sentences(i):
            if i not in cache:
                strings = []
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in word_dict:
                        for tail in sentences(j):
                            if tail != ' ':
                                strings.append(s[i:j] + ' ' + tail)
                            else:
                                strings.append(s[i:j])
                cache[i] = strings
            return cache[i]

        return sentences(0)
