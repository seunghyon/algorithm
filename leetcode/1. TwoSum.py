def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        dic.setdefault(num,i)

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dic:
            if dic[diff] != i:
                return [i,dic[diff]]

nums,target = [2,7,11,15] ,9
print(twoSum(nums, target))
