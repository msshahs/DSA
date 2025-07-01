# LeetCode #141
# Given the head of a linked list, determine if it has a cycle in it.


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

# def isCycle(head):
#     visited = set()
#     current = head;
    
#     while current:
#         if current in visited:
#             return True
#         visited.add(current)
#         current = current.next
#     return False 


# Floyd’s Cycle Detection (2 pointer -> 1 step and 2 steps)
def isCycle(head):
    slow=fast= head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
                
    

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

# Create a cycle: make last node point to node with value 3
cycle_start = head.next.next 
current = head
while current.next:
    current = current.next
current.next = cycle_start 

# Test cycle detection
print("Cycle detected:", isCycle(head)) 
        
    
