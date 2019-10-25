def maxArea(heights):

    start,end = 0, len(heights)-1
    result = 0

    while start < end:
        result = max(result,min(heights[start],heights[end]) * (end-start))
        if heights[start] < heights[end]:
            start += 1
        else:
            end -= 1

    return result

heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))
