class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for path in paths :
            files = path.split()
            for file in files[1:]:
                ind = file.index("(")
                text = file[ind+1:-1]
                dic[text].append(files[0]+"/"+file[:ind])
        return [dic[text] for text in dic if len(dic[text])>1] 