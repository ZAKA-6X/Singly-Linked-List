# Linked List
# why liknklist and not arrays:
#   arrays have some limitations and disadvantages: Size limitation, you can't add an element between

# Types of linked list:
# Single linked list: Farword navigation
# Doubly linked list: Farword and Backward navigation
# Circular linked list: last element linked to the first

# Make a Nodes
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        currentnode = self.head
        while currentnode.next != None:
            currentnode = currentnode.next
        currentnode.next = new_node

    def addelement(self, data, index):
        if index > self.lengh():
            print('Error')
            return
        new_node = Node(data)
        currentnode = self.head
        currentindex = 0
        lastnode = currentnode
        currentnode = currentnode.next
        while currentnode.next != None and currentindex < index:
            lastnode = currentnode
            currentnode = currentnode.next
            currentindex += 1
        lastnode.next = new_node
        new_node.next = currentnode

    def prepending(self, data):
        new_node = Node(data)
        if self.head and self.head.next:
            new_node.next = self.head.next
        self.head.next = new_node
    
    def display(self):
        currentnode = self.head
        print('This is your Linked List: ')
        while currentnode.next != None:
            currentnode = currentnode.next
            print( currentnode.data, end=' -> ')
        print('None')
            
    def lengh(self):
        currentnode = self.head
        lengh = 0
        while currentnode.next != None:
            currentnode = currentnode.next
            lengh += 1
        return lengh 
    
    def deletebydata(self, data):
        currentnode = self.head
        while currentnode.next is not None:
            if currentnode.next.data == data:
                currentnode.next = currentnode.next.next
                return
            currentnode = currentnode.next
        print('Error: there is no element with this DATA')

    def deletebyindex(self, index):
        currentnode = self.head
        currentindex = 0
        while currentnode.next is not None:
            if currentindex == index:
                currentnode.next = currentnode.next.next
                return
            currentnode = currentnode.next
            currentindex += 1
        print('Error: there is no element with this DATA')
                    
    def getindex(self, data):
        currentnode = self.head
        currentindex = 0
        position = -1
        while currentnode.next != None:
            if currentnode.data == data:
                position = currentindex
            currentindex += 1
            currentnode = currentnode.next
        return position
    

        
            
        




Node_List = LinkedList()

Node_List.append(33)
Node_List.append(32)
Node_List.append(78)
Node_List.append(11)
Node_List.append(98)
Node_List.append(3)
Node_List.append(43)
Node_List.append(399)






