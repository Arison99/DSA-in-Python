class Solution:
    def isMatch(self, s, p):
        # Create a DP table with dimensions (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* etc.
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if p[j - 2] == '.' or p[j - 2] == s[i - 1] else False)
        
        return dp[len(s)][len(p)]

# Example usage
matcher = Solution()
print(matcher.isMatch("aa", "a"))  # Output: False
print(matcher.isMatch("aa", "a*"))  # Output: True
print(matcher.isMatch("ab", ".*"))  # Output: True