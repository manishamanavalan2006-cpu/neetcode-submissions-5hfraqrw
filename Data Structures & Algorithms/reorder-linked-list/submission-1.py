# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle element
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        
        #reverse the second part of list
        secondlist=slow.next
        slow.next=None

        prev=None
        cur=secondlist
        while cur is not None:
            nextnode = cur.next
            cur.next=prev
            prev=cur
            cur=nextnode
        secondlist=prev

        #merging of two list
        firstlist=head
        
        while secondlist is not None:
            temp1=firstlist.next
            temp2=secondlist.next

            firstlist.next=secondlist
            secondlist.next=temp1

            firstlist=temp1
            secondlist=temp2
