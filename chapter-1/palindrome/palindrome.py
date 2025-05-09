def is_palindrome_1(word: str) -> bool:
    return word[::-1] == word


def is_palindrome_2(word: str) -> bool:
    while len(word) > 1:
        if word[0] != word[-1]:
            return False
        word = word[1: -1]
    
    return True


def is_palindrome_3(word: str) -> bool:
    start_pos = 0
    end_pos = len(word) - 1
    
    while start_pos < end_pos:
        if word[start_pos] != word[end_pos]:
            return False
        start_pos += 1
        end_pos -= 1 
        
    return True