class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        newS=("".join(s.split())).lower()
        newS=newS.translate(str.maketrans('', '', string.punctuation))
        print(newS)
        end = len(newS) // 2
            
        for i in range(end):
            if newS[i] != newS[-(i+1)]:
                return False
            continue

        return True    

            

            
        