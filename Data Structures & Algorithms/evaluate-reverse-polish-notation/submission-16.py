class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if len(token)>1 or token.isdigit() :
                stack.append(int(token))
            else:
                if token == '+':
                    stack.append(stack.pop()+stack.pop())
                elif token == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(float(b)/a))
                else:
                    stack.append(stack.pop()*stack.pop())
        return stack[0]
