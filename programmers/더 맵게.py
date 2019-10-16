import heapq

def solution(scoville,k):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        elif len(scoville) == 0 :
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1+2*min2)
        answer += 1
    return answer

scoville,k = [1,2,3,9,10,11],7
print(solution(scoville,k))
