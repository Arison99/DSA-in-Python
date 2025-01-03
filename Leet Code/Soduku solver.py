from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}"
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth: return dummy.next

            start, group_next = group_prev.next, kth.next
            group_prev.next, start.next = reverse(start, group_next), group_next
            group_prev = start

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        word_len, total_len = len(words[0]), len(words[0]) * len(words)
        word_count = {w: words.count(w) for w in words}
        res = []

        for i in range(word_len):
            left, count, curr_count = i, 0, {}
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left + word_len]] -= 1
                        count -= 1
                        left += word_len
                    if count == len(words): res.append(left)
                else:
                    curr_count, count, left = {}, 0, j + word_len
        return res

    def longestValidParentheses(self, s: str) -> int:
        max_len, stack = 0, [-1]
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len

    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, r, c):
            box = {(r//3, c//3, num) for r, c in [(r, x) for x in range(9)] + [(x, c) for x in range(9)] + [(r//3*3+x//3, c//3*3+x%3) for x in range(9)]}
            return not any(board[r][c] == num for r, c in box)

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            if is_valid(num, r, c):
                                board[r][c] = num
                                if backtrack(): return True
                                board[r][c] = '.'
                        return False
            return True

        backtrack()



if __name__ == "__main__":


    # Test solveSudoku
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Solution.solveSudoku(board)
    for row in board:
        print(row)
