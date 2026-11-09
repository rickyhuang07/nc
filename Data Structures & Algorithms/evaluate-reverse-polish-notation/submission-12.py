class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
            else:
                if token == "+":
                    res = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "-":
                    res = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "*":
                    res = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "/":
                    res = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
        return stack[0]

            
        
            

        