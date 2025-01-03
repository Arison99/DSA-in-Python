from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # Min-heap to keep track of the smallest elements among the linked lists
        min_heap = []

        # Initialize the heap with the head nodes of each linked list
        for i, node in enumerate(lists):
            if node:  # Only add non-empty nodes
                heapq.heappush(min_heap, (node.val, i, node))

        # Dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        # Merge all lists
        while min_heap:
            val, i, node = heapq.heappop(min_heap)  # Get the smallest element
            current.next = node  # Add it to the merged list
            current = current.next

            if node.next:  # If the popped node has a next node, push it into the heap
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

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
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]

    solution = Solution()
    merged_head = solution.mergeKLists(lists)
    print(linked_list_to_list(merged_head))
