from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def removeNode(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
        self.size -= 1
        
    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail
    

class LFUCache:

    def __init__(self, capacity=0):
        self.cache = {}
        self.frequencyMap = defaultdict(DLL)
        self.capacity = capacity
        self.minimumFrequency = 0
    
    def _update_node(self, node, key, value):
        node = self.cache[key]
        previousFreq = node.freq
        node.freq += 1
        node.value = value
        self.frequencyMap[previousFreq].removeNode(node)
        self.frequencyMap[node.freq].addNode(node)

        if previousFreq == self.minimumFrequency and self.frequencyMap[previousFreq].size == 0:
            self.minimumFrequency += 1

        return node.value
    
    def get(self, key):
        if key not in self.cache:
            raise Exception("Key doesn't exist.")
        return self._update_node(self.cache[key], key, self.cache[key].value)
        
        
    def put(self, key, value):
        '''Tests the put function'''

        # if capacity of cache is not set
        if not self.capacity:
            raise Exception("Cache capacity is not initialized.")

        # if key in cache then update the value and rearrange the dll in frequency map
        if key in self.cache:
            self._update_node(self.cache[key], key, value)

        else:
            # if cache capacity is full then delete the tail
            if len(self.cache) == self.capacity:               
                previousTail = self.frequencyMap[self.minimumFrequency].removeTail()
                del self.cache[previousTail.key]
            
            node = ListNode(key, value)
            self.frequencyMap[1].addNode(node)
            self.cache[key] = node
            self.minimumFrequency = 1