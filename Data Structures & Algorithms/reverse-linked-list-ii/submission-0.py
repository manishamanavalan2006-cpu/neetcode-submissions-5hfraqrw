# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode(0)
        dummy.next=head
        before=dummy

        for i in range(left-1):
            before=before.next
        
        cur=before.next

        for j in range(right-left):
            new=cur.next

            cur.next=new.next
            new.next=before.next
            before.next=new
        return dummy.next