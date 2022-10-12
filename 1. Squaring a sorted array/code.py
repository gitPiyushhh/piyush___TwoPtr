def solve(arr):
    
    ## // 2 ptr setup
    l = 0
    r = len(arr)
    
    ans = []
    
    while l <= r:
        
        if abs(arr[l]) > abs(r[l]):
            ans.append(arr[l]**2)
            l += 1
        
        else:
            ans.append(arr[r]**2)
            r -= 1
        
    ## Srted in reverse order
    return ans[::-1]