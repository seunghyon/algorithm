def fourSum(nums,target):
    nums.sort()
    result = set()

    for i in range(len(nums)-3):
        for j in range(i+1,len(nums)-2):
            t = target - nums[i] - nums[j]

            sum = 0 
            k = j + 1
            l = len(nums)-1

            while k < l:
                sum = nums[k] + nums[l]
                if t == sum :
                    result.add((nums[i],nums[j],nums[k],nums[l]))
                    k += 1
                    l -= 1
                elif t > sum:
                    k += 1
                else:
                    l -= 1

    return result

    
nums, target = [1, 0, -1, 0, -2, 2],0
print(fourSum(nums,target))
