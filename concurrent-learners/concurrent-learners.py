

"""
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
"""

def concurrentLearners(streams): 
    for stream in streams:
        print(stream)
    
    #Return the maximum number of concurrent streams
    

streams = [
    ["User_001", 0, 1000],
    ["User_002", 500, 2000],
    ["User_003", 2500, 3000],
    ["User_004", 400, 1400]
]

print(concurrentLearners(streams))