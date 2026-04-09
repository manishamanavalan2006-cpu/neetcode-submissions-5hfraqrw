# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list=[]
        for values  in lists:
            while values:
                sorted_list.append(values.val)
                values=values.next
        sorted_list.sort()
        #create a linked list
        new_linked_list=ListNode(0)
        curr=new_linked_list
        for i in sorted_list:
            curr.next=ListNode(i)
            curr=curr.next
        return new_linked_list.next
