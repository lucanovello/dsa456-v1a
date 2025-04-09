import random

# Node class for BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert function for BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Function to calculate the height of a BST
def height(node):
    if node is None:
        return -1  
    return 1 + max(height(node.left), height(node.right))

# Function to calculate the imbalance of a BST at the root
def imbalance(root):
    if root is None:
        return 0
    return abs(height(root.left) - height(root.right))

if __name__ == "__main__":
    num_trees = 10
    results = []
        
    for i in range(num_trees):
        values = random.sample(range(1, 21), 20) # Generate a random list and build the BST
        root = None
        for val in values:
            root = insert(root, val)
        tree_height = height(root)
        tree_imbalance = imbalance(root)
        results.append((tree_height, tree_imbalance))
        print(f"Tree {i+1}: Height = {tree_height}, Imbalance = {tree_imbalance}")
        
    print("\nSummary (Height, Imbalance):")
    for i, (h, im) in enumerate(results, start=1):
        print(f"Tree {i}: ({h}, {im})")
