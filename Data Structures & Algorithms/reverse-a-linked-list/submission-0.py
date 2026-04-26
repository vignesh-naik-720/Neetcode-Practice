# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

# head = [5, 6, 2, 4] <-- 5->6->2->4
# prev = None, curr = (5, #6)
# LOOP
# curr ? <-- True
# next_temp = curr.next <-- next_temp = (6, #2)
# curr.next = prev <-- curr.next = None
# prev = curr <-- prev = (5, None)
# curr = next_temp <-- curr = (6, #2)
# prev=>5->
# curr=>6->2->4
# curr ? <-- True
# next_temp = curr.next <-- next_temp = (2, #4)
# curr.next = prev <-- curr.next = (5, None)
# prev = curr <-- prev = (6, #5)
# curr = next_temp <-- curr = (2, #4)
# prev=>6->5->
# curr=>2->4
# curr ? <-- True
# next_temp = curr.next <-- next_temp = (4, None)
# curr.next = prev <-- curr.next = (6, #5)
# prev = curr <-- prev = (2, #6)
# curr = next_temp <-- curr = (4, None)
# prev=>2->6->5->
# curr=>4
# curr ? <-- True
# next_temp = curr.next <-- next_temp = None
# curr.next = prev <-- curr.next = (2, #6)
# prev = curr <-- prev = (4, #2)
# curr = next_temp <-- curr = None
# prev=>4->2->6->5->
# curr=>
# curr ? <-- False
