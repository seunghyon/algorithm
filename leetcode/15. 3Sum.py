def threeSum(nums):

    nums.sort()
    print(nums)
    result = set()
    
    for i in range(len(nums)-2):
        start = i+1
        end = len(nums)-1
        while start < end:
            diff = nums[i] - (nums[start] + nums[end])
            if diff == 0 :
                result.add((nums[i],nums[start],nums[end]))
                print(i,start,end)
                start += 1
                end -= 1
            elif diff < 0 :
                start += 1
            else:
                end -= 1
                
    return result



nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
