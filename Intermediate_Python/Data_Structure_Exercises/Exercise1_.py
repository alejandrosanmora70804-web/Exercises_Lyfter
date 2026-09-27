class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0


    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.count += 1
        print(f"Pushed '{data}' onto the stack.")


    def pop(self):
        if self.is_empty():
            print("Error: the stack is empty, there is nothing to pop.")
            return None

        node_to_remove = self.top
        self.top = node_to_remove.next_node
        self.count -= 1
        print(f"Popped '{node_to_remove.data}' from the stack.")
        return node_to_remove.data


    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("the stack is empty.")
            return

        print("Stack contents (top to bottom):")
        current = self.top
        position = 1
        while current is not None:
            print(f" {position}. {current.data}")
            current  = current.next_node
            position += 1

if __name__ == "__main__":
    stack = Stack()

    stack.push("First")
    stack.push("Second")
    stack.push("Third")

    stack.display()

    stack.pop()

    stack.display()

    stack.push("Fourth")
    stack.display()