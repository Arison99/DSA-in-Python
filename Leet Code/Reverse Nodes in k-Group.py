from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}"

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Helper function to reverse a portion of the list
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        # Dummy node to help with edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are at least k nodes left
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the k nodes
            start = group_prev.next
            end = kth.next
            reversed_head = reverse(start, end)

            # Reconnect the reversed part with the rest of the list
            group_prev.next = reversed_head
            start.next = group_next

            # Move to the next group
            group_prev = start

# Helper functions to test the solution
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    print(linked_list_to_list(new_head))
