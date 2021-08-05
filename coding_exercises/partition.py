class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_list(self, n):
        while(n):
            print(n.val)
            n = n.next
            
    def partition(self, head, x):
        
        #stores nodes less than x
        n = ListNode(0)
        c = n     #a variable to track through the nodes less than x
        #prev = head # tracks through the nodes previous value so that we can connect to a node given it satisifies the condition
        
        node1 = head
        while(node1.val != x):
            node1 = node1.next
            
        node = node1
        prev = node1
        self.print_list(node)
        print(node.val)
        
        while(node):
            if(node.val < x):
                c.next = node
                c = c.next
                
                prev.next = node.next
                node = prev.next
                
            else:
                prev = node
                node = node.next
                
        node = head
        c = n.next
        prev = node
        #this time it will put any element in front of the pivot
        
        while(node.val != x):
            if(c and node.val >= c.val):
                prev.next = c
                c.next = node
                node = c
                c = c.next
                
            else:
                prev = node
                node = node.next
                
        return head

def create_linkedlist(arr):
    head = ListNode(arr[0])
    node = head
    i = 1
    while(i < len(arr)):
        node.next = ListNode(arr[i])
        node = node.next

    node.next = None
    return head

def print_list(n):
    while(n):
        print(n.val)
        n = n.next

l = create_linkedlist([1,4,3,2,5,2])
print_list(l)
p = Solution
h = p.partition(l, 3)
print_list(h)


