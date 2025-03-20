from typing import Dict, Optional


class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


# runtime: 13.15%, space: 99.97%
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: Dict[int, Optional[Node]] = {}
        
        self.head: Optional[Node] = Node(-1, -1)
        self.tail: Optional[Node] = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Optional[Node]) -> None:
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def _remove(self, node: Optional[Node]) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1
        
        node: Optional[Node] = self.cache.get(key)
        self.cache.pop(key)
        self._remove(node)
        self._add(node)
        self.cache.update({key: node})

        return self.cache.get(key).val

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            old_node: Optional[Node] = self.cache.get(key)
            self.cache.pop(key)
            self._remove(old_node)
        
        if len(self.cache.keys()) == self.capacity:
            self.cache.pop(self.tail.prev.key)
            self._remove(self.tail.prev)

        new_node: Optional[Node] = Node(key, value)
        self._add(new_node)

        self.cache.update({key: new_node})


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)