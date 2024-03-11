class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def delete_node_at_index(self, index):
        if index < 0 or not self.head:
            return None  # Index out of range or empty list

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node

        prev_node = None
        current_node = self.head
        count = 0

        while current_node and count != index:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if count == index and current_node:
            deleted_node = current_node
            prev_node.next = current_node.next
            return deleted_node

        return None  # Index out of range

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

# Example Usage:
my_list = LinkedList()
my_list.insert_at_end(299)
my_list.insert_at_end(288)
my_list.insert_at_end(277)
deleted_node = my_list.delete_node_at_index(1)
if deleted_node:
    print("Deleted node:", deleted_node.value)
else:
    print("Node not found or index out of range")
my_list.print_list()
