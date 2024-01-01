# 1ST
def findHighAccessEmployees(at):
    mp = {}
    for t in at:
        m = int(t[1][:2])
        s = int(t[1][2:])
        if t[0] not in mp:
            mp[t[0]] = [(m*60)+s]
        else:
            mp[t[0]].append((m*60)+s)
    # return mp
    ans = []
    for key,value in mp.items():
        if len(value)>=3:
            value.sort()
            i = 0
            while i+2<len(value):
                if value[i+2]-value[i]<60 and key not in ans:
                    ans.append(key)
                    i = i+2
                i+=1
    return ans

# 2ND
def smallestTrimmedNumbers(nums, queries):
    ans, trimmed = [], {}
    for k, trim in queries:
        trimmed.setdefault(trim, sorted([(num[-trim :], i) for i, num in enumerate(nums)]))
        ans.append(trimmed[trim][k - 1][1])
    return ans

# 3RD
def combinationSum3(k, n):
    temp = []
    ans = []
    def solve(ind,k,ans,temp,s,n):
        if s==n and k==0:
            ans.append(list(temp))
            # print(temp)
            return 
        if s>n:
            return 
        for i in range(ind,10):
            if i>n:
                break
            temp.append(i)
            solve(i+1,k-1,ans,temp,s+i,n)
            temp.pop()
        
    solve(1,k,ans,temp,0,n)
    return ans

