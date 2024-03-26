import unittest
from unittest.mock import MagicMock
from project_code.src.InstanceCreator import InstanceCreator
from project_code.src.UserFactory import UserFactory
from project_code.src.UserInputParser import UserInputParser
from project_code.src.User import User

class TestInstanceCreator(unittest.TestCase):
    def setUp(self):
        self.mock_user_factory = MagicMock(spec=UserFactory)
        self.mock_parser = MagicMock(spec=UserInputParser)
        self.instance_creator = InstanceCreator(self.mock_user_factory, self.mock_parser)

    def test_get_user_info_yes_creates_new_user(self):
        # Prepare the mock objects
        self.mock_parser.parse.return_value = "new"  # Simulate the response for creating a new user
        mock_user = MagicMock(spec=User)
        self.mock_user_factory.create_user.return_value = mock_user

        # Execute the method under test
        user = self.instance_creator.get_user_info("yes")

        # Verify the results
        self.mock_parser.parse.assert_called_once_with("Create a new username or login to an existing account?")
        self.mock_user_factory.create_user.assert_called_once_with(self.mock_parser)
        self.assertEqual(user, mock_user, "The method should return a new user object")

    def test_get_user_info_no_returns_none(self):
        # Execute the method under test with a response that should not create a user
        user = self.instance_creator.get_user_info("no")

        # Verify the results
        self.assertIsNone(user, "The method should return None for a 'no' response")

    # You can add more tests to cover other scenarios, such as handling login

import unittest
from main import Character, Location, Event, EventInputParser

class TestCharacter(unittest.TestCase):
    def test_character_creation(self):
        character = Character("Test Character")
        self.assertEqual(character.name, "Test Character")

    def test_character_default_stats(self):
        character = Character()
        self.assertEqual(character.strength.value, 0)
        self.assertEqual(character.dexterity.value, 0)
        # Add more assertions for other default stats...

    def test_character_stat_increase(self):
        character = Character()
        character.strength.increase(10)
        self.assertEqual(character.strength.value, 10)

    # Add more test cases for Character class methods..
          
class TestLocation(unittest.TestCase):
    def test_location_creation(self):
        location = Location()
        self.assertIsInstance(location, Location)

    def test_location_event_creation(self):
        parser = EventInputParser()
        location = Location(parser, number_of_events=3)
        self.assertEqual(len(location.events), 3)

    def test_event_creation(self):
        event = Event(
            name="Test Event",
            parser=self.parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        self.assertEqual(event.name, "Test Event")

    def test_event_status_change(self):
        event = Event(
            name="Test Event",
            parser=self.parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        event.set_status(EventStatus.PASS)
        self.assertEqual(event.status, EventStatus.PASS)

    def test_event_execute(self):
        event = Event(
            name="Test Event",
            parser=self.parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        party = ["Character A", "Character B", "Character C"]
        event.execute(party)
        self.assertIn(event.status, [EventStatus.PASS, EventStatus.PARTIAL, EventStatus.FAIL])

    def test_event_resolve_choice_pass(self):
        event = Event(
            name="Test Event",
            parser=self.parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        character = "Character A"
        chosen_skill = "Swordsmanship"
        result = event.resolve_choice([], character, chosen_skill)
        self.assertEqual(result, "You passed.")

    def test_event_resolve_choice_partial_pass(self):
        event = Event(
            name="Test Event",
            parser=self.parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        character = "Character A"
        # Choose a skill that partially overlaps with event attributes
        chosen_skill = "Dexterity"
        result = event.resolve_choice([], character, chosen_skill)
        self.assertEqual(result, "You partially passed.")

    def test_event_resolve_choice_fail(self):
        event = Event(
            name="Test Event",
            parser=self.parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        character = "Character A"
        # Choose a skill that does not overlap with event attributes
        chosen_skill = "Magic"
        result = event.resolve_choice([], character, chosen_skill)
        self.assertEqual(result, "You failed.")

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(None)

    def test_add_character(self):
        character = Character("Test Character")
        self.game.add_character(character)
        self.assertIn(character, self.game.characters)

    def test_add_location(self):
        location = Location(None)
        self.game.add_location(location)
        self.assertIn(location, self.game.locations)

    def test_add_event(self):
        event = Event(
            name="Test Event",
            parser=None,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )
        self.game.add_event(event)
        self.assertIn(event, self.game.events)

    def test_initialize_game(self):
        self.game._initialize_game()
        self.assertGreaterEqual(len(self.game.characters), 1)
        self.assertGreaterEqual(len(self.game.locations), 1)

    def test_start_game(self):
        # Test that the game starts without errors
        result = self.game.start_game()
        self.assertTrue(result)

class TestStatisticClass(unittest.TestCase):
    def test_statistic_initialization(self):
        stat = Statistic(legacy_points=50)
        self.assertEqual(stat.value, 50)

    def test_statistic_increase(self):
        stat = Statistic(legacy_points=50)
        stat.increase(10)
        self.assertEqual(stat.value, 60)

    def test_statistic_decrease(self):
        stat = Statistic(legacy_points=50)
        stat.decrease(20)
        self.assertEqual(stat.value, 30)

class TestCharacterClass(unittest.TestCase):
    def test_character_creation(self):
        char = Character(name="Test Character")
        self.assertEqual(char.name, "Test Character")

    def test_character_initial_stats(self):
        char = Character()
        self.assertTrue(char.strength.value >= 0 and char.strength.value <= 100)
        # Add more assertions for other stats as needed

class TestStartGameFunction(unittest.TestCase):
    def test_start_game(self):
        # You may need to mock certain dependencies for this test
        # For simplicity, we'll just check if it runs without errors
        start_game()


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.mock_parser = MagicMock()
        self.event = Event(
            name="Test Event",
            parser=self.mock_parser,
            requirements="Test Requirements",
            success_outcome="Success",
            partial_success_outcome="Partial Success",
            failure_outcome="Failure"
        )

    def test_event_requirements(self):
        self.assertEqual(self.event.requirements, "Test Requirements")
        self.assertIsInstance(self.event.requirements, str)

    def test_event_outcomes(self):
        self.assertEqual(self.event.success_outcome, "Success")
        self.assertEqual(self.event.partial_success_outcome, "Partial Success")
        self.assertEqual(self.event.failure_outcome, "Failure")
        self.assertIsInstance(self.event.success_outcome, str)
        self.assertIsInstance(self.event.partial_success_outcome, str)
        self.assertIsInstance(self.event.failure_outcome, str)

    def test_event_parser_dependency(self):
        self.assertEqual(self.event.parser, self.mock_parser)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(None)

    def test_party_management(self):
        # Add characters to the game's party
        character1 = Character("Character 1")
        character2 = Character("Character 2")
        self.game.add_character(character1)
        self.game.add_character(character2)
        
        # Verify party size increases
        self.assertEqual(len(self.game.party), 2)

        # Remove a character from the party
        self.game.remove_character(character1)

        # Verify party size decreases
        self.assertEqual(len(self.game.party), 1)
        self.assertNotIn(character1, self.game.party)
        self.assertIn(character2, self.game.party)

    def test_current_location_and_event(self):
        # Create and add a location with events to the game
        location = Location(None)
        event1 = Event(name="Event 1", parser=None, requirements="", success_outcome="", partial_success_outcome="", failure_outcome="")
        event2 = Event(name="Event 2", parser=None, requirements="", success_outcome="", partial_success_outcome="", failure_outcome="")
        location.events.extend([event1, event2])
        self.game.add_location(location)

        # Set current location and event
        self.game.set_current_location(location)
        self.game.set_current_event(event1)

        # Verify current location and event are correctly set
        self.assertEqual(self.game.current_location, location)
        self.assertEqual(self.game.current_event, event1)

if __name__ == '__main__':
    unittest.main()
