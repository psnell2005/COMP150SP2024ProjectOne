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
        # etc
        # self.intelligence: Intelligence = Intelligence(self)

    def _generate_name(self):
        return "Bob"

character1 = Character(name="Miller")
character1.strength.value = 70
character1.dexterity.value = 10
character1.constitution.value = 10
character1.vitality.value = 40
character1.endurance.value = 30
character1.intelligence.value = 50
character1.wisdom.value = 80
character1.knowledge.value = 75
character1.willpower.value = 50
character1.spirit.value = 40

character2 = Character(name="James")
character2.strength.value = 65 
character2.dexterity.value = 30 
character2.constitution.value = 50 
character2.vitality.value = 60 
character2.endurance.value = 50 
character2.intelligence.value = 60 
character2.wisdom.value = 60 
character2.knowledge.value = 77 
character2.willpower.value = 40 
character2.spirit.value = 20 

character3 = Character(name="Jen")
character3.strength.value = 55 
character3.dexterity.value = 50 
character3.constitution.value = 90
character3.vitality.value = 90 
character3.endurance.value = 80 
character3.intelligence.value = 80 
character3.wisdom.value = 30 
character3.knowledge.value = 60 
character3.willpower.value = 80 
character3.spirit.value = 60 

character4 = Character(name="Phoebe")
character4.strength.value = 55
character4.dexterity.value = 45
character4.constitution.value = 85
character4.vitality.value = 90 
character4.endurance.value = 75 
character4.intelligence.value = 80 
character4.wisdom.value = 30 
character4.knowledge.value = 59 
character4.willpower.value = 80 
character4.spirit.value = 61 

character5 = Character(name="Therese")
character5.strength.value = 75 
character5.dexterity.value = 60 
character5.constitution.value = 90 
character5.vitality.value = 90 
character5.endurance.value = 85
character5.intelligence.value = 80 
character5.wisdom.value = 30 
character5.knowledge.value = 60 
character5.willpower.value = 85 
character5.spirit.value = 50 

character6 = Character(name="Larry")
character6.strength.value = 80 
character6.dexterity.value = 15
character6.constitution.value = 75
character6.vitality.value = 40 
character6.endurance.value = 60 
character6.intelligence.value = 90
character6.wisdom.value = 33
character6.knowledge.value = 80 
character6.willpower.value = 50 
character6.spirit.value = 30 

character7 = Character(name="Gabe")
character7.strength.value = 34 
character7.dexterity.value = 90 
character7.constitution.value = 50 
character7.vitality.value = 85
character7.endurance.value = 40 
character7.intelligence.value = 45 
character7.wisdom.value = 31 
character7.knowledge.value = 40 
character7.willpower.value = 20 
character7.spirit.value = 49 

character8 = Character(name="Trinity")
character8.strength.value = 45 
character8.dexterity.value = 79 
character8.constitution.value = 75 
character8.vitality.value = 80 
character8.endurance.value = 80 
character8.intelligence.value = 85 
character8.wisdom.value = 30 
character8.knowledge.value = 50 
character8.willpower.value = 50 
character8.spirit.value = 11 

character9 = Character(name="Johnathan")
character9.strength.value = 35 
character9.dexterity.value = 60 
character9.constitution.value = 80 
character9.vitality.value = 75 
character9.endurance.value = 80 
character9.intelligence.value = 40 
character9.wisdom.value = 33
character9.knowledge.value = 38 
character9.willpower.value = 70
character9.spirit.value = 96 

character10 = Character(name="Arjun")
character10.strength.value = 60 
character10.dexterity.value = 80 
character10.constitution.value = 89 
character10.vitality.value = 79 
character10.endurance.value = 85 
character10.intelligence.value = 88 
character10.wisdom.value = 32 
character10.knowledge.value = 65 
character10.willpower.value = 89 
character10.spirit.value = 60 

character11 = Character(name="Milosz")
character11.strength.value = 45 
character11.dexterity.value = 50 
character11.constitution.value = 55 
character11.vitality.value = 64 
character11.endurance.value = 60 
character11.intelligence.value = 50 
character11.wisdom.value = 36 
character11.knowledge.value = 40 
character11.willpower.value = 25 
character11.spirit.value = 30

character12 = Character(name="Hookah")
character12.strength.value = 40 
character12.dexterity.value = 50 
character12.constitution.value = 40 
character12.vitality.value = 70 
character12.endurance.value = 10 
character12.intelligence.value = 30 
character12.wisdom.value = 33
character12.knowledge.value = 30 
character12.willpower.value = 10 
character12.spirit.value = 10 

character13 = Character(name="Sherron")
character13.strength.value = 39 
character13.dexterity.value = 90
character13.constitution.value = 80 
character13.vitality.value = 75 
character13.endurance.value = 50 
character13.intelligence.value = 60 
character13.wisdom.value = 36 
character13.knowledge.value = 39 
character13.willpower.value = 30 
character13.spirit.value = 25 

character14 = Character(name="Abdullah")
character14.strength.value = 40 
character14.dexterity.value = 85 
character14.constitution.value = 80 
character14.vitality.value = 80 
character14.endurance.value = 30 
character14.intelligence.value = 65 
character14.wisdom.value = 31 
character14.knowledge.value = 55
character14.willpower.value = 50 
character14.spirit.value = 40 

character15 = Character(name="Abdul")
character15.strength.value = 40 
character15.dexterity.value = 80 
character15.constitution.value = 70 
character15.vitality.value = 78 
character15.endurance.value = 50 
character15.intelligence.value = 55
character15.wisdom.value = 32 
character15.knowledge.value = 40 
character15.willpower.value = 60 
character15.spirit.value = 40 

character16 = Character(name="Alex C.")
character16.strength.value = 38 
character16.dexterity.value = 60 
character16.constitution.value = 70 
character16.vitality.value = 77 
character16.endurance.value = 83 
character16.intelligence.value = 55 
character16.wisdom.value = 32 
character16.knowledge.value = 40 
character16.willpower.value = 70 
character16.spirit.value = 20 

character17 = Character(name="Adriana") 
character17.strength.value = 35 
character17.dexterity = 80 
character17.constitution.value = 70 
character17.vitality.value = 79 
character17.endurance.value = 20 
character17.intelligence.value = 40 
character17.wisdom.value = 31 
character17.knowledge.value = 30 
character17.willpower.value = 10 
character17.spirit.value = 10 

character18 = Character(name="Alex P.")
character18.strength.value = 36 
character18.dexterity.value = 76 
character18.constitution.value = 60 
character18.vitality.value = 76 
character18.endurance.value = 30 
character18.intelligence.value = 40 
character18.wisdom.value = 31 
character18.knowledge.value = 30 
character18.willpower.value = 20 
character18.spirit.value = 10 

character19 = Character(name="Jay")
character19.strength.value = 37 
character19.dexterity.value = 90 
character19.constitution.value = 60 
character19.vitality.value = 77 
character19.endurance.value = 17
character19.intelligence.value = 40 
character19.wisdom.value = 33 
character19.knowledge.value = 40 
character19.willpower.value = 10 
character19.spirit.value = 10 

character20 = Character(name="Luke")
character20.strength.value = 38 
character20.dexterity.value = 79 
character20.constitution.value = 60 
character20.vitality.value = 76 
character20.endurance.value = 30 
character20.intelligence.value = 40 
character20.wisdom.value = 31 
character20.knowledge.value = 40 
character20.willpower.value = 23 
character20.spirit.value = 10 

