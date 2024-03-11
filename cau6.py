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

  def find_middle_node(self):
      if not self.head:
          return None

      slow_pointer = self.head
      fast_pointer = self.head

      while fast_pointer and fast_pointer.next:
          slow_pointer = slow_pointer.next
          fast_pointer = fast_pointer.next.next

      return slow_pointer

  def print_list(self):
      current_node = self.head
      while current_node:
          print(current_node.value, end=" -> ")
          current_node = current_node.next
      print("None")

# Example Usage:
my_list = LinkedList()
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)
my_list.insert_at_end(4)
my_list.insert_at_end(5)

middle_node = my_list.find_middle_node()
if middle_node:
  print("Middle node value:", middle_node.value)
else:
  print("List is empty")

# Example with even number of nodes
my_list.insert_at_end(6)
middle_node = my_list.find_middle_node()
if middle_node:
  print("Middle node value:", middle_node.value)
else:
  print("List is empty")
