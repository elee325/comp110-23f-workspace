"""File to define Fish class."""


class Fish:
    """Represents fish in river."""
    age: int

    def __init__(self):
        """Constructor."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Adds one to age every day."""
        self.age += 1
        return None