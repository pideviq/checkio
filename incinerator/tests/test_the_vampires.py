import unittest
from incinerator.the_warriors import Warrior, fight
from incinerator.army_battles import Army, Battle
from incinerator.the_defenders import Defender, Rookie
from incinerator.the_vampires import Vampire


class TestTheVampires(unittest.TestCase):
    """Test a solution of The Vampires mission."""

    def setUp(self) -> None:
        # Initial Vampire attributes
        self.health: int = 40
        self.attack: int = 4
        self.vampiring: int = 50

    def test_vampire(self) -> None:
        """Test vampire unit type."""
        vampire = Vampire()

        self.assertEqual(self.health, vampire.health)
        self.assertEqual(self.attack, vampire.attack)
        self.assertEqual(self.vampiring, vampire.vampiring)

    def test_vampire_restore_health(self) -> None:
        """Test restoring health after hitting an enemy."""
        with self.subTest(msg='Test default interaction'):
            vampire = Vampire()
            warrior = Warrior()

            vampire.hit(warrior)
            self.assertEqual(self.health, vampire.health)

            warrior.hit(vampire)
            vampire.hit(warrior)
            healing = int(vampire.attack * vampire.vampiring / 100)
            remaining_health = self.health - warrior.attack + healing
            self.assertEqual(remaining_health, vampire.health)

        with self.subTest(msg='Test interaction with Defender'):
            vampire = Vampire()
            defender = Defender()

            defender.hit(vampire)
            vampire.hit(defender)
            healing = int((vampire.attack - defender.defense)
                          * vampire.vampiring / 100)
            remaining_health = self.health - defender.attack + healing
            self.assertEqual(remaining_health, vampire.health)

        with self.subTest(msg='Test interaction with Rookie'):
            vampire = Vampire()
            rookie = Rookie()

            rookie.hit(vampire)
            vampire.hit(rookie)
            # Remaining health with straight count exceeds health limit
            self.assertEqual(self.health, vampire.health)

    def test_fight(self) -> None:
        """Test fight with vampire."""
        eric = Vampire()
        adam = Vampire()
        richard = Defender()
        ogre = Warrior()

        self.assertFalse(fight(eric, richard))
        self.assertTrue(fight(ogre, adam))

    def test_battle(self) -> None:
        """Test battle with vampires in the army."""
        my_army = Army()
        my_army.add_units(Defender, 2)
        my_army.add_units(Vampire, 2)
        my_army.add_units(Warrior, 1)

        enemy_army = Army()
        enemy_army.add_units(Warrior, 2)
        enemy_army.add_units(Defender, 2)
        enemy_army.add_units(Vampire, 3)

        army_3 = Army()
        army_3.add_units(Warrior, 1)
        army_3.add_units(Defender, 4)

        army_4 = Army()
        army_4.add_units(Vampire, 3)
        army_4.add_units(Warrior, 2)

        battle = Battle()

        self.assertFalse(battle.fight(my_army, enemy_army))
        self.assertTrue(battle.fight(army_3, army_4))


if __name__ == '__main__':
    unittest.main()
