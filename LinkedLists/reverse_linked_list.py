# LeetCode #206
# Reverse a singly linked list and return the new head.

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

def reverseList(head):
    prev=None 
    current=head
    
    while current:
        next_temp= current.next
        current.next = prev
        prev = current
        current = next_temp
     
    return prev   
      
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
    
# Test case (no cycle)
values = [1, 2, 3, 4, 5, 6]
head = build_linked_list(values)


op = reverseList(head)
print(op.val)

    
