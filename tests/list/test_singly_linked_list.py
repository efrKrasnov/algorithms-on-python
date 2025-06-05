from domain.services.singly_linked_list import SinglyLinkedList

def test_append():
    """ Проверяем вставку элементов спереди. Так как это односвязный список, 
        то порядок элементов идет в обратном порядке
    """
    lst = SinglyLinkedList()
    assert [item for item in lst] == []
    lst.append(10)
    assert [item for item in lst] == [10]
    lst.append(20)
    assert [item for item in lst] == [20, 10]
    lst.append(30)
    assert [item for item in lst] == [30, 20, 10]

def test_preppend():
    """ Проверяем вставку элементов сзади
    """
    lst = SinglyLinkedList()
    assert [item for item in lst] == []
    lst.prepend(10)
    assert [item for item in lst] == [10]
    lst.prepend(20)
    assert [item for item in lst] == [10, 20]
    lst.prepend(30)
    print(lst)
    assert [item for item in lst] == [10, 20, 30]

def test_delete():
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.delete() == 30
    assert [item for item in lst] == [20, 10]
    assert lst.delete() == 20
    assert [item for item in lst] == [10]
    assert lst.delete() == 10
    assert [item for item in lst] == []
    assert lst.delete() is None
    assert [item for item in lst] == []
    # Выполняем все повторно - вдруг остались косяки
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.delete() == 30
    assert [item for item in lst] == [20, 10]
    assert lst.delete() == 20
    assert [item for item in lst] == [10]
    assert lst.delete() == 10
    assert [item for item in lst] == []
    assert lst.delete() is None
    assert [item for item in lst] == []

def test_pop():
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.pop() == 10
    assert [item for item in lst] == [30, 20]
    assert lst.pop() == 20
    assert [item for item in lst] == [30]
    assert lst.pop() == 30
    assert [item for item in lst] == []
    assert lst.pop() is None
    assert [item for item in lst] == []
    # Выполняем все повторно - вдруг остались косяки
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.pop() == 10
    assert [item for item in lst] == [30, 20]
    assert lst.pop() == 20
    assert [item for item in lst] == [30]
    assert lst.pop() == 30
    assert [item for item in lst] == []
    assert lst.pop() is None
    assert [item for item in lst] == []

def test_remove():
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    lst.append(40)
    assert lst.remove(50) is None
    assert [item for item in lst] == [40, 30, 20, 10]
    assert lst.remove(30) == 30
    assert [item for item in lst] == [40, 20, 10]
    assert lst.remove(10) == 10
    assert [item for item in lst] == [40, 20]
    assert lst.remove(40) == 40
    assert [item for item in lst] == [20]
    assert lst.remove(20) == 20
    assert [item for item in lst] == []
    assert lst.remove(20) is None
    assert [item for item in lst] == []
    lst.append(10)
    lst.append(20)
    lst.append(30)
    lst.append(40)
    assert lst.remove(50) is None
    assert [item for item in lst] == [40, 30, 20, 10]
    assert lst.remove(30) == 30
    assert [item for item in lst] == [40, 20, 10]
    assert lst.remove(10) == 10
    assert [item for item in lst] == [40, 20]
    assert lst.remove(40) == 40
    assert [item for item in lst] == [20]
    assert lst.remove(20) == 20
    assert [item for item in lst] == []
    assert lst.remove(20) is None
    assert [item for item in lst] == []

def test_search():
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.search(10) == 10
    assert lst.search(20) == 20
    assert lst.search(30) == 30
    assert lst.search(40) is None
    


def test_is_empty() -> None:
    lst = SinglyLinkedList()
    assert lst.is_empty() is True
    lst.append(10)
    assert lst.is_empty() is False
    lst.pop()
    assert lst.is_empty() is True
    