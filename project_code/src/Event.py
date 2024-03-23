class Event:
    def __init__(self, name, requirements, success_outcome, partial_success_outcome, failure_outcome):
        self.name = name
        self.requirements = requirements
        self.success_outcome = success_outcome
        self.partial_success_outcome = partial_success_outcome
        self.failure_outcome = failure_outcome


event1 = Event(
    name="Gathering Allies",
    requirements="Convince various kingdoms to join forces against the Demon King.",
    success_outcome="The heroes successfully unite all villagers and kingdoms, forming a powerful team.",
    partial_success_outcome="Some kingdoms join the alliance, but others remain skeptical or refuse to cooperate fully.",
    failure_outcome="You fail to convince any kingodms to join their mission, weakening their chances against the Demon King."
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

