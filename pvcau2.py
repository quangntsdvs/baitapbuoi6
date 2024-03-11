class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def nth_to_last(head, n):
  # Initialize two pointers: fast and slow
  slow_pointer = head
  fast_pointer = head

  # Move the fast pointer n steps ahead
  for _ in range(n):
      if not fast_pointer:
          return None  # If n is greater than the length of the list, return None
      fast_pointer = fast_pointer.next

  # Move both pointers simultaneously until the fast pointer reaches the end of the list
  while fast_pointer:
      slow_pointer = slow_pointer.next
      fast_pointer = fast_pointer.next

  # At this point, the slow pointer is at the nth to last element
  return slow_pointer

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Find the 2nd to last element
n = 2
result = nth_to_last(head, n)
if result:
  print(f"The {n}nd to last element is: {result.value}")
else:
  print(f"The list doesn't have {n} elements")
