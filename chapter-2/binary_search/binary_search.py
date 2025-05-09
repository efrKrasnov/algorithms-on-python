def binary_search(in_list: list, target) -> bool:
    lo_pos: int = 0
    hi_pos: int = len(in_list) - 1
    
    while lo_pos <= hi_pos:
        mid_pos = (lo_pos + hi_pos) // 2
        
        if target < in_list[mid_pos]:
            hi_pos = mid_pos - 1
        elif target > in_list[mid_pos]:
            lo_pos = mid_pos + 1
        else:
            return True
        
    return False
        
    