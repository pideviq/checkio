"""The Vampires

The flocks of crows circled over the battlefield. Many brave warriors have
fallen in this battle, many have continued to fight.
"If this goes on, we’ll simply kill each other, and there will be no winners -
we’ll all lose." - reflected Sir Ronald, watching a bleak picture in front of
him.
"I have to make an important decision. I know what it’ll cost, but now that’s
the only thing that can save us all..."
A long time ago, when he was often in search of trouble and adventure, he went
to hunt a witch who had a huge bounty on her head. The bloody creature was able
to save her life by persuading the knight to take a gift from her - a vial of
vampire blood. This blood poured into the dying man’s mouth could bring him
back to life in vampire form.
Is it really the day when he has to use it?..
It seemed to be the only way to win this battle.
Sir Ronald began to lean over the barely living bodies of his knights, who were
lying beside him. To each of them he said:
- "Drink. You’ll be given a new life..."

So we have 3 types of units: the Warrior, Knight and Defender. Let's make the
battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional
vampiring parameter, which helps him to heal himself. When the Vampire hits the
other unit, he restores his health by +50% of the dealt damage (enemy defense
makes the dealt damage value lower).
The basic parameters of the Vampire:
health = 40
attack = 4
vampiring = 50%
You should store vampiring attribute as an integer (50 for 50%). It will be
needed to make this solution evolute's to fit one of the next challenges of
this saga.

Input: The warriors and armies.
Output: The result of the battle (True or False).
How it is used: For the computer games development.
Precondition: 4 types of units.
"""


from .the_warriors import Warrior


class Vampire(Warrior):
    """Vampire representation."""

    def __init__(self):
        super().__init__()
        self.health: int = 40
        self.__health_limit: int = self.health
        self.attack: int = 4
        self.vampiring: int = 50

    def hit(self, enemy: 'Warrior') -> None:
        """Hit an enemy (make him take damage)."""
        super().hit(enemy)
        self.restore_health(enemy)

    def restore_health(self, enemy: 'Warrior') -> None:
        """Restore health after hitting an enemy."""
        healing = int(self.get_real_damage(enemy) * self.vampiring / 100)
        restored_health = self.health + healing
        self.health = min(restored_health, self.__health_limit)

    def get_real_damage(self, enemy: 'Warrior') -> int:
        """Return real damage for an enemy."""
        defense = enemy.defense if hasattr(enemy, 'defense') else 0
        return max(self.attack - defense, 0)
