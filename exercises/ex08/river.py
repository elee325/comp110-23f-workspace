"""File to define River class."""

__author__: str = "730468571"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Represents the river where bears and fish populate."""    
    # tells you what day of the river's lifecycle
    day: int
    # stores river's bear population
    bears: list[Bear]
    # stores river's fish population
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages of animals then remove if too high."""
        surviving_bears: list[Bear] = [bear for bear in self.bears if bear.age <= 5]
        surviving_fish: list[Fish] = [fish for fish in self.fish if fish.age <= 3]
        
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None

    def remove_fish(self, amount: int):
        """Remove frontmost fish based off amount given."""
        for num in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Bears eat if fish pop greater than 5, eat 3 fish and gain 3 hunger score."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Remove bear if hunger score less than 0."""
        surviving_bears: list[Bear] = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """For every pair of fish, produce four offspring."""
        pairs: int = len(self.fish) // 2
        for pair in range(0, (pairs * 4)):
            new_fish = Fish()
            self.fish.append(new_fish)
            
        return None
    
    def repopulate_bears(self):
        """For every pair of bears, add one offspring."""
        pairs: int = len(self.bears) // 2
        for pair in range(0, pairs):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """Prints status of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Shows status of river over one week."""
        for num in range(0, 7):
            self.one_river_day()
        return None
            
