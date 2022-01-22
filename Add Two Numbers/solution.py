# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode(), l2: ListNode()) -> ListNode:
        head1 = l1
        head2 = l2
        output_root = None
        temp_output = output_root
        carry = 0
        while head1 != None or head2 != None:
            l1_val = 0 if head1 is None else head1.val
            l2_val = 0 if head2 is None else head2.val
            
            head3 = ListNode((l1_val + l2_val + carry) % 10)
            carry = (l1_val + l2_val + carry) // 10
            
            if output_root is None:
                output_root = head3
                temp_output = output_root
            else:
                output_root.next = head3
                output_root = output_root.next
            
            head1 = None if head1 is None else head1.next
            head2 = None if head2 is None else head2.next
        else:
            if carry:
                head3 = ListNode((l1_val + l2_val + carry) // 10)
                output_root.next = head3
                output_root = output_root.next
                   
        return temp_output