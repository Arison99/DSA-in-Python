class Solution:
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s or len(s) == 1:
            return s

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Even length palindromes
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

# Example usage:
s1 = "babad"
s2 = "cbbd"
solution = Solution()
print(solution.longestPalindrome(s1))  # Output: "bab" or "aba"
print(solution.longestPalindrome(s2))  # Output: "bb"