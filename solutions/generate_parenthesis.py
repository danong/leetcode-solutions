class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(p, left, right):
            if right >= left >= 0:
                if right == 0:
                    yield p
                yield from generate(p + '(', left - 1, right)
                yield from generate(p + ')', left, right - 1)

        return list(generate('', n, n))