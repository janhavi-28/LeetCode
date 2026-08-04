# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):

        # If the list is empty, return it
        if head is None:
            return head

        # Start from the first node
        current = head

        # Traverse until the last node
        while current.next:

            # If current node and next node have the same value
            if current.val == current.next.val:

                # Skip the duplicate node
                current.next = current.next.next

            else:
                # Move to the next node
                current = current.next

        # Return the updated linked list
        return head