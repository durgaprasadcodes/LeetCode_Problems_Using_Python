class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                a = stack.pop()
                b = stack.pop()
                
                if token == "+":
                    stack.append(b + a)
                    
                elif token == "-":
                    stack.append(b - a)
                    
                elif token == "*":
                    stack.append(b * a)
                    
                else:  # division
                    # truncate toward zero (important!)
                    stack.append(int(b / a))
                    
            else:
                stack.append(int(token))
                
        return stack[0]
    
s=Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(s.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 4 + (13 / 5) = 4 + 2 = 6
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # Output: 22