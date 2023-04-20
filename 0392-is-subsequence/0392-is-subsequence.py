class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        j = 0  # pointer for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # if the characters match, move the pointer for s
                i += 1
            j += 1  # move the pointer for t regardless
        return i == len(s)  # if i has reached the end of s, s is a subsequence of t, else not