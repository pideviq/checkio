"""
One day, on a typical spring afternoon, Sir Ronald has been looking around his
land, riding a horse. Nothing foretold troubles, when suddenly Sir Ronald heard
a scream for help, coming from somewhere nearby:
- "Help! Help!" - shouted a piercing young girl's voice.
As a true knight, Sir Ronald couldn't stay away and went to the lady's rescue.
Rushing in the direction from which the cry came, he saw a carriage. The girl
peered out the window hoping to see someone who could help her.
- "Stop!"- ordered Sir Ronald to the coachman. - "By what right are you on my
land?"
The coachman didn't get a chance to open his mouth, as his master came out of
the carriage.
- "My respects, noble sir. I had no idea that this land is yours. My bride and
I were just going to my estate, not wanting to give anyone any trouble."
- "A flat-out lie! I'm not his bride!" - the girl exclaimed from the window.
- "Explain yourself, Sir. What does that mean?",- said Sir Ronald.
- "Of course. The king of a neighboring country has promised his daughter and
half his kingdom to the one who'll save her from the outlaws who took her. I've
defeated those bastards, and now I'm taking the princess to her father."
- "It's not true! They were in on it together. They've kidnapped me on his
order! I saw how he paid them a bag of gold!" - The princess didn't stop taking
for a second, trying to quickly describe the situation to the miraculously
appeared savior.
- "Such behavior is unworthy of a knight! Prepare to die!",- exclaimed Sir
Ronald, drawing his sword.
- "Ha-ha-ha, simple-hearted nobleman! We'll see about that..."

I'm sure that many of you have some experience with computer games. But have
you ever wanted to change the game so that the characters or a game world would
be more consistent with your idea of the perfect game? Probably, yes.
In this mission (and in several subsequent ones, related to it) you'll have
a chance "to sit in the developer's chair" and create the logic of a simple
game about battles.
Let's start with the simple task - one-on-one duel. You need to create the
class Warrior, the instances of which will have 2 parameters - health (equal
to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which
can be True (if warrior's health is > 0) or False (in the other case). In
addition, you have to create the second unit type - Knight, which should be the
subclass of the Warrior but have the increased attack - 7. Also, you have to
create a function fight(), which will initiate the duel between 2 warriors and
define the strongest of them. The duel occurs according to the following
principle:
Every turn, the first warrior will hit the second and this second will lose his
health in the same value as the attack of the first warrior. After that, if he
is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still
alive (and thus the other one is not anymore), the function should return True,
False otherwise.
"""


class Warrior:
    """Warrior representation."""

    def __init__(self):
        self.health: int = 50
        self.attack: int = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int):
        """Take damage from hit (decreases health)."""
        if damage < 0:
            raise ValueError('damage must be greater than or equal to zero')
        self.health -= damage
        if self.health < 0:
            # Warrior can't be more dead than dead
            self.health = 0

    def hit(self, enemy: 'Warrior'):
        """Hit an enemy (make him take damage)."""
        enemy.take_damage(self.attack)


class Knight(Warrior):
    """Knight representation."""

    def __init__(self):
        super().__init__()
        self.attack: int = 7


def fight(unit_1: 'Warrior', unit_2: 'Warrior'):
    """Initiate the duel between two units and define the strongest."""
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.hit(unit_2)
        if unit_2.is_alive:
            unit_2.hit(unit_1)
    return unit_1.is_alive
