class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list) # charCount : group of Anagrams

        for s in strs:
            count = [0] * 26 # a-z
            for c in s:
                count[ord(c)-ord("a")]+=1
            
            maps[tuple(count)].append(s)
            returnable=[]
        
        for count in maps:
                returnable.append(maps[count])
            
        return returnable
                

        
                
        