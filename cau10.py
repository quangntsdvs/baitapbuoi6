class ListNode:
  def __init__(self, value=0, next=None):
      self.value = value
      self.next = next

def remove_elements(head, val):
  # Create a dummy node to serve as the head of the result list
  dummy = ListNode(0)
  dummy.next = head
  current_node = dummy

  # Iterate through the list
  while current_node.next:
      # If the next node has the given value, skip it
      if current_node.next.value == val:
          current_node.next = current_node.next.next
      else:
          # Move to the next node
          current_node = current_node.next

  # Return the head of the result list (skipping the dummy node)
  return dummy.next

def print_list(head):
  result = []
  while head:
      result.append(head.value)
      head = head.next
  print(result)

# Example usage:
# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

# Print original list
print("Original list:")
print_list(head)

# Remove elements with value 6
new_head = remove_elements(head, 6)

# Print list after removing elements
print("List after removing elements with value 6:")
print_list(new_head)

# Create the linked list: 7 -> 7 -> 7 -> 7 -> 7
head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(7)

# Print original list
print("Original list:")
print_list(head)

# Remove elements with value 7
new_head = remove_elements(head, 7)

# Print list after removing elements
print("List after removing elements with value 7:")
print_list(new_head)
