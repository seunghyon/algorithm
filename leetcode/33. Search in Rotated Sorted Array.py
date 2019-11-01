def search(nums,target):
    left,right = 0,len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] < target:
            if nums[left] > nums[mid] and nums[left] <= target:
                right = mid -1
            else:
                left = mid + 1
        elif nums[mid] > target:
            if nums[right] < nums[mid] and nums[right] >= target:
                left = mid + 1
            else:
                right = mid -1
        else:
            return mid

    return -1


nums,target = [4,5,6,7,0,1,2],0
#nums,target = [4,5,6,7,0,1,2],3
print(search(nums,target))
