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
values1 = [1, 2, 3, 4, 5, 6]
values2 = [1,2,3,4,5,6,7,8]
head1 = build_linked_list(values1)
head2 = build_linked_list(values2)

print(print_linked_list(mergelist(head1,head2)))




