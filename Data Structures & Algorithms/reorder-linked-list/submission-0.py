# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #fast and slow pyt + reverse list + merge list
        #find middle, reverse 2nd half, merge them

        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
            
        curr = mid
        prev = None
        list2 = []
        while (curr!=None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
            first = head
            second = prev 

        while second.next:
    # save next pointers
            tmp1 = first.next
            tmp2 = second.next
    
    # connect
            first.next = second
            second.next = tmp1
    
    # move forward
            first = tmp1
            second = tmp2

        




        