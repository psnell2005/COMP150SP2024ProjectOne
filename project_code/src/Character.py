from project_code.src.Statistic import *

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


