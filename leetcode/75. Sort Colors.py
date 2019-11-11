def sortColors(nums):
    colorArr = [0] * 3
    
    for i in range(len(nums)):
        colorArr[nums[i]] += 1

    print(colorArr)
    for i in range(len(nums)):
        if i < colorArr[0]:
            nums[i] = 0
        elif i < colorArr[0] + colorArr[1]:
            nums[i] = 1
        else:
            nums[i] = 2

    return nums
            
nums = [2,0,2,1,1,0]
print(sortColors(nums))
