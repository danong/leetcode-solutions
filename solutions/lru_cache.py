"""https://leetcode.com/problems/lru-cache"""
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            v = self.cache[key]
            self._remove(v)
            self._add(v)
            return v.val
        else:
            return -1
 
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self._remove(self.cache[key])
        n = Node(key, value)
        self._add(n)
        self.cache[key] = n
        if len(self.cache) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.cache[n.key]
            
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
