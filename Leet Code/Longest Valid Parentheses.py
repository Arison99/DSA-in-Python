from typing import Optional, List

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

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        # Count the frequency of each word in words
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []

        # Check each possible starting index
        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)

                else:
                    current_count.clear()
                    count = 0
                    left = right

        return result

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Initialize with a base index for valid substring calculation

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # Reset the base index
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

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
    # Test reverseKGroup
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    print(linked_list_to_list(new_head))

    # Test findSubstring
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(solution.findSubstring(s, words))

    # Test longestValidParentheses
    s = "(()"
    print(solution.longestValidParentheses(s))

    s = ")()())"
    print(solution.longestValidParentheses(s))

    s = ""
    print(solution.longestValidParentheses(s))
