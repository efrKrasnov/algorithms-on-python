from domain.interfaces.binary_tree import IBinaryTree, LambdaFunc
from domain.models.binary_tree import TreeNode
from typing import TypeVar, Generic

NodeDataType = TypeVar("NodeDataType")


class _Queue(Generic[NodeDataType]):
    def __init__(self):
        self.items: list[NodeDataType] = []
        
    def enqueue(self, value: NodeDataType):
        self.items.insert(0, value)
        
    def dequeue(self) -> NodeDataType:
        return self.items.pop()
    
    def is_empty(self) -> bool:
        return len(self.items) == 0

class BinarySearchTree(IBinaryTree[NodeDataType]):
    def __init__(self):
        self.root: TreeNode | None = None
        
    def in_order_traverse(self, func: LambdaFunc) -> None:
        self._in_order_traverse(self.root, func)

    def pre_order_traverse(self, func: LambdaFunc) -> None:
        self._pre_order_traverse(self.root, func)

    def post_order_traverse(self, func: LambdaFunc) -> None:
        self._post_order_traverse(self.root, func)

    def level_order_traverse(self, func: LambdaFunc):
        if not self.root:
            return
        
        queue = _Queue[TreeNode]()
        queue.enqueue(self.root)
        
        while not queue.is_empty():
            item = queue.dequeue()
            func(item.value)
            if item.left is not None:
                queue.enqueue(item.left)
            if item.right is not None:
                queue.enqueue(item.right)
                
            
    def search(self, value: NodeDataType) -> NodeDataType | None:
        return self._search(self.root, value)

    def insert(self, value: NodeDataType):
        self.root = self._insert(self.root, value)

    def delete(self, value: NodeDataType):
        self.root = self._delete(self.root, value)

    def height(self) -> int:
        return self._height(self.root)

    def find_min(self) -> NodeDataType | None:
        min_node = self._find_min(self.root)
        return min_node.value if min_node else None

    def find_max(self) -> NodeDataType | None:
        max_node = self._find_max(self.root)
        return max_node.value if max_node else None
    
    def is_balanced(self):
        balanced, height = self._is_balanced(self.root)
        return balanced
    
    def _delete(self, node: TreeNode | None, value: NodeDataType):
        if not node:
            return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._find_min(node.right)
            assert temp is not None
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
                
        return node
        
    def _insert(self, node: TreeNode | None, value: NodeDataType):
        # Условие остановки - у нас не установлен узел - устанавливаем его
        if not node:
            return TreeNode(value)
        # Если значение меньше узла - то переходим в левую часть узла
        if value < node.value:
            node.left = self._insert(node.left, value)
        # Если больше то в правую
        else:
            node.right = self._insert(node.right, value)
        # Возвращаем узел (чтобы ничего не потерять)
        return node
        
    def _height(self, node: TreeNode | None):
        if not node:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))
        
    def _find_min(self, node: TreeNode | None):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node
    
    def _find_max(self, node: TreeNode | None):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node
    
    def _search(self, node: TreeNode | None, value: NodeDataType) -> NodeDataType | None:
        if not node:
            return None
        else:
            if value < node.value:
                return self._search(node.left, value)
            elif value > node.value:
                return self._search(node.right, value)
            return node.value

    def _in_order_traverse(self, node: TreeNode | None, func: LambdaFunc):
        if node is not None:
            self._in_order_traverse(node.left, func)
            func(node.value)
            self._in_order_traverse(node.right, func)

    def _pre_order_traverse(self, node: TreeNode | None, func: LambdaFunc):
        if node is not None:
            func(node.value)
            self._pre_order_traverse(node.left, func)
            self._pre_order_traverse(node.right, func)
    
    def _post_order_traverse(self, node: TreeNode | None, func: LambdaFunc):
        if node is not None:
            self._post_order_traverse(node.left, func)
            self._post_order_traverse(node.right, func)
            func(node.value)
    
    def __contains__(self, key: NodeDataType) -> bool:
        if self.search(key) == key:
            return True
        else:
            return False
        
    def _is_balanced(self, node: TreeNode | None) -> tuple[bool, int]:
        if node is None:
            return (True, -1)
        
        left_balanced, left_height = self._is_balanced(node.left)
        right_balanced, right_height = self._is_balanced(node.right)
        
        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return (is_balanced, height)
    