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

  def reverse(self):
      if not self.head or not self.head.next:
          return

      prev_node = None
      current_node = self.head

      while current_node:
          next_node = current_node.next
          current_node.next = prev_node
          prev_node = current_node
          current_node = next_node

      self.head = prev_node

  def print_list(self):
      current_node = self.head
      while current_node:
          print(current_node.value, end=" ")
          if current_node.next:
              print("->", end=" ")
          current_node = current_node.next

# Example Usage:
my_list = LinkedList()
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)
my_list.insert_at_end(4)
my_list.insert_at_end(5)

print("Original singly linked list:")
my_list.print_list()

my_list.reverse()
print()
print("Reversed singly linked list:")
my_list.print_list()
