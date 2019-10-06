def canCompleteCircuit(gas,cost):
    if sum(gas) - sum(cost) < 0 :
        return -1
    tank = start = total = 0

    for i in range(len(gas)):
        tank += (gas[i] - cost[i])
        if tank < 0 :
            start = i+1
            total += tank
            tank = 0

    return start if total + tank >= 0 else -1
            

gas,cost = [1,2,3,4,5],[3,4,5,1,2]
#gas,cost = [2,3,4],[3,4,3]
#gas,cost = [3,3,4],[3,4,4]
print(canCompleteCircuit(gas,cost))
