"""
...Sir Ronald’s opponent - Umbert, has proved to be a very skillful warrior. In
addition, he was a good fifteen years younger, which gave him a certain
advantage. But Sir Ronald was also very strong - he had the experience of
participation in many battles and in several major wars behind his back. And
besides that, in his youth he was known as the best duelist in this land.
Realizing that the forces are equal, each of them had followed the only course
possible - to call for help. Umbert sent for the reinforcement his coachman on
a horse, and Sir Ronald used a family horn that sounded more than once in hot
battles. The knight's castle was close enough for the call to arms was heard
back there. Nobody quite knew where the Umbert's accomplices were located, and
this made it difficult to come up with a strategy for the battle ahead.
Fortunately, the reinforcements for both sides arrived almost simultaneously.
Now it was more than a question of the girl's honor. There was no peaceful
solutions to this matter. One of the two armies must be destroyed.

In the previous mission - Warriors - you've learned how to make a duel between
2 warriors happen. Great job! But let's move to something that feels a little
more epic - the armies! In this mission your task is to add new classes and
functions to the existing ones. The new class should be the Army and have the
method add_units() - for adding the chosen amount of units to the army. The
first unit added will be the first to go to fight, the second will be the
second,...
Also you need to create a Battle() class with a fight() function, which will
determine the strongest army. The battles occur according to the following
principles:
at first, there is a duel between the first warrior of the first army and the
first warrior of the second army. As soon as one of them dies - the next
warrior from the army that lost the fighter enters the duel, and the surviving
warrior continues to fight with his current health. This continues until all
the soldiers of one of the armies die. In this case, the fight() function
should return True, if the first army won, or False, if the second one was
stronger.
Note that army 1 have the advantage to start every fight!

Input: The warriors and armies.
Output: The result of the battle (True or False).
How it is used: For computer games development.

Precondition:
- 2 types of units;
- for all battles, each army is obviously not empty at the beginning.
"""


from collections import deque
from typing import Type
from .the_warriors import Warrior, fight


class Army:
    """Representation of an army of different types of warriors."""

    def __init__(self):
        self.units = deque()

    def __len__(self):
        return len(self.units)

    def add_units(self, units_type: Type[Warrior],
                  number_of_units: int) -> None:
        """Add chosen number of units to the tail of the army."""
        for _ in range(number_of_units):
            conscript = units_type.__call__()
            self.units.append(conscript)

    def get_fighter(self):
        """Return next fighter (FIFO)."""
        return self.units.popleft()


class Battle:
    """Epic battle between two armies."""

    @staticmethod
    def fight(army_1: 'Army', army_2: 'Army') -> bool:
        """Return the result of a battle for army_1.
        (True if won, False otherwise)

        Arguments:
            army_1 - the first Army
            army_2 - the second Army
        """
        if not (army_1 and army_2):
            raise ValueError('bring your troops and fight like a man!')

        unit_1 = army_1.get_fighter()
        unit_2 = army_2.get_fighter()
        while unit_1 and unit_2:
            unit_1_won = fight(unit_1, unit_2)
            try:
                if unit_1_won:
                    unit_2 = army_2.get_fighter()
                else:
                    unit_1 = army_1.get_fighter()
            except IndexError:
                # The battle is over
                break
        return not unit_2
