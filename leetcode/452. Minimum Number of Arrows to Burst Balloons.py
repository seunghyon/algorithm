import math
def findMinArrowShots(points):
    points.sort(key = lambda x: x[1])
    end = -math.inf
    result = 0
    
    for i in range(len(points)):
        if points[i][0] > end:
            end = points[i][1]
            result += 1
            
    return result

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))



    
