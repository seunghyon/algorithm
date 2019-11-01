def searchRange(nums,target):
    
    left,right = 0,len(nums)-1
    
    while left <= right:
        mid = (left + right) //2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
        else:
            left, right = mid, mid
            while 0 < left and nums[left-1] == target:
                left -= 1
            while right < len(nums)-1 and nums[right+1] == target:
                right += 1
            return [left,right]

    return [-1,-1]

nums,target = [5,7,7,8,8,10],6
print(searchRange(nums, target))
