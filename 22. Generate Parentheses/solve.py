class Solution(object):
    def generateParenthesis(self, n):
        self.expres = []
        self.make_pars("",n,n,0)
        return self.expres
    def make_pars(self,expr,r,l,s):
        if s < 0 :
            return None 
        if r == 0 and l == 0 and s == 0 :
             self.expres.append(expr) 
        if r > 0 : 
            self.make_pars(expr+"(",r-1,l,s+1)
        if l > 0 :
            self.make_pars(expr+")",r,l-1,s-1)
    