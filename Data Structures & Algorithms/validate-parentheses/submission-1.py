class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c not in mapping:
                stack.append(c)
                print(stack)
            else:
                if stack and stack[-1]==mapping[c]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
        