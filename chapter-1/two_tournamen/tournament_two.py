from math import ceil
from typing import Any


def tournament_two(lst: list) -> None | Any:
    if not lst:
        return None
    
    if len(lst) == 1:
        return lst[0]
    
    comparsion_count: int = ceil(len(lst) / 2)
    winners: list[None]  = [None for i in range(comparsion_count)]
    l_len = len(lst)
    
    while l_len != 1:
        w_pos = 0
        c_pos = 0
        cmps = l_len // 2
        
        while cmps:
            if lst[c_pos] > lst[c_pos + 1]:
                winners[w_pos] = lst[c_pos]
            else:
                winners[w_pos] = lst[c_pos + 1]
                
            w_pos += 1
            c_pos += 2
            cmps -= 1
            
        if c_pos != l_len:
            winners[w_pos] = lst[c_pos]
            w_pos += 1
            
        l_len = w_pos
        lst = winners
        
    return winners[0]

