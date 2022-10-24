def solve(nums, target):
    ######################################
    ### Helper Code
    def helper(nums, i, j, l, h, target, res):
        while l < h:
            if nums[l] + nums[h] == target:
                res.append([nums[i], nums[j], nums[l], nums[h]])
                
                ## // Duplicates
                while l < h and nums[l] == nums[l-1]: l += 1
                while l < h and nums[h] == nums[l+1]: h -= 1
            
            elif nums[l] + nums[h] <= target:
                l += 1
            
            else: h -= 1

    ######################################
    ### Main Code
    res = []
    n = len(nums)
    nums.sort()
    
    for i in range(n):
        ## // Duplicates
        if i > 0 and nums[i] == nums[i-1]: continue
        
        for j in range(i+1, n):
            ## // Duplicates
            if j > i+1 and nums[j] == nums[j-1]: continue
            
            sm1 = nums[i] + nums[j]
            sm2 = target - sm1
            
            helper(nums, i, j, j+1, n-1, sm2, res)
    
    return res
            
            

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    
    print(solve(nums, target))