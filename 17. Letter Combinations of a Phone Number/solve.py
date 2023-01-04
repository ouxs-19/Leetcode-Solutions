class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        n = len(digits)
        self.words = []
        def solve(i,word):
            if i == n :
                if word : self.words.append(word)
                return 
            for char in dic[digits[i]]:
                solve(i+1,word+char)
        solve(0,"")
        return self.words