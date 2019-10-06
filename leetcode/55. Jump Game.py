def canJump(nums):
    n = len(nums)
    if n <= 1:
        return True

    lastPoint = n-1
    for i in range(n-1,-1,-1):
        if i + nums[i] >= lastPoint:
            lastPoint = i
            
    return lastPoint == 0

nums = [3,2,1,0,4]#[2,3,1,1,4]#
print(canJump(nums))
