def solve(arr):
    
    ## // 2 ptr setup
    r = len(arr)-1      # First 2
    l = 0               # Last 1
    i = 0               # iterative ptr
    
    while i < r:
        
        # 1. One 
        if arr[i] == 1:
            i += 1 # // Sort 0, 2 onw will be sorted automatically
        
        # 2. Zero
        elif arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            i += 1
            l += 1
        
        # 3. Two
        else:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
    
    return arr