"""File to define Bear class."""


class Bear:
    """Represents bear in river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """For every day, adds 1 to bear's age and subtract 1 from hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """For every fish eaten, adds to hunger_score."""
        self.hunger_score += num_fish
        return None