

"""
# Definition of concurrent streams: 
Sure, let's consider a simple example to illustrate what overlapping means in the context of concurrent streams.

Let's say we have three users with the following stream times:

- User_001: 0 to 1000 (milliseconds)
- User_002: 500 to 1500
- User_003: 700 to 1200

Here's how the timeline looks:

```
User_001: |---------|
User_002:     |---------|
User_003:       |---|
Time:     0....500...700..1000..1200..1500
```

- From 0 to 500, only User_001 is streaming, so there's 1 concurrent stream.
- From 500 to 700, User_001 and User_002 are both streaming, so there are 2 concurrent streams.
- From 700 to 1000, all three users are streaming, so there are 3 concurrent streams.
- From 1000 to 1200, User_002 and User_003 are streaming, so there are 2 concurrent streams.
- From 1200 to 1500, only User_002 is streaming, so there's 1 concurrent stream.

So, the maximum number of concurrent streams is 3, which occurs from 700 to 1000. This is what we mean by "overlapping" streams: the streams of User_001, User_002, and User_003 all overlap during this time period.


# Example
Example input:
```json
[
    ["User_001", 0, 1000],
    ["User_002", 500, 2000],
    ["User_003", 2500, 3000],
    ["User_004", 400, 1400]
]
```

Example output:
```json
"The maximum number of concurrent streams is 3."
```
---

original times:  [(0, 1, 'User_001'), (1000, -1, 'User_001'), (500, 1, 'User_002'), (2000, -1, 'User_002'), (2500, 1, 'User_003'), (3000, -1, 'User_003'), (400, 1, 'User_004'), (1400, -1, 'User_004')]
sorted times:  [(0, 1, 'User_001'), (400, 1, 'User_004'), (500, 1, 'User_002'), (1000, -1, 'User_001'), (1400, -1, 'User_004'), (2000, -1, 'User_002'), (2500, 1, 'User_003'), (3000, -1, 'User_003')]

"""

def max_concurrent_streams(streams):
    times = []
    for stream in streams:
        user, start, end = stream
        times.append((start, 1, user))
        times.append((end, -1, user))
        print("original times: ",times)
    times.sort()
    print("sorted times: ",times)
    counter = 0
    max_counter = 0
    for time in times:
        counter += time[1]
        max_counter = max(max_counter, counter)
    return max_counter

streams = [
    ["User_001", 0, 1000],
    ["User_002", 500, 2000],
    ["User_003", 2500, 3000],
    ["User_004", 400, 1400]
]

print(max_concurrent_streams(streams))