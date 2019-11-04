def backtrack(nums, path, temp, result):
    if len(temp) == len(nums):
        result.append(temp[:])
        return

    for i in range(len(nums)):
        if not path[i]:
            path[i] = True
            temp.append(nums[i])
            backtrack(nums, path,temp,result)
            temp.pop()
            path[i] = False

def permute(nums):
    result = []
    path = [False] * len(nums)
    backtrack(nums, path, [],result)
    return result


nums = [1,2,3]
print(permute(nums))
