class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        outer_to_inner = {"]" : "[", "}": "{", ")": "("}
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            elif c in outer_to_inner:
                if stack and stack[-1] == outer_to_inner[c]:
                    stack.pop()
                else:
                    return False
        return not stack
            

            
            
            
            

                