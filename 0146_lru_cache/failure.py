import sys
from typing import Dict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: Dict[int, int] = {}
        self.recency: Dict[int, int] = {}
        self._min_key: int = sys.maxsize
        

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1
        
        self.recency[key] += 1
        if self._min_key == key:
            self._updateMin(key)

        return self.cache.get(key)
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache.keys()) == self.capacity:
            self.cache.pop(self._min_key)
            self.recency.pop(self._min_key)

            self._updateMin(self._min_key)
        
        if len(self.cache.keys()) == 0:
            self._min_key = key
        
        self.cache.update({key: value})
        self.recency.update({key: 0})

    def _updateMin(self, key: int) -> None:
        _min: int = sys.maxsize
        for k, v in self.recency.items():
            _min = min(_min, v)
            if _min == v and k != key:
                self._min_key = k
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)