def solve(arr):
    n = len(arr)
    hashmap = {}
    
    for i in range(n):
        if arr[i] in hashmap.keys():
            hashmap[arr[i]] += 1
        
        else:
            hashmap[arr[i]] = 1
    
    nums = hashmap.values()
    nums.sort()
    
    for i in range(1, len(nums)):
        j = i - 1
        
        if nums[i] == nums[j]:
            return False
    
    return True 