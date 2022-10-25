def solve(s1, s2):
    ###########################
    ### Helper method
    def helper(s, i):
        cnt = 0 ## // Keep chk on elems to be skipped
        
        while i >= 0:
            # 1. If hash {toh skip}
            if s[i] == '#': cnt += 1 
            
            # 2. Valid but to be skip {prev hash}
            elif cnt: cnt -= 1
            
            # 3. Valid and not to be skipped
            else: break

            # 4. Reduce index in every iter
            i -= 1 
        
        return i
    
    ###########################
    ### Main method
    
    ## // 2 ptr setup
    p1 = len(s1) - 1 
    p2 = len(s2) - 1
    
    while p1 >= 0 or p2 >= 0:
        # 1. Find valid indxes
        v1 = helper(s1, p1)
        v2 = helper(s2, p2)
        
        # 2. Chck cases
        if v1 < 0 and v2 < 0: return True
        
        if (v1 < 0 or v2 < 0) or (s1[v1] != s2[v2]): return False
        
        if v1 == 0 and v2 == 0: return True ## // Dono ko saath 0 hona hoga
        
        # 3. New cur ptrs
        p1 = v1 - 1
        p2 = v2 - 1
        
    

if __name__ == '__main__':
    s1, s2 = 'ab#c', 'ad#c'
    
    print(solve(s1, s2))