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
        
        if not head:
            return None
        
        cur=head
        hashmap={}
        while cur:
            hashmap[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            if cur.next:
                hashmap[cur].next=hashmap[cur.next]
            if cur.random:
                hashmap[cur].random=hashmap[cur.random]
            cur=cur.next
        return hashmap[head]





