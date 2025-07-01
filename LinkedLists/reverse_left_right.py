# LeetCode #92
# Reverse a portion of a linked list from position left to right, in 1-based index, and return the head.

# Input:  1 → 2 → 3 → 4 → 5,  left = 2, right = 4  
# Output: 1 → 4 → 3 → 2 → 5


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next
        



# Remove elemets from left to right order

def reverse_left_right(head,left,right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    for _ in range(left-1):
        prev = prev.next
        
    current = prev.next
    for _ in range(right - left):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next=temp
    return dummy.next

        

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


new_head=reverse_left_right(head, 3,5)
print(print_linked_list(new_head))
