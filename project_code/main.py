# main.py
import sys
from project_code.src.UserInputParser import UserInputParser
from project_code.src.InstanceCreator import InstanceCreator
from project_code.src.UserFactory import UserFactory

def start_game():
    parser = UserInputParser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)

    response = parser.parse("Would you like to start a new game? (yes/no)")
    print(f"Response: {response}")
    user = instance_creator.get_user_info(response)
    if user is not None:
        game_instance = user.current_game
        if game_instance is not None:
            response = game_instance.start_game()
            if response == "Save and quit":
                user.save_game()
                print("Game saved. Goodbye!")
                sys.exit()
            elif response:
                print("Goodbye!")
                sys.exit()
    else:
        print("See you next time!")
        sys.exit()

if __name__ == '__main__':
    start_game()

class Character:

    def __init__(self, name: str = None):
        """
        Core Stats: Everyone has these
        - Strength: How much you can lift. How strong you are. How hard you punch, etc.
        - Dexterity: How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed.
        - Constitution: The bodies natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities
        - vitality: A measure of how lively you feel. How many Hit Points you have. An indirect measure of age.
        - Endurance: How fast you recover from injuries. How quickly you recover from fatigue.
        - Intelligence: How smart you are. How quickly you can connect the dots to solve problems. How fast you can think.
        - Wisdom: How effectively you can make choices under pressure. Generally low in younger people.
        - Knowledge: How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas.
        - Willpower: How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control.
        - Spirit: Catchall for ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills.
         """
        self.name = self._generate_name() if name is None else name
        self.strength: Strength = Strength(self)
        self.dexterity: Dexterity = Dexterity(self)
        self.constitution: Constitution = Constitution(self)
        self.vitality: Vitality = Vitality(self)
        self.endurance: Endurance = Endurance(self)
        self.intelligence: Intelligence = Intelligence(self)
        self.wisdom: Wisdom = Wisdom(self)
        self.knowledge: Knowledge = Knowledge(self)
        self.willpower: Willpower = Willpower(self)
        self.spirit: Spirit = Spirit(self)
        
    def _generate_name(self):
        return "Bob"

character1 = Character(name="Miller")


character2 = Character(name="James")


character3 = Character(name="Jen")
 

character4 = Character(name="Phoebe")


character5 = Character(name="Therese")


character6 = Character(name="Larry")


character7 = Character(name="Gabe")


character8 = Character(name="Trinity")


character9 = Character(name="Johnathan")


character10 = Character(name="Arjun")


character11 = Character(name="Milosz")


character12 = Character(name="Hookah")


character13 = Character(name="Sherron")


character14 = Character(name="Abdullah")
 

character15 = Character(name="Abdul")


character16 = Character(name="Alex C.")


character17 = Character(name="Adriana") 


character18 = Character(name="Alex P.")


character19 = Character(name="Jay")


character20 = Character(name="Luke")


class Event:
    def __init__(self, name, requirements, success_outcome, partial_success_outcome, failure_outcome):
        self.name = name
        self.requirements = requirements
        self.success_outcome = success_outcome
        self.partial_success_outcome = partial_success_outcome
        self.failure_outcome = failure_outcome

class Game:
    def __init__(self, parser):
        self.parser = parser
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True
        

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        pass

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            response = self.input.parse("What would you like to do?")
            if response:
                self.continue_playing = False 
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if part is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False
        
class UserFactory:

    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(parser, username=username, password=password)

        
class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
                return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        pass

class Location:
    pass

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

class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.parser = parser 
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
        pass


class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response
