# Singly Linked List:

### Node Class

  The Node class represents each element in the linked list.<br>
  It has two attributes: data, which stores the value of the node, and next, which points to the next node in the list.<br>
  The __init__ method initializes a node with optional data and sets the next node to None by default.

### LinkedList Class

    The LinkedList class manages the linked list.
    It has a single attribute head, which points to the first node in the list.
    The __init__ method initializes an empty linked list with a dummy head node.
    The append method adds a new node at the end of the list by traversing the list until it finds the last node.
    The addelement method adds a new node at a specified index in the list.
    The prepending method adds a new node at the beginning of the list.
    The display method prints the elements of the linked list.
    The length method calculates the length of the linked list.
    The deletebydata method deletes a node with a given data value.
    The deletebyindex method deletes a node at a specified index.
    The getindex method returns the index of a node with a given data value.

### Usage

  An instance of LinkedList is created.<br>
  Nodes are added to the linked list using the append method.<br>
  Various operations such as adding, deleting, and retrieving elements are performed on the linked list.
