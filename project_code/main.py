# main.py
import sys
import random
from enum import Enum
import pickle

from game_file_manager import load_user_data_from_storage

# Add the function definitions here

def load_user_data_from_storage(filename="user_data.pickle"):
    """Load user data from storage."""
    try:
        with open(filename, "rb") as file:
            user_data = pickle.load(file)
        return user_data
    except FileNotFoundError:
        return None

def save_to_file(data, filename="saved_game_state.pickle"):
    """Save game state data to a file."""
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_from_file(filename="saved_game_state.pickle"):
    """Load game state data from a file."""
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None


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


class EventStatus(Enum):
     UNKNOWN = "unknown"
     PASS = "pass"
     FAIL = "fail"
     PARTIAL = "partial pass"


class Event:
    def __init__(self, parser: EventInputParser):
                self.parser = parser
                self.status = EventStatus.UNKNOWN
                self.fail = {
                    "message": "You failed."
                }
                self.pass_message = {
                    "message": "You passed."
                }
                self.partial_pass = {
                    "message": "You partially passed."
                }
                self.primary: Statistic = Strength() 
                self.secondary: Statistic = Dexterity() 
                 
    def execute(self, party):
        self.parser.select_party_member(party)
        chosen_one = self.parser.select_party_member(party)
        chosen_skill = self.parser.select_skill(chosen_one)
        self.set_status(EventStatus.PASS)
        pass 

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status 
    
    def resolve_choice(self, party, character, chosen_skill):
        event_attributes = [attribute for attribute in dir(self) if not attribute.startswith('__')]
        skill_attributes = [attribute for attribute in dir(chosen_skill) if not attribute.startswith('__')]

        overlapping_attributes = [attr for attr in event_attributes if attr in skill_attributes]

        if len(overlapping_attributes) == 0:
            return "You failed."
        elif len(overlapping_attributes) == len(event_attributes):
            return "You passed."
        else:
            return "You partially passed."
        
event1 = Event(
    name="Gathering Allies",
    requirements="Convince various kingdoms to join forces against the Demon King.",
    success_outcome="The heroes successfully unite all villagers and kingdoms, forming a powerful team.",
    partial_success_outcome="Some kingdoms join the alliance, but others remain skeptical or refuse to cooperate fully.",
    failure_outcome="You fail to convince any kingdoms to join their mission, weakening their chances against the Demon King."
)

event2 = Event(
    name="Obtaining Legendary Weapons",
    requirements="Embark on a perilous journey to find and retrieve legendary weapons rumored to be capable of defeating the Demon King.",
    success_outcome="The heroes locate and acquire powerful artifacts that enhance their abilities and increase their chances of victory.",
    partial_success_outcome="The heroes find some legendary weapons, but not all of them. They must make do with what they have.",
    failure_outcome="The heroes are unable to find any legendary weapons, leaving them ill-prepared for the final battle against the Demon King."
)

event3 = Event(
    name="Infiltrating the Demon King's Fortress",
    requirements="Sneak into the heavily guarded fortress of the Demon King to gather intelligence and weaken his defenses.",
    success_outcome="The heroes successfully infiltrate the fortress, sabotaging key elements of the Demon King's army and gaining valuable information.",
    partial_success_outcome="The heroes manage to enter the fortress but are quickly discovered, forcing them to retreat before completing their mission.",
    failure_outcome="The heroes are captured while attempting to infiltrate the fortress, giving the Demon King the upper hand in the upcoming battle."
)

event4 = Event(
    name="Confrontation with the Demon King",
    requirements="Engage in a climactic battle with the Demon King to decide the fate of the world.",
    success_outcome="Through courage, teamwork, and determination, the heroes emerge victorious, vanquishing the Demon King and saving the world from his tyranny.",
    partial_success_outcome="The heroes put up a valiant fight, but the Demon King proves too powerful to defeat outright. They manage to weaken him, buying time for a temporary retreat.",
    failure_outcome="Despite their best efforts, the heroes are no match for the overwhelming might of the Demon King. They are defeated, and the world falls under his control."
)

game_instance.add_event(event1)
game_instance.add_event(event2)
game_instance.add_event(event3)
game_instance.add_event(event4)

class UserFactory:

    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(parser, username=username, password=password)

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
       game_state = self.sterialize_game_state()
       save_to_file(game_state)  

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
        names = ['Prof', 'Jen', 'Therese', 'Larry', 'Arjun']
        return random.choice(names)

class Location:
    
    def __init__(self, parser, number_of_events: int = 1): 
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]

    def create_custom_event_from_static_text_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        return Event(self.parser, data)


    def _load_user(self) -> User:
        user_data = load_user_data_from_storage()
        if user_data:
            return User(user_data)
        else: 
            return None 

class Game:
    def __init__(self, parser):
        self.parser = parser
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
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
        character_list = [Character() for _ in range(10)]
        location_list = [Location(self.parser) for _ in range(2)]

        for character in character_list:
            self.add_character(character)

        for location in location_list:
            self.add_location(location)

    def start_game(self):
        """Start the game."""
        self._initialize_game()
        return self._main_game_loop() 
    
    
    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
           self.current_location = self.locations[0]
           for event in self.current_location.events:
                self.current_event = event
                self.current_event.execute(self.party)
                if not self.continue_playing: 
                    return True 
                elif self.continue_playing == "Save and quit":
                    return "Save and quit"
        return False
    
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
       game_state = GameFileManager.sterialize_game_state(self.current_game)
       GameFileManager.save_to_file(game_state)  


class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response

class UserFactory:

    def create_user(self, parser: UserInputParser) -> User:
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
        # Implement the logic to load user data from storage and return a User object
        user_data = load_user_data_from_storage()
        if user_data:
            return User(self.parser, username=user_data["username"], password=user_data["password"])
        else:
            return None
    
class GameFileManager:
    @staticmethod
    def save_to_file(data, filename="saved_game_state.pickle"):
        """Save game state data to a file."""
        with open(filename, "wb") as file:
            pickle.dump(data, file)
    @staticmethod
    def load_from_file(filename="saved_game_state.pickle"):
        """Load game state data from a file."""
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
            return data
        except FileNotFoundError:
            return None 
    @staticmethod
    def serialize_game_state(game_state):
        """Serialize the game state data to a format suitable for saving."""
        # You can implement this function based on your game's requirements
        # For example, you can convert the game state object into a dictionary
        # containing all the necessary information to reconstruct the game state.
        serialized_data = {
            "characters": game_state.characters,
            "locations": game_state.locations, 
            "events": game_state.events, 
            "party": game_state.party, 
            "current_location": game_state.current_location
            "current_event": game_state.current_event, 
            "continue_playing": game_state.continue_playing 
           }
        return serialized_data
    @staticmethod
    def deserialize_game_state(serialized_data):
        """Deserialize the serialized game state data."""
        # You can implement this function to convert serialized data back into
        # the game state object, using the appropriate logic to reconstruct
        # the game state from the serialized data.
        characters = serialized_data["characters"]
        locations = serialized_data["locations"]
        events = serialized_data["events"]
        party = serialized_data["party"]
        current_location = serialized_data["current_location"]
        current_event = serialized_data["current_event"]
        continue_playing = serialized_data["continue_playing"]
    
        # Reconstruct the game state object using the extracted information
        game_state = GameState(characters, locations, events, party, current_location, current_event, continue_playing)
        return game_state
    @staticmethod
    def load_user_data_from_storage(filename="user_data.pickle"):
        """Load user data from storage."""
        try:
            with open(filename, "rb") as file:
                user_data = pickle.load(file)
            return user_data
        except FileNotFoundError:
            return None
    @staticmethod
    def save_user_data_to_storage(user_data, filename="user_data.pickle"):
        """Save user data to storage."""
        with open(filename, "wb") as file:
            pickle.dump(user_data, file)


class EventInputParser:
    def __init__(self):
        self.style = "console"

    def select_party_member(self, party):
        return random.choice(party)
    
    def select_skill(self, character):
        skills = ["Swordsmanship", "Archery", "Magic", "Stealth", "Invisibility", "Lockpicking"]
        return random.choice(skills)


def start_game():
    """Entry point for starting the game."""
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
        user_data = load_user_data_from_storage()
        if user_data:
            return User(user_data)
        else: 
            return None 
