import math

def threeSumClosest(nums,target):
    nums.sort()
    diff = math.inf
    result = 0
    for p in range(2,len(nums)):
        l = 0
        r = p-1
        while l < r:
            sum = nums[l] + nums[r] + nums[p]
            if target == sum :
                return target
            if abs(target-sum) < diff:
                diff = abs(target-sum)
                result = sum
            if target > sum : l += 1
            else: r -= 1

    return result

nums,target = [-1,2,1,-4],1
print(threeSumClosest(nums,target))
