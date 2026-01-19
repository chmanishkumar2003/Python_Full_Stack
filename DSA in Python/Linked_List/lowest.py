class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def lowest(head):
    min=head.data
    cr=head.next
    while cr:
        if cr.data < min:
            min=cr.data
        cr=cr.next
    return min

node1=Node(7)
node2=Node(71)
node3=Node(10)
node4=Node(3)
node5=Node(1)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

print("Lowest value in the List is",lowest(node1))
