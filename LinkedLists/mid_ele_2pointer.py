# LeetCode #876
# Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second one.

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next
        

def mid_element(head):
    # count number of elements inside the linked list find middle and traverse till that element 
    # in this we dont have the length method or the index to approach we only have head to traverse 
    
    count=0
    current = head
    while current:
         count+=1
         current = current.next
         
    mid = count // 2
    current = head 
    for _ in range(mid): 
        current = current.next
    
    return current 


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
        
    
