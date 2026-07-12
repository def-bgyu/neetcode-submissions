"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Have to get the exact copt of the LinkedList

        # Cant use brute force coz u dont have a future node to save in the pointer of previous nodes

        #Use hasmap, we will create 2passes., one for storing all nodes, then we will add all the pointers

        hashmap ={}
        curr = head

        if not head:
            return None

        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        first = head

        while first:
            # set next pointer
            hashmap[first].next = hashmap[first.next] if first.next else None
    
            # set random pointer  
            hashmap[first].random = hashmap[first.random] if first.random else None
    
            # move forward
            first = first.next
        
        return hashmap[head]




        