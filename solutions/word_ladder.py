from collections import deque, defaultdict


def build_word_dict(word_list):
    d = defaultdict(list)  # key: placeholder str, value: list of words
    wlen = len(word_list[0])
    for word in word_list:
        for i in range(wlen):
            placeholder = '{}_{}'.format(word[:i], word[i+1:])
            d[placeholder].append(word)
    return d
            
def get_neighbors(word, wdict):
    for i in range(len(word)):
        placeholder = '{}_{}'.format(word[:i], word[i+1:])
        yield from wdict[placeholder]

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wdict = build_word_dict(wordList)
        visited = set()
        visit_queue = deque([(beginWord, 1)])
        while visit_queue:
            cur, depth = visit_queue.popleft()
            if cur == endWord:
                return depth
            visited.add(cur)
            # neighbors = (word for word in wordList if is_neighbor(cur, word) and word not in visited)
            # for neighbor in neighbors:
            for neighbor in get_neighbors(cur, wdict):
                if neighbor not in visited:
                    visit_queue.append((neighbor, depth + 1))
        return 0
        
