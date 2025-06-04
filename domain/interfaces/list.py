from abc import ABC, abstractmethod
from typing import Self, TypeVar, Generic


NodeDataType = TypeVar("NodeDataType")


class IList(ABC, Generic[NodeDataType]):
    @abstractmethod
    def append(self, value: NodeDataType) -> None:
        """Добавляет элемент в начало списка

        :param value: элемент
        """
        pass
    
    @abstractmethod
    def prepend(self, value: NodeDataType) -> None:
        """ Добавляет элемент в конец списка 
        
        :param value: элемент
        """
        pass
    
    @abstractmethod
    def delete(self) -> NodeDataType | None:
        """Удаляет элемент из начала списка
        
        :return: Удаленный элемент или None
        """
        pass
    
    @abstractmethod
    def pop(self) -> NodeDataType | None:
        """Удаляет элемент из конца списка
        :return: Удаленный элемент или None
        """
        pass
    
    @abstractmethod
    def remove(self, value: NodeDataType) -> NodeDataType | None:
        """ Удаляет объект с конкретным значением

        :param value: само значение
        :return: элемент или None, если объект не найден
        """
        pass
    
    @abstractmethod
    def search(self, value: NodeDataType) -> NodeDataType | None:
        """Ищет объект с конкретным значением 

        :param value: значение
        :return: элемент или None, если объект не найден
        """
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Возвращает информацию о том, пустой список или нет

        :return: пустой список или нет
        """
        pass
   
    