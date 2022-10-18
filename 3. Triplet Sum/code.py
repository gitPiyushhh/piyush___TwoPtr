def solve(nums):
    def helper(nums, s, l, res):
        h = len(nums) - 1
        
        while l < h:
            if nums[s] + nums[l] + nums[h] == 0:
                res.append([nums[s], nums[l], nums[h]])
                l += 1
                h -= 1
                
                # Chck for duplcates
                while l < h and nums[l] == nums[l-1]:  l += 1
                while l < h and nums[h] == nums[h+1]: h -= 1
            
            elif nums[s] + nums[l] + nums[h] > 0:
                h -= 1
            
            else: 
                l += 1
    
    
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n-1):
        if i > 0 and nums[i] == nums[i-1]:  continue
        else: helper(nums, i, i+1, res)
    
    return res

