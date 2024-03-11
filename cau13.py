class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def find_middle_node(head):
  slow_pointer = head
  fast_pointer = head

  while fast_pointer and fast_pointer.next:
      slow_pointer = slow_pointer.next
      fast_pointer = fast_pointer.next.next

  return slow_pointer

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Find the middle node
middle_node = find_middle_node(head)

print("Middle node:", middle_node.value)  # Output: 3
