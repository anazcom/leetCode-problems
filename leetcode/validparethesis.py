# Runtime: 37 ms
# Memory: 16.62 MB
# Link: https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parenthesis = "("; closed_parenthesis = ")"
        open_bracket = "["; closed_bracket = "]"
        open_curly_bracket = "{"; closed_curly_bracket = "}"

        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:
            if ch in [
                open_bracket, open_curly_bracket, open_parenthesis]:
                stack.append(ch)
                continue
            if not stack: return False
            if ch in [
                closed_bracket,closed_curly_bracket,closed_parenthesis
            ] and d[ch] != stack.pop(): return False
        
        return not stack
    
s = Solution()
# assert s.isValid(s = "()") == True, "Wrong Answer"
assert s.isValid(s="{[]}") == True, "Wrong Answer"