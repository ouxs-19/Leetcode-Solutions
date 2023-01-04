class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # This is a nightmare
        n , m = len(matrix) , len(matrix[0])
        cells = defaultdict(set)
        for i in range(n):
            for j in range(m):
                    cells[matrix[i][j]].add((i, j)) 
        ranked = sorted(cells)
        r = defaultdict(list) 
        c = defaultdict(list)
        new_m = [[0]*m for j in range(n)]
        def bfs(new_row,new_column,qs,num):
            seem = set()
            seem_row =  set()
            seem_column =  set()
            
            while(qs):
                rank,idx = heappop(qs)
                if(idx in seem):continue
                i,j = idx
                rank *=-1
                Qs = set([idx])
                while(Qs):
                    next_Qs = set()
                    for Q in Qs:
                        if(Q in seem):continue
                        I,J=Q
                        r[I][1] = rank
                        c[J][1] = rank
                        new_m[I][J]=rank       
                        seem.add(Q)
                        if(I not in seem_row):
                            for j in new_row[I]:
                                if((I,j) in seem or (I,j) in Qs):continue
                                next_Qs.add((I,j))
                            seem_row.add(I)
                            
                        if(J not in seem_column):
                            for i in new_column[J]:
                                if((i,J) in seem  or (i,J) in Qs):continue
                                next_Qs.add((i,J))
                            seem_column.add(J)
                    Qs = next_Qs
        def change(index,num):
            i,j = index
            tmp_row = 1
            if(i not in r):pass
            elif(r[i][0]==num):tmp_row=r[i][1]
            else:tmp_row=r[i][1]+1
            tmp_column = 1
            if(j not in c):pass
            elif(c[j][0]==num):tmp_column=c[j][1]
            else:tmp_column=c[j][1]+1
            new_m[i][j] = max(tmp_row,tmp_column)
            r[i] = [num,new_m[i][j]]
            c[j] = [num,new_m[i][j]]
            
        for val in ranked :
            qs = []
            new_row = defaultdict(set)
            new_column = defaultdict(set)
            
            for ind in cells[val]:
                i,j = ind
                new_row[i].add(j)
                new_column[j].add(i)
                change(ind,val)
                heappush(qs,(-new_m[i][j],ind))
            bfs(new_row,new_column,qs,val) 
        return new_m