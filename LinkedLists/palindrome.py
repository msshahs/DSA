# LeetCode #234
# Check if a linked list is a palindrome (reads the same forward and backward).


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next
        

def isPalindrome(head):
    
    if not head or not head.next:
        return True
    
    slow=fast=head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev=None
    while slow:
        next_node = slow.next
        slow.next =prev
        prev= slow 
        slow= next_node
        
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
    

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
    

# # Test case
# values = [1, 2, 3, 4, 5, 6]

# head = build_linked_list(values)

values = [1, 2, 2, 1]
head = build_linked_list(values)

print("Is Palindrome:", isPalindrome(head))

