class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def reverse_list(head):
  prev_node = None
  current_node = head

  while current_node:
      next_node = current_node.next
      current_node.next = prev_node
      prev_node = current_node
      current_node = next_node

  return prev_node

# Example usage:
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the list
reversed_head = reverse_list(head)

# Print reversed list
while reversed_head:
  print(reversed_head.value, end=" -> ")
  reversed_head = reversed_head.next
