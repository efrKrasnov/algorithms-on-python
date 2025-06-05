from domain.services.binary_search_tree import BinarySearchTree


def test_height():
    tree = BinarySearchTree[int]()
    
    # Проверяем высоту пустого дерева
    assert tree.height() == -1
    
    # Проверяем высоту при каждой из вставок
    tree.insert(5)
    assert tree.height() == 0
    tree.insert(3)
    assert tree.height() == 1
    tree.insert(7)
    assert tree.height() == 1
    tree.insert(1)
    assert tree.height() == 2
    tree.insert(4)
    assert tree.height() == 2
    tree.insert(6)
    assert tree.height() == 2
    tree.insert(8)
    assert tree.height() == 2
    
    # Проверяем высоту при удалении элементов
    tree.delete(1)
    assert tree.height() == 2
    tree.delete(4)
    assert tree.height() == 2
    tree.delete(6)
    assert tree.height() == 2
    tree.delete(8)
    assert tree.height() == 1
    tree.delete(3)
    assert tree.height() == 1
    tree.delete(7)
    assert tree.height() == 0
    tree.delete(5)
    assert tree.height() == -1
    
    # Выполняем все повторно
    # Проверяем высоту при каждой из вставок
    tree.insert(5)
    assert tree.height() == 0
    tree.insert(3)
    assert tree.height() == 1
    tree.insert(7)
    assert tree.height() == 1
    tree.insert(1)
    assert tree.height() == 2
    tree.insert(4)
    assert tree.height() == 2
    tree.insert(6)
    assert tree.height() == 2
    tree.insert(8)
    assert tree.height() == 2
    
    # Проверяем высоту при удалении элементов
    tree.delete(1)
    assert tree.height() == 2
    tree.delete(4)
    assert tree.height() == 2
    tree.delete(6)
    assert tree.height() == 2
    tree.delete(8)
    assert tree.height() == 1
    tree.delete(3)
    assert tree.height() == 1
    tree.delete(7)
    assert tree.height() == 0
    tree.delete(5)
    assert tree.height() == -1
    
    
def test_pre_order_traverse():
    items = []
    lambda_func = lambda x: items.append(x)
    tree = BinarySearchTree[int]()
    
    # проверяем пустое дерево
    tree.pre_order_traverse(lambda_func)
    assert items == []
    
    # проверяем дерево с одним элементом
    tree.insert(10)
    tree.pre_order_traverse(lambda_func)
    assert items == [10]
    items.clear()
    
    # проверяем большое дерево
    big_tree = _prepare_tree()
    big_tree.pre_order_traverse(lambda_func)
    assert items == [6, 2, 1, 4, 3, 5, 7, 9, 8]
    
    
def test_in_order_traverse():
    items = []
    def lambda_func(x):
        return items.append(x)
    tree = BinarySearchTree[int]()
    
    # проверяем пустое дерево
    tree.in_order_traverse(lambda_func)
    assert items == []
    
    # проверяем дерево с одним элементом
    tree.insert(10)
    tree.in_order_traverse(lambda_func)
    assert items == [10]
    items.clear()
    
    # проверяем большое дерево
    big_tree = _prepare_tree()
    big_tree.in_order_traverse(lambda_func)
    assert items == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    
def test_post_order_traverse():
    items = []
    def lambda_func(x):
        return items.append(x)
    tree = BinarySearchTree[int]()
    
    # проверяем пустое дерево
    tree.post_order_traverse(lambda_func)
    assert items == []
    
    # проверяем дерево с одним элементом
    tree.insert(10)
    tree.post_order_traverse(lambda_func)
    assert items == [10]
    items.clear()
    
    # проверяем большое дерево
    big_tree = _prepare_tree()
    big_tree.post_order_traverse(lambda_func)
    assert items == [1, 3, 5, 4, 2, 8, 9, 7, 6]
    
    
def test_level_order_traverse():
    items = []
    def lambda_func(x):
        return items.append(x)
    tree = BinarySearchTree[int]()
    
    # проверяем пустое дерево
    tree.level_order_traverse(lambda_func)
    assert items == []
    
    # проверяем дерево с одним элементом
    tree.insert(10)
    tree.level_order_traverse(lambda_func)
    assert items == [10]
    items.clear()
    
    # проверяем большое дерево
    big_tree = _prepare_tree()
    big_tree.level_order_traverse(lambda_func)
    assert items == [6, 2, 7, 1, 4, 9, 3, 5, 8]
    
    
def test_search():
    big_tree = _prepare_tree()
    assert 5 in big_tree
    assert 10 not in big_tree
    
def _prepare_tree() -> BinarySearchTree:
    # Возвращает дерево следующего вида 
    #          6 
    #        /   \
    #       2     7
    #      / \     \ 
    #     1   4     9
    #        / \   /
    #       3   5 8
    
    tree = BinarySearchTree[int]()
    tree.insert(6)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(9)
    tree.insert(8)
    return tree