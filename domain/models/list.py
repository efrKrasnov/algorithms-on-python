from typing import Self, TypeVar, Generic


NodeDataType = TypeVar("NodeDataType")


class SinglyLinkedNode(Generic[NodeDataType]):
    def __init__(self, data: NodeDataType, next: Self | None = None):
        self.value: NodeDataType = data
        self.next = next
        
        
class DoublyLinkedNode(Generic[NodeDataType]):
    def __init__(self, data: NodeDataType, next: Self | None = None, prev: Self | None = None):
        self.value: NodeDataType = data
        self.next = next
        
        
class CircularLinkedNode(SinglyLinkedNode, Generic[NodeDataType]):
    pass


ListType = SinglyLinkedNode | DoublyLinkedNode | CircularLinkedNode