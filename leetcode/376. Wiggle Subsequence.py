def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums)

    prediff = nums[1]-nums[0]
    count = 2 if prediff != 0 else 1
    print(count)

    for i in range(2,len(nums)):
        diff = nums[i]-nums[i-1]
        if (diff > 0 and prediff <= 0) or (diff < 0 and prediff >= 0 ):
            count += 1
            prediff = diff

    return count

nums = [3,3,3,2,5]#[1,7,4,9,2,5]#[0,0]
print(wiggleMaxLength(nums))
