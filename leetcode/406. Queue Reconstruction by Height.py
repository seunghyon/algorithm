def reconstructQueue(people):

    people.sort(key = lambda x: (-x[0],x[1]))
    print(people)
    result = []
    for h,k in people:
        result.insert(k,(h,k))
    return result
       
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(reconstructQueue(people))
