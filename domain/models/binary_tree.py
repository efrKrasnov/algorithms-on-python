from typing import Self, TypeVar, Generic
from dataclasses import dataclass


NodeDataType = TypeVar("NodeDataType")


@dataclass
class TreeNode(Generic[NodeDataType]):
    value: NodeDataType
    left: Self | None = None
    right: Self | None = None
    