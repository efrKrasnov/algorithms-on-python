from typing import Self, TypeVar, Generic
from domain.models.list import ListType


NodeDataType = TypeVar("NodeDataType")


class ListIterator(Generic[NodeDataType]):
    def __init__(self, head: ListType | None) -> None:
        self.current: ListType | None = head

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> NodeDataType:
        if not self.current:
            raise StopIteration
        else:
            item: NodeDataType = self.current.value
            self.current = self.current.next
            return item
