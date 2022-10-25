def solve(nums):
    ## // 2 ptr setup
    l = 0
    h = len(nums)-1
    max_area = 0
    
    while l < h:
        height = min(nums[l], nums[h])
        width = h - l
        
        max_area = max(max_area, height * width)
        
        if nums[l] < nums[h]: l += 1
        else: h -= 1
    
    return max_area
        
        

if __name__ == '__main__':
    heights = [1,8,6,2,5,4,8,3,7]
     
    print(solve(heights))