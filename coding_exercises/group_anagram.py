def groupAnagrams(strs):
    if(len(strs)==0):
        return [[""]]
        
    if(len(strs)==1):
        return [strs]
        
    d = {}
    for x in range(0, len(strs)):
        # s = frozenset(strs[x])
        # i = strs[x]
        s = sorted(strs[x])
        s = ''.join(s)
        if(s not in d):
            t = []
            t.append(strs[x])
            d[s] = t
            print(d)
        
        elif(s in d):
            d[s].append(strs[x])
            
    l = []
    for k,v in d.items():
        l.append(v)
        
    return l

print(groupAnagrams(["ddddddddddg","dgggggggggg"]))