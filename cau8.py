class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.value < list2.value:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2

# Example usage:
# Create two sorted linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two lists
merged_list = merge_two_lists(list1, list2)

# Print the merged list
result = []
while merged_list:
    result.append(merged_list.value)
    merged_list = merged_list.next
print(result)
