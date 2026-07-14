class Node:
    def __init__(self,key:int, val:int):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        #Define Capacity
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0) #2 dummy nodes acting as head and tail of DLL
        self.tail = Node(0,0)

        #Connect the 2
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.cache[key] = node

        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
