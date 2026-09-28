class Node:

    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class Deque:

    def __init__(self):
        self.head = None 
        self.tail = None  
        self.count = 0 


    def push_left(self, data):
        new_node = Node(data, prev_node=None, next_node=self.head)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            self.head = new_node

        self.count += 1
        print(f"Pushed '{data}' to the left end.")


    def push_right(self, data):
        """
        Adds a new node at the back (right end) of the deque.
        """
        new_node = Node(data, prev_node=self.tail, next_node=None)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.count += 1
        print(f"Pushed '{data}' to the right end.")


    def pop_left(self):
        if self.is_empty():
            print("Error: the deque is empty, there is nothing to pop.")
            return None

        node_to_remove = self.head
        self.head = node_to_remove.next_node

        if self.head is not None:
            self.head.prev_node = None
        else:
            self.tail = None

        self.count -= 1
        print(f"Popped '{node_to_remove.data}' from the left end.")
        return node_to_remove.data


    def pop_right(self):
        if self.is_empty():
            print("Error: the deque is empty, there is nothing to pop.")
            return None

        node_to_remove = self.tail
        self.tail = node_to_remove.prev_node

        if self.tail is not None:
            self.tail.next_node = None
        else:
            self.head = None

        self.count -= 1
        print(f"Popped '{node_to_remove.data}' from the right end.")
        return node_to_remove.data


    def is_empty(self):
        return self.head is None


    def print(self):
        if self.is_empty():
            print("The deque is empty.")
            return

        print("Deque contents (left to right):")
        current = self.head
        position = 1
        while current is not None:
            print(f"  {position}. {current.data}")
            current = current.next_node
            position += 1


if __name__ == "__main__":
    deque = Deque()

    deque.push_right("Second")
    deque.push_left("First")
    deque.push_right("Third")
    deque.push_left("Zeroth")

    deque.print()

    deque.pop_left()
    deque.pop_right()

    deque.print()

    deque.push_right("New Last")
    deque.print()