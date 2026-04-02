class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = { ')' : '(',
                      '}' : '{',
                      ']' : '[' }
        if len(s) == 0:
            return True

        for c in s:
            if c in closeOpen:
                if stack and stack[-1] == closeOpen[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
            
        return len(stack) == 0
                
        
        




            

            
            
            
                        

            
            
            
            

        
        