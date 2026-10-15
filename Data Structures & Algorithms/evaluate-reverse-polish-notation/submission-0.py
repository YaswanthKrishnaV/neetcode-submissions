class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators =set(["+","-","*","/"])
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            elif c =="+":
                stack.append(stack.pop()+stack.pop())
            elif c =="-":
                stack.append(-stack.pop()+stack.pop())
            elif c =="*":
                stack.append(stack.pop()*stack.pop())
            elif c =="/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))

        return stack[0]
                

                

        