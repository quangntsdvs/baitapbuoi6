class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def get_intersection_node(headA, headB):
  if not headA or not headB:
      return None

  # Function to get the length and tail of a linked list
  def get_length_and_tail(node):
      length = 0
      tail = None
      while node:
          length += 1
          if not node.next:
              tail = node
          node = node.next
      return length, tail

  # Get lengths and tails of both lists
  lengthA, tailA = get_length_and_tail(headA)
  lengthB, tailB = get_length_and_tail(headB)

  # If tails are different, lists don't intersect
  if tailA != tailB:
      return None

  # Find the difference in lengths
  diff = abs(lengthA - lengthB)

  # Move head of the longer list forward by the difference
  longer_head = headA if lengthA > lengthB else headB
  shorter_head = headB if lengthA > lengthB else headA

  for _ in range(diff):
      longer_head = longer_head.next

  # Iterate through both lists to find the intersection point
  while longer_head and shorter_head:
      if longer_head == shorter_head:
          return longer_head
      longer_head = longer_head.next
      shorter_head = shorter_head.next

  return None

# Example usage:
# Constructing two sample linked lists: 1->2->3->4->5 and 6->7->8->9->10
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(6)
headB.next = ListNode(7)
headB.next.next = ListNode(8)
headB.next.next.next = headA.next.next  # Introducing intersection

intersection_node = get_intersection_node(headA, headB)

if intersection_node:
  print("Intersection node value:", intersection_node.val)
else:
  print("No intersection found")