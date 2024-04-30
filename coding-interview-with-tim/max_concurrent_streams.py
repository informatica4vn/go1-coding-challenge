

def max_concurrent_streams(streams): 
    event_list = []
    # expected [(start_time, "start", user_id), (end_time, "end", user_id)]
    for stream in streams: 
        # transform original input json -> event_list format
        """
        user_id = stream[0]
        start_time = stream[1]
        end_time = stream[2]
        """
        user_id, start_time, end_time = stream 
        # split the starting event
        event_list.append((start_time, "start", user_id))
        # split the ending event 
        event_list.append((end_time, "end", user_id))

    event_list.sort()
        # print(event_list)

        # expected event list would be: 
        # starting time sorting in increasing order 
        # sorting "end" before "start"

    current_count = 0 
    max_count = 0

    for event in event_list:
        # event (0, 'start', 'User_001')
        if event[1] == "start":
            current_count += 1 
        else: 
            current_count -= 1
        max_count = max(current_count, max_count)
            
    return max_count

    # return max_concurrent_count


input = [
    ["User_001", 0, 1000],
    ["User_002", 500, 2000],
    ["User_003", 2500, 3000],
    ["User_004", 400, 1400]
]

print(max_concurrent_streams(input))