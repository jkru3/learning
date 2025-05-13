def solution(times):
    # ID check time in seconds
    id_check_time = 5 * 60
    # Initialize the queue and the result array
    queue = []
    result = []
    
    for arrival_time in times:
        # Process the queue if the current arrival time is greater than the first person in the queue's finish time
        while queue and arrival_time >= queue[0]:
            queue.pop(0)
        
        # If the queue has more than 10 people, the person leaves
        if len(queue) > 10:
            result.append(arrival_time)
        else:
            # Calculate the finish time for the current person
            finish_time = max(queue[-1] if queue else arrival_time, arrival_time) + id_check_time
            queue.append(finish_time)
            result.append(finish_time)
    
    return result

s = solution([4, 400, 450, 500])
print(s) # should be [304, 700, 1000, 1300]
