class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def alphaNum(self, c):
            if (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9')):
                return True
            return False
        l, r = 0, len(s) - 1
        while l<r:
            while l<r and alphaNum(self, s[l]) == False:
                l+=1
            while l<r and alphaNum(self, s[r]) == False:
                r-=1    
            
            if s.lower()[l] != s.lower()[r]:
                return False
            l+=1
            r-=1
            

        return True    
 
            

            
        