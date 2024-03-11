class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def remove_duplicates(head):
  if not head:
      return None

  # Use a set to store unique values
  seen_values = set()
  seen_values.add(head.value)
  current_node = head

  while current_node.next:
      if current_node.next.value in seen_values:
          # If the next node's value is a duplicate, remove it
          current_node.next = current_node.next.next
      else:
          # If the next node's value is not a duplicate, add it to the set
          seen_values.add(current_node.next.value)
          current_node = current_node.next

  return head

def print_list(head):
  result = []
  while head:
      result.append(head.value)
      head = head.next
  print(result)

# Example usage:
# Create an unsorted linked list: 1 -> 2 -> 3 -> 2 -> 4 -> 1 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(3)

# Print original list
print("Original list:")
print_list(head)

# Remove duplicates
new_head = remove_duplicates(head)

# Print list after removing duplicates
print("List after removing duplicates:")
print_list(new_head)
