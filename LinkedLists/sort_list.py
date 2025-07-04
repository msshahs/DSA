#  Problem 8: Sort a Linked List
# LeetCode #148
# Sort a singly linked list in O(n log n) time and O(1) space if possible.

# LeetCode #234
# Check if a linked list is a palindrome (reads the same forward and backward).


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next
        

def mergelist(list1,list2):
    dummy = ListNode(0)
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    return dummy.next    
        
# Helper Function to build linked list from the array list

def sortlist(head):
    if not head or not head.next:
        return head
    
    # Middle element
    slow, fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    
    mid = slow.next
    slow.next=None
    
    left = sortlist(head)
    right = sortlist(mid)
    
    return mergelist(left,right)


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
    

values = [4, 2, 1, 3]
head = build_linked_list(values)
print("Original:")
print_linked_list(head)

sorted_head = sortlist(head)
print("Sorted:")
print_linked_list(sorted_head)




