from domain.interfaces.list import IList
from domain.models.list import SinglyLinkedNode
from typing import TypeVar, Generic

from domain.services.list_iterator import ListIterator


NodeDataType = TypeVar("NodeDataType")

class SinglyLinkedList(IList, Generic[NodeDataType]):
    def __init__(self):
        self.head: SinglyLinkedNode[NodeDataType] | None = None
    
    def append(self, value: NodeDataType) -> None:
        new_node = SinglyLinkedNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def prepend(self, value: NodeDataType) -> None:
        if not self.head:
            self.append(value)
        else:
            last_node: SinglyLinkedNode[NodeDataType] = self.head
            while last_node.next:
                last_node = last_node.next
            new_node = SinglyLinkedNode(value)
            last_node.next = new_node
                
    
    def delete(self) -> NodeDataType | None:
        node = self.head
        if node:
            assert self.head is not None
            self.head = self.head.next
            value = node.value
            del node
            return value
        
    def pop(self) -> NodeDataType | None:
        if not self.head:
            return None
        else:
            last_node: SinglyLinkedNode[NodeDataType] = self.head
            pre_last_node = None
            while last_node.next:
                pre_last_node = last_node
                last_node = last_node.next
            
            if pre_last_node:
                pre_last_node.next = last_node.next
            else:
                self.head = None
                
            value = last_node.value
            del last_node
            return value
            
    
    def remove(self, value: NodeDataType) -> NodeDataType | None:
        if not self.head:
            return None
        else:
            node_to_remove = self.head
            prev_node = None
            while node_to_remove and node_to_remove.value != value:
                prev_node = node_to_remove
                node_to_remove = node_to_remove.next
                
            if node_to_remove:
                if prev_node:
                    prev_node.next = node_to_remove.next
                else:
                    self.head = node_to_remove.next
                result = node_to_remove.value
            else:
                result = None
            return result
    
    def search(self, value: NodeDataType) -> NodeDataType | None:
        if not self.head:
            return None
        else:
            node_to_search = self.head
            while node_to_search and node_to_search.value != value:
                node_to_search = node_to_search.next
                
            if node_to_search:
                return value
            else:
                return None
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def __iter__(self) -> ListIterator:
        return ListIterator[NodeDataType](self.head)
    
    def __str__(self) -> str:
        items = [str(item) for item in self.__iter__()]
        return ' -> '.join(items)
            
            