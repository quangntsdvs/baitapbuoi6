class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
  def __init__(self, value):
      self.head = Node(value)
      self.tail = self.head
      self.length = 1

  def append(self, value):
      new_node = Node(value)
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1

  def prepend(self, value):
      new_node = Node(value)
      new_node.next = self.head
      self.head = new_node
      self.length += 1

  def insert(self, index, value):
      if index >= self.length:
          self.append(value)
          return
      if index == 0:
          self.prepend(value)
          return
      new_node = Node(value)
      leader = self._traverse_to_index(index - 1)
      new_node.next = leader.next
      leader.next = new_node
      self.length += 1

  def remove(self, index):
      if index == 0:
          self.head = self.head.next
          self.length -= 1
          return
      leader = self._traverse_to_index(index - 1)
      node_to_remove = leader.next
      leader.next = node_to_remove.next
      self.length -= 1

  def _traverse_to_index(self, index):
      current_node = self.head
      count = 0
      while count != index:
          current_node = current_node.next
          count += 1
      return current_node

  def print_list(self):
      current_node = self.head
      while current_node:
          print(current_node.value, end=" -> ")
          current_node = current_node.next
      print("None")

# Example Usage:
my_list = LinkedList(10)
my_list.append(20)
my_list.append(30)
my_list.prepend(5)
my_list.insert(2, 15)
my_list.print_list()
my_list.remove(2)
my_list.print_list()
