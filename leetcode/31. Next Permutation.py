def reverse(nums,start):
    low,high = start,len(nums)-1
    while low < high:
        nums[low],nums[high] = nums[high],nums[low]
        low,high = low+1,high-1

def nextPermutation(nums):
    i = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i > 0 :
        j = i
        while j < len(nums) and nums[i-1] < nums[j]:
            j += 1
        nums[i-1],nums[j-1] = nums[j-1],nums[i-1]

    reverse(nums,i)

    return nums


    
nums = [3,2,1]#[1,2,3]
print(nextPermutation(nums))
