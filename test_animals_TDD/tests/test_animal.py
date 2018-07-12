import unittest
import sys
sys.path.append('../')
from animal import Animal
from dog import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")
        self.furry = Animal()

    # @classmethod
    # def tearDownClass(self):

    def test_animal_creation(self):

        self.assertIsInstance(self.furry, Animal)
        self.assertIsInstance(self.bob, Dog)
        self.assertIsInstance(self.bob, Animal)

    def test_animal_can_set_legs(self):

        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_species_for_dog(self):

        self.assertEqual(self.bob.species, "Dog")

    def test_species_for_animal(self):

        new_fluff = Animal(None, "Kitty")

        self.assertEqual(self.furry.species, None)
        self.assertEqual(new_fluff.species, "Kitty")
    
    def test_initial_speed(self):

        self.assertEqual(self.bob.speed, 0)
        self.assertEqual(self.furry.speed, 0)

    def test_naming_for_dog(self):

        # test_dog = Dog()
        # self.assertEqual(self.test_dog, None)

        self.assertEqual(self.furry.name, None)
        self.assertEqual(self.bob.name, "Bob")

    def test_set_and_get_species_dog(self):

        bobby = Dog("Bobby")
        bobby.set_species("Woofer")

        self.assertEqual(bobby.get_species(), "Woofer")
        self.assertEqual(self.bob.get_species(), "Dog")
        self.assertEqual(bobby.species, "Woofer")

    def test_dog_walking(self):

        bobby = Dog("Bobby")
        bobby.set_legs(6)
        self.assertEqual(bobby.speed, 0)
        bobby.walk()
        self.assertEqual(bobby.speed, 1.2)



if __name__ == '__main__':
    unittest.main()