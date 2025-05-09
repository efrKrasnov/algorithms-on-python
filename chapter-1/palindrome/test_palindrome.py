from palindrome import (
    is_palindrome_1,
    is_palindrome_2,
    is_palindrome_3
)
    


def test_is_palindrome() -> None:
    assert is_palindrome_1('aabbccbbaa') is True
    assert is_palindrome_1('aabbcdcbbaa') is True
    assert is_palindrome_2('aabbccbbaa') is True
    assert is_palindrome_2('aabbcdcbbaa') is True
    assert is_palindrome_3('aabbccbbaa') is True
    assert is_palindrome_3('aabbcdcbbaa') is True
    
def test_is_not_palindrome() -> None:
    assert is_palindrome_1('aabbcdcbbdaa') is False
    assert is_palindrome_2('aabbcdcbbdaa') is False
    assert is_palindrome_3('aabbcdcbbdaa') is False
    
def test_check_char_is_palindrome() -> None:
    assert is_palindrome_1('a') is True
    assert is_palindrome_2('a') is True
    assert is_palindrome_3('a') is True
    
def test_check_empty_string_is_palindrome() -> None:
    assert is_palindrome_1('') is True
    assert is_palindrome_2('') is True
    assert is_palindrome_3('') is True
    
