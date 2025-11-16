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
