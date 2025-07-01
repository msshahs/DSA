# LeetCode #203
# Remove all nodes with a specific value from the linked list.

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next= next
        

def remove_element(head,val):
    dummy = ListNode(0)
    dummy.next = head
    current=dummy
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
  
    return dummy.next
    
# Helper to print linked list from any node
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
    
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


target = 6
new_head = remove_element(head, target)
print("After removing value", target)
print_linked_list(new_head)



    
