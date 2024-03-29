class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._insert_recursively(self.root, key, value)

    def _insert_recursively(self, node, key, value):
        if key < node.key:
            if not node.left:
                node.left = TreeNode(key, value)
            else:
                self._insert_recursively(node.left, key, value)
        elif key > node.key:
            if not node.right:
                node.right = TreeNode(key, value)
            else:
                self._insert_recursively(node.right, key, value)
        else:
            node.value = value

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)
