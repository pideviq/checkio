import unittest
from incinerator.the_warriors import Warrior, Knight, fight
from incinerator.army_battles import Army, Battle
from incinerator.the_defenders import Defender, Rookie


class TestTheDefenders(unittest.TestCase):
    """Test a solution of The Defenders problem."""

    def test_defender(self) -> None:
        defender = Defender()
        # Check properties
        self.assertEqual(60, defender.health)
        self.assertEqual(3, defender.attack)
        self.assertEqual(2, defender.defense)
        # Check invalid damage
        with self.assertRaises(ValueError):
            defender.take_damage(-2)
        # Check damage > health
        defender.take_damage(defender.health + defender.defense + 1)
        self.assertEqual(0, defender.health)

    def test_fight(self) -> None:
        """Test fight with defender."""
        bob = Defender()
        mike = Knight()
        rog = Warrior()
        lancelot = Defender()

        self.assertFalse(fight(bob, mike))
        self.assertTrue(fight(lancelot, rog))

    def test_battle_with_defenders(self) -> None:
        """Test battle between two armies with defenders in it."""
        my_army = Army()
        my_army.add_units(Defender, 1)

        enemy_army = Army()
        enemy_army.add_units(Warrior, 2)

        army_3 = Army()
        army_3.add_units(Warrior, 1)
        army_3.add_units(Defender, 1)

        army_4 = Army()
        army_4.add_units(Warrior, 2)

        battle = Battle()

        self.assertFalse(battle.fight(my_army, enemy_army))
        self.assertTrue(battle.fight(army_3, army_4))

    def test_battle_with_rookies(self) -> None:
        """Test battle with rookies,
        whose attack is less than defender's defense.
        """
        my_army = Army()
        my_army.add_units(Defender, 1)

        enemy_army = Army()
        enemy_army.add_units(Rookie, 100)

        self.assertTrue(Battle.fight(my_army, enemy_army))

    def test_fight_with_rookie(self) -> None:
        """Test defender's behavior in fight with rookie."""
        defender = Defender()
        initial_health = defender.health
        rookie = Rookie()
        self.assertTrue(fight(defender, rookie))
        self.assertTrue(defender.is_alive)
        self.assertEqual(initial_health, defender.health)
        self.assertFalse(rookie.is_alive)


if __name__ == '__main__':
    unittest.main()
