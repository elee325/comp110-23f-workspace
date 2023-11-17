<<<<<<< HEAD
"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self):
        return None
    
    def tail(self):
        return None
    
    def last(self):
        return None
=======
"""Node class for a linked list."""

from __future__ import annotations

class Node:
    
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a node."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            # base case
            return str(self.data)
        else:
            # recursive step
            return str(self.data) + "->" + str(self.next)
>>>>>>> 0578a44 (class practice)
