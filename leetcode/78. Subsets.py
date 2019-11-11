def subset(nums):

    def dfs(n,start,cur):
        if n == len(cur):
            result.append(cur[:])
            return

        for i in range(start,len(nums)):
            cur.append(nums[i])
            dfs(n, i+1, cur)
            cur.pop()

    result = []

    for i in range(len(nums)+1):
        dfs(i,0,[])

    return result

nums = [1,2,3]
print(subset(nums))
