import unittest
from incinerator.the_warriors import Warrior, Knight
from incinerator.army_battles import Army, Battle


class TestArmyBattles(unittest.TestCase):
    """Test a solution of Army Battles problem."""

    def test_army(self):
        """Test creation of an army."""
        my_army = Army()
        self.assertFalse(my_army)

        reinforcement = {
            'type': Knight,
            'total': 3,
        }
        my_army.add_units(reinforcement['type'], reinforcement['total'])
        self.assertTrue(my_army)
        self.assertEqual(reinforcement['total'], len(my_army))

        new_reinforcement = {
            'type': Warrior,
            'total': 10,
        }
        my_army.add_units(new_reinforcement['type'],
                          new_reinforcement['total'])
        self.assertEqual(reinforcement['total'] + new_reinforcement['total'],
                         len(my_army))

    def test_army_of_one(self):
        """Test an army with a single warrior."""
        my_army = Army()
        my_army.add_units(Knight, 1)

        enemy = Army()
        enemy.add_units(Warrior, 1)

        battle = Battle()
        self.assertTrue(battle.fight(my_army, enemy))

    def test_empty_armies(self):
        """Test empty armies (go beyond the task)."""
        my_army = Army()
        enemy = Army()

        battle = Battle()
        with self.assertRaises(ValueError):
            battle.fight(my_army, enemy)

    def test_battle(self):
        """Test battle between two armies."""
        my_army = Army()
        my_army.add_units(Knight, 3)

        enemy_army = Army()
        enemy_army.add_units(Warrior, 3)

        army_3 = Army()
        army_3.add_units(Warrior, 20)
        army_3.add_units(Knight, 5)

        army_4 = Army()
        army_4.add_units(Warrior, 30)

        battle = Battle()

        self.assertTrue(battle.fight(my_army, enemy_army))
        self.assertFalse(battle.fight(army_3, army_4))


if __name__ == '__main__':
    unittest.main()
