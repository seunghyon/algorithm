def maxSubArray(nums):
    result = []
    result.append(nums[0])
    for i in range(1,len(nums)):
        result.append(max(nums[i],result[i-1]+nums[i]))

    return max(result)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
