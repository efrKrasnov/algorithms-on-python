from random import shuffle
from tournament_two import max_tournament_algo

def test_sorted_with_odd_len() -> None:
    arr: list[int] = [i for i in range(1, 10)]
    assert max_tournament_algo(arr) == 9
    
def test_shuffled_with_odd_len() -> None:
    arr: list[int] = [i for i in range(1, 10)]
    shuffle(arr)
    assert max_tournament_algo(arr) == 9 
    
    
def test_sorted_with_even_len() -> None:
    arr: list[int] = [i for i in range(1, 11)]
    assert max_tournament_algo(arr) == 10
    
def test_shuffled_with_even_len() -> None:
    arr: list[int] = [i for i in range(1, 11)]
    shuffle(arr)
    assert max_tournament_algo(arr) == 10
    
    
def test_with_single_item() -> None:
    assert max_tournament_algo([10]) == 10 
    
    
def test_empty() -> None:
    assert max_tournament_algo([]) is None