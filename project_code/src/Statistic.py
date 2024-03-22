import random


class Statistic:
    def __init__(self, legacy_points: int):
        self.value = self._generate_starting_value(legacy_points)
        self.description = None
        self.min_value = 0
        self.max_value = 100

    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random."""
        return legacy_points % 100 + random.randint(1, 3)


class Strength(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

class Dexterity(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Dexterity is a measure of agility and reflexes."


class Constitution(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Constitution is a measure of resilience and endurance."


class Vitality(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Vitality is a measure of overall health and vigor."


class Endurance(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Endurance is a measure of stamina and resistance to fatigue."


class Intelligence(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Intelligence is a measure of cognitive ability and problem-solving skills."


class Wisdom(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Wisdom is a measure of insight, intuition, and judgment."


class Knowledge(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Knowledge is a measure of accumulated information and expertise."


class Willpower(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Willpower is a measure of determination and mental resilience."


class Spirit(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Spirit is a measure of connection to otherworldly energies and metaphysical strength."

