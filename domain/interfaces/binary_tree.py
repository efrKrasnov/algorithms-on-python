from abc import ABC, abstractmethod
from typing import Callable, TypeVar, Generic

NodeDataType = TypeVar("NodeDataType")
LambdaFunc = Callable[[TypeVar], None]


class IBinaryTree(ABC, Generic[NodeDataType]):
    @abstractmethod
    def pre_order_traverse(self, func: LambdaFunc) -> None:
        """Обходит дерево в следующем порядке: Корень -> Левый -> Правый

        :param func: функция, которая будет вызвана для каждого элемента
        """
        pass

    @abstractmethod
    def in_order_traverse(self, func: LambdaFunc) -> None:
        """Обходит дерево в следующем порядке: Левый -> Корень -> Правый

        :param func: функция, которая будет вызвана для каждого элемента
        """
        pass

    @abstractmethod
    def post_order_traverse(self, func: LambdaFunc) -> None:
        """Обходит дерево в следующем порядке: Левый -> Правый -> Корень

        :param func: функция, которая будет вызвана для каждого элемента
        """
        pass

    @abstractmethod
    def level_order_traverse(self, func: LambdaFunc):
        """Обходит дерево в ширниу - т.е. сперва первый слой, потом второй и т.д.

        :param func: функция, которая будет вызвана для каждого элемента
        """
        pass

    @abstractmethod
    def search(self, value: NodeDataType) -> NodeDataType | None:
        """Ищет значение value в дереве

        :param value: искомое значение
        :return: значение, если оно найдено, иначе None
        """
        pass

    @abstractmethod
    def insert(self, value: NodeDataType):
        """ Вставляет элемент в дерево

        :param value: Само значение
        """
        pass

    @abstractmethod
    def delete(self, value: NodeDataType) -> NodeDataType | None:
        """ Удаляет значение из дерева
        
        :param value: Само значение
        :return: Значение, если оно было удалено, иначе None
        """
        pass

    @abstractmethod
    def height(self) -> int:
        """ Возвращает высоту дерева

        :return: высота дерева или -1 если дерево пустое
        """
        pass

    @abstractmethod
    def find_min(self) -> NodeDataType | None:
        """Поиск минимального значения

        :return: минимальное значение или None, если дерево пустое
        """
        pass

    @abstractmethod
    def find_max(self) -> NodeDataType | None:
        """Поиск максимального значения

        :return: максимальное значение или None, если дерево пустое
        """
        pass
