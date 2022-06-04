import unittest
from incinerator.the_warriors import Warrior, Knight, fight


class TestTheWarriors(unittest.TestCase):
    """Test a solution of The Warriors mission."""

    def test_warrior_init(self):
        """Test initial indicators of a Warrior."""
        warrior = Warrior()
        self.assertEqual(50, warrior.health)
        self.assertEqual(5, warrior.attack)
        self.assertTrue(warrior.is_alive)
        self.assertTrue(warrior)

    def test_knight_init(self):
        """Test initial indicators of a Knight."""
        knight = Knight()
        self.assertEqual(50, knight.health)
        self.assertEqual(7, knight.attack)
        self.assertTrue(knight.is_alive)
        self.assertTrue(knight)

    def test_take_damage(self):
        """Test take_damage implementation."""
        warrior = Warrior()
        with self.assertRaises(ValueError):
            warrior.take_damage(-2)
        damage = 5
        health_after_damage = warrior.health - damage
        warrior.take_damage(damage)
        self.assertEqual(health_after_damage, warrior.health)

    def test_fight(self):
        """Test the duel result."""
        chuck = Warrior()
        bruce = Warrior()
        self.assertTrue(fight(chuck, bruce))
        self.assertTrue(chuck.is_alive)
        self.assertTrue(chuck)
        self.assertFalse(bruce.is_alive)
        self.assertFalse(bruce)

        carl = Knight()
        dave = Warrior()
        self.assertFalse(fight(dave, carl))
        self.assertTrue(carl.is_alive)
        self.assertFalse(dave.is_alive)

        mark = Warrior()
        self.assertFalse(fight(carl, mark))

    def test_fight_with_dead_warrior(self):
        """Try to fight with already dead warrior."""
        carl = Knight()
        dave = Warrior()
        fight(dave, carl)
        # dave was killed in a fight
        mark = Warrior()
        self.assertFalse(fight(dave, mark))
        self.assertEqual(dave.health, 0)


if __name__ == '__main__':
    unittest.main()
