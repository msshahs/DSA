# LeetCode #876
# Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second one.

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next
        

def mid_element(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Helper Function to build linked list from the array list

def build_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Helper to print linked list from any node
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
    

# Test case
values = [1, 2, 3, 4, 5, 6]
head = build_linked_list(values)
middle = mid_element(head)
print("Middle Node and onward:")
print_linked_list(middle)
        
    
