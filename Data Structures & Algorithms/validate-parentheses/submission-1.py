class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        
        for i, c in enumerate(s):
            if c in '{[(':
                stack.append(c)
            elif c in ')]}':
                if not stack:
                    return False
                
                if stack[-1] == '[' and c == ']':
                    stack.pop()
                elif stack[-1] == '(' and c == ')':
                    stack.pop()
                elif stack[-1] == '{' and c == '}':
                    stack.pop()
                else:
                    return False
            
        return not stack

            

            
            
            
                        

            
            
            
            

        
        