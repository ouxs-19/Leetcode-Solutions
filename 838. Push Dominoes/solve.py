class Solution:
    def pushDominoes(self, doms: str) -> str:
        while True:
            tmp = doms
            doms = doms.replace('R.L', 'xxx')      
            doms = doms.replace('R.', 'RR')
            doms = doms.replace('.L', 'LL') 
            if tmp == doms : 
                return  doms.replace('xxx', 'R.L') 