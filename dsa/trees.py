from graphviz import Digraph
from IPython.display import SVG
from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def _add(self, current, value):
        
        if self.root == None:
            self.root = Node(value)
        else:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self._add(current.left, value)
            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self._add(current.right, value)
      
    def add(self, value):
        new_node = Node(value)
        
        if self.root == None:
            self.root = new_node
            
        else:
             self._add(self.root, value)
    
    def delete(self,root, key):
        if not root:
            return None

        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = self.find_min(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)

        return root

    def find_min(self,root):
        while root.left:
            root = root.left
        return root
        

    def _search(self, node, value):
        if node is None or node.value == value:
            return node          
        
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right,value) 
        
    def search(self, value):
        result = self._search(self.root,value)
        
        if result is None:
            print(f"NO node with value {value} found in BST!")
        elif result.value == value:
            print(f"YES, a node with value {value} found in BST!")
    
    
    def visit(self, node):
        print(node.value)

    def preorder(self, current):
        if current is not None:
            self.visit(current)
            self.preorder(current.left)
            self.preorder(current.right)
        
    def preprint(self):
        self.preorder(self.root)

    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)
            self.visit(current)
            self.inorder(current.right)
    
    def inprint(self):
        self.inorder(self.root)

    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            self.visit(current)
            
    def postprint(self):
        self.postorder(self.root)
    
    def level_order_traversal(self,root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_vals = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_vals)

        return res

    def levelprint(self):
        levellist = self.level_order_traversal(self.root)
        for item in levellist:
            print(item)
                
    def visualize(self):
        dot = Digraph(comment='Binary Tree')
        
        def add_nodes_edges(node):
            if node is None:
                return
            dot.node(str(node.value), str(node.value))
            if node.left is not None:
                dot.edge(str(node.value), str(node.left.value))
                add_nodes_edges(node.left)
            if node.right is not None:
                dot.edge(str(node.value), str(node.right.value))
                add_nodes_edges(node.right)
        
        add_nodes_edges(self.root)
        return SVG(dot.pipe(format='svg'))

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        q = deque([self.root])

        while q:
            current = q.popleft()

            if current.left is None:
                current.left = new_node
                return
            elif current.right is None:
                current.right = new_node
                return
            else:
                q.append(current.left)
                q.append(current.right)

    def level_order_traversal(self):
        if not self.root:
            return []

        res = []
        q = deque([self.root])

        while q:
            level_size = len(q)
            level_vals = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_vals)

        return res

    def levelprint(self):
        levels = self.level_order_traversal()
        for level in levels:
            print(level)

    # Traversals: preorder, inorder, postorder
    def visit(self, node):
        print(node.value)

    def preorder(self, current):
        if current is not None:
            self.visit(current)
            self.preorder(current.left)
            self.preorder(current.right)

    def preprint(self):
        self.preorder(self.root)

    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)
            self.visit(current)
            self.inorder(current.right)

    def inprint(self):
        self.inorder(self.root)

    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            self.visit(current)

    def postprint(self):
        self.postorder(self.root)

    def visualize(self):
        dot = Digraph(comment='Binary Tree (General)')

        def add_nodes_edges(node):
            if node is None:
                return
            node_id = str(id(node))
            dot.node(node_id, str(node.value))
            if node.left:
                dot.edge(node_id, str(id(node.left)))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(node_id, str(id(node.right)))
                add_nodes_edges(node.right)

        add_nodes_edges(self.root)
        return SVG(dot.pipe(format='svg'))


class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # height of this node


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        # New root of this subtree
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # New root of this subtree
        return y

    def _insert(self, node, value):
        # 1) Normal BST insert
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # 2) Update height
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # 3) Get balance factor
        balance = self.get_balance(node)

        # 4) If unbalanced, do rotations

        # Case 1: Left Left
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Case 2: Right Right
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Case 3: Left Right
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4: Right Left
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    # Simple preorder traversal to show structure
    def _preorder(self, node):
        if not node:
            return
        print(node.value, end=" ")
        self._preorder(node.left)
        self._preorder(node.right)

    def preprint(self):
        self._preorder(self.root)
        print()
        
    def visualize(self):
        dot = Digraph(comment="AVL Tree")

        def add_nodes_edges(node):
            if not node:
                return

            node_id = str(id(node))

            # If value is a (language, speed) tuple, show only language name
            if isinstance(node.value, tuple):
                label = str(node.value[0])
            else:
                label = str(node.value)

            dot.node(node_id, label)

            if node.left:
                left_id = str(id(node.left))
                dot.edge(node_id, left_id)
                add_nodes_edges(node.left)

            if node.right:
                right_id = str(id(node.right))
                dot.edge(node_id, str(id(node.right)))
                add_nodes_edges(node.right)

        add_nodes_edges(self.root)
        return SVG(dot.pipe(format="svg"))
