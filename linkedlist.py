from typing import Optional
from node import Node

class LinkedList:
# Attributes
    head: Optional['Node']

# Constructor
    def __init__(self):
        self.head = None  # initially empty list

# Add a New First Node
    def add_front(self, name: str) -> None:
        # Insert a new node at the front of the list
        new_node = Node(name)

        # If the List is already started, point the new front node to the rest of the list
        if self.head is not None:
            new_node.next = self.head
            
        self.head = new_node

# Add a New End Node
    def add_end(self, name: str) -> None:
        # Insert a new node at the end of the list
        last_node = self.get_last_node()
        if last_node is None:
            return None
        
        new_node = Node(name)
        last_node.next = new_node

# Remove a Specific Node
    def remove(self, name: str) -> None:
        # If the list is empty there is nothing to remove 
        if self.head is None:
            return None
        
        # Special case for removing the head node
        if self.head.name == name:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
            return None
        
        # find the specific node and set the previous node to skip over it
        current = self.head
        prev = self.head
        while current is not None:
            if current.name == name:
                prev.next = current.next
            prev = current
            current = current.next
        return None
        
# Helper method to find the last node in the list
    def get_last_node(self) -> Optional[Node]:
        # Loop
        if self.head is None:
            return None
        
        current = self.head
        while current.next is not None:
           current = current.next
        return current 
    
    def find_node(self, name:str) -> Optional[Node]:
        # Loop
        if self.head is None:
            return None

        current = self.head
        while current is not None:
            if current.name == name:
                return current
            current = current.next
        return None



# Print the Entire List
    def print_list(self) -> None:
        if self.head is None:
            return None
        
        current = self.head
        while current is not None:
            print(current.name)
            current = current.next
