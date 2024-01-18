from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = deque([0] * (bridge_length-1))
    truck_que = deque(truck_weights)
    sum_weights = 0
    
    while truck_que:
        sum_weights += truck_que[0]
        if truck_que:
            if sum_weights <= weight:
                bridge.append(truck_que.popleft())
            else:
                sum_weights -= truck_que[0]
                bridge.append(0)
        sum_weights -= bridge.popleft()
        answer += 1
        
    return answer+len(bridge)

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     time = 1
#     bridge = 
#     truck_weights = deque(truck_weights)
#     sum_trucks = 0

#     while truck_weights:
#         sum_trucks += truck_weights[0]
#         if sum_trucks <= weight:
#             bridge.append(truck_weights.popleft())
#         else:
#             sum_trucks -= truck_weights[0]
#             bridge.append(0)
#         sum_trucks -= bridge.popleft()
#         time += 1

#     return time + len(bridge)
