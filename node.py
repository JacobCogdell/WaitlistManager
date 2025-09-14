from typing import Optional

class Node:
# Attributes
    name: str
    next: Optional['Node']
    
# Constructor    
    def __init__(self, name: str):
        self.name = name        # string holding the name of the customer
        self.next = None        # defaults to empty

# Helper Method to Print the Object
    def __ToString__(self):
        return f"Node(name={self.name!r})"
