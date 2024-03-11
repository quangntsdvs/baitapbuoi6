class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def is_palindrome(head):
  # Step 1: Traverse the linked list and store values in a list
  values = []
  current_node = head
  while current_node:
      values.append(current_node.value)
      current_node = current_node.next

  # Step 2: Use two pointers to compare values
  left, right = 0, len(values) - 1
  while left < right:
      if values[left] != values[right]:
          return False
      left += 1
      right -= 1

  return True

# Example usage:
# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

print(is_palindrome(head))  # Output: True

# Create a non-palindrome linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(is_palindrome(head))  # Output: False
