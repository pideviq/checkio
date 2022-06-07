"""The Defenders

...the clashes between different soldiers occurred here and there, and the new
troops kept coming. The conflict gradually was starting to look more like
a small war.
"Knights, hear my command! Take your shields! Strengthen the armor! We are
taking too much beating", - Sir Ronald shouted.
Nobody’s expected that Umbert's soldiers could compete with the well-trained
knights, so at the beginning of the battle the knights used exclusively
two-handed swords - no one even thought of being on the defensive. But it seems
that it's time to back down and take one-handed swords and shields instead of
the former deadly weapons. This will slightly reduce the assault capacity of
knights, but will allow them to better defend themselves against the dangerous
attacks of enemy soldiers.
In the previous mission - Army battles, you've learned how to make a battle
between 2 armies. But we have only 2 types of units - the Warriors and Knights.
Let's add another one - the Defender. It should be the subclass of the Warrior
class and have an additional defense parameter, which helps him to survive
longer. When another unit hits the defender, he loses a certain amount of his
health according to the next formula: enemy attack - self-defense (if enemy
attack > self-defense). Otherwise, the defender doesn't lose his health.
The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

Input: The warriors and armies.
Output: The result of the battle (True or False).
How it is used: For the computer games development.
Note: From now on, the tests from "check" part will use another type of
warrior: the rookie.
Precondition: 3 types of units
"""


from .the_warriors import Warrior


class Defender(Warrior):
    """Defender representation."""

    def __init__(self):
        super().__init__()
        self.health: int = 60
        self.attack: int = 3
        self.defense: int = 2

    def take_damage(self, damage: int):
        """Take damage from hit (decreases health)."""
        if damage < 0:
            raise ValueError('damage must be greater than or equal to zero')
        real_damage = damage - self.defense if damage > self.defense else 0
        self.health -= real_damage
        if self.health < 0:
            # Warrior can't be more dead than dead
            self.health = 0


class Rookie(Warrior):
    """Rookie representation."""

    def __init__(self):
        super().__init__()
        self.attack: int = 1
