class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signtoOper = { '+' : lambda a, b: int(b) + int(a),
                       '-' : lambda a, b: int(b) - int(a),
                       '*' : lambda a, b: int(b) * int(a),
                       '/' : lambda a, b: int(int(b)/int(a))}

        for c in tokens:
            if stack and c in signtoOper:
                c = signtoOper[c](stack[-1], stack[-2])
                print(c)
                stack.pop()
                stack.pop()
                stack.append(c)
            else:
                stack.append(c)
                print(c)
            
        return int(stack[-1])
            
            


