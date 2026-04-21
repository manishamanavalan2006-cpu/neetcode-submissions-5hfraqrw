# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        arr=[]
        while cur:
            arr.append(cur.val)
            cur=cur.next
        
        arr.sort()
        cur=head
        for i in range(0,len(arr)):
            cur.val=arr[i]
            cur=cur.next
        return head
