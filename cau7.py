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

  def remove_duplicates(self):
      if not self.head:
          return

      unique_values = set()
      current_node = self.head
      prev_node = None

      while current_node:
          if current_node.value in unique_values:
              prev_node.next = current_node.next
          else:
              unique_values.add(current_node.value)
              prev_node = current_node
          current_node = current_node.next

  def print_list(self):
    current_node = self.head
    while current_node:
        print(current_node.value, end=" ")
        if current_node.next:
            print("->", end=" ")
        current_node = current_node.next
    print()


# Example Usage:
my_list = LinkedList()
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(4)
my_list.insert_at_end(3)
my_list.insert_at_end(4)
my_list.insert_at_end(2)

print("Original Linked List:")
my_list.print_list()

my_list.remove_duplicates()

print("Result Linked List:")
my_list.print_list()
