def combinationSum(candidates,target):

    result = []
    candidates.sort()
    backtrack(candidates,target,0,[],result)
    return result

def backtrack(nums,target,index,path,result):
    for i in range(index,len(nums)):
        remain = target - nums[i]
        if remain < 0 :
            break
        if remain == 0:
            result.append(path + [nums[i]])
            break
        backtrack(nums,remain,i,path+[nums[i]],result)

candidates,target = [2,3,5], 8
print(combinationSum(candidates,target))
