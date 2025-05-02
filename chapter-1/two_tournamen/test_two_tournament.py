from random import shuffle
from tournament_two import tournament_two

def test_sorted_with_odd_len() -> None:
    arr: list[int] = [i for i in range(1, 10)]
    assert tournament_two(arr) == 9
    
def test_shuffled_with_odd_len() -> None:
    arr: list[int] = [i for i in range(1, 10)]
    shuffle(arr)
    assert tournament_two(arr) == 9 
    
    
def test_sorted_with_even_len() -> None:
    arr: list[int] = [i for i in range(1, 11)]
    assert tournament_two(arr) == 10
    
def test_shuffled_with_even_len() -> None:
    arr: list[int] = [i for i in range(1, 11)]
    shuffle(arr)
    assert tournament_two(arr) == 10
    
    
def test_with_single_item() -> None:
    assert tournament_two([10]) == 10 
    
    
def test_empty() -> None:
    assert tournament_two([]) is None