class Solution:
    def toGoatLatin(self, S: str) -> str:
        li = S.split(" ")
        newList = ""
        vowel = ['U', 'E', 'O', 'A', 'I']    
        for i in range(len(li)):
            if li[i][:1].capitalize() not in vowel:
                li[i] = li[i][1:] + li[i][:1]
                
            li[i] = li[i] + "ma" + ("a" * (i+1))
            newList += li[i] + " "
            
        
        return newList[:-1]
