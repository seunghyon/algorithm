def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    result,prev = 0,0

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[prev][1]:
            if intervals[i][1] < intervals[prev][1]:
                prev = i
            result += 1
        else:
            prev = i

    return result
    
intervals = [[1,2],[1,2],[1,2]]#[[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
