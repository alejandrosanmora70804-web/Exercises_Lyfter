class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None
        self.count = 0


    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

        self.count += 1
        print(f"Inserted '{data}' into the tree.")


    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)


    def is_empty(self):
        """
        Returns True if the tree has no nodes.
        """
        return self.root is None


    def print(self):
        if self.is_empty():
            print("The tree is empty.")
            return

        print("Tree contents (indented by depth):")
        self._print_recursive(self.root, depth=0)


    def _print_recursive(self, current_node, depth):
        if current_node is None:
            return

        indent = "  " * depth
        print(f"{indent}- {current_node.data}")

        if current_node.left is not None or current_node.right is not None:
            if current_node.left is not None:
                self._print_recursive(current_node.left, depth + 1)
            else:
                print(f"{'  ' * (depth + 1)}- (no left child)")

            if current_node.right is not None:
                self._print_recursive(current_node.right, depth + 1)
            else:
                print(f"{'  ' * (depth + 1)}- (no right child)")


if __name__ == "__main__":
    tree = BinaryTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    tree.print()