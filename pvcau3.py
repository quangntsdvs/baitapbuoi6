class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def partition(head, x):
  # Initialize two dummy nodes for two separate lists: one for less than x and one for greater than or equal to x
  before_head = ListNode()
  before = before_head
  after_head = ListNode()
  after = after_head

  # Traverse the original list
  current_node = head
  while current_node:
      if current_node.value < x:
          # Append nodes with value less than x to the before list
          before.next = current_node
          before = before.next
      else:
          # Append nodes with value greater than or equal to x to the after list
          after.next = current_node
          after = after.next
      current_node = current_node.next

  # Connect the two lists
  after.next = None  # Set the next of the last node in the after list to None
  before.next = after_head.next  # Connect the before list to the after list

  # Return the head of the before list
  return before_head.next

def print_list(head):
  result = []
  while head:
      result.append(head.value)
      head = head.next
  print(result)

# Example usage:
# Create a linked list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(8)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(10)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)

# Print original list
print("Original list:")
print_list(head)

# Partition around value x = 5
x = 5
partitioned_head = partition(head, x)

# Print list after partitioning
print(f"List after partitioning around {x}:")
print_list(partitioned_head)
