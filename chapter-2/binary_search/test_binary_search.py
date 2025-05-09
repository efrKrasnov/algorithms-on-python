from binary_search import binary_search


def test_binary_search_success() -> None:
    assert binary_search(list(range(0, 100)), 10) is True
    assert binary_search([5], 5) is True
    
    
def test_binary_search_failed() -> None:
    assert binary_search(list(range(0, 100)), 100) is False
    assert binary_search([], 100) is False
    assert binary_search([5], 10) is False