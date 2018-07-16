# Items can be added to bag, and assigned to a child.
# Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
# Must be able to list all children who are getting a toy.
# Must be able to list all toys for a given child's name.
# Must be able to set the delivered property of a child, which defaults to false to true.

import sys
import unittest
from lootbag import Bag

class TestLootbag(unittest.TestCase):

    def test_add(self):

        new_bag = Bag()
        new_bag.add_child_toy("kite", "suzy")

        self.assertDictEqual(new_bag.directory, {"suzy" : ["kite"]})
        self.assertEqual(new_bag.directory["suzy"], ['kite'])

        new_bag.add_child_toy("money", "suzy")

        self.assertDictEqual(new_bag.directory, {"suzy" : ["kite", "money"]})
        self.assertEqual(new_bag.directory["suzy"], ['kite', 'money'])

    def test_removing_items(self):

        new_bag = Bag()
        new_bag.add_child_toy("kite", "suzy")
        new_bag.add_child_toy("money", "suzy")
        new_bag.remove_child_toy("kite", "suzy")

        self.assertEqual(new_bag.directory, {'suzy' : ['money']})
        self.assertEqual(new_bag.remove_child_toy('shoe', 'suzy'), "This child doesn't have that toy to begin with.")
        self.assertEqual(new_bag.remove_child_toy('shoe', 'kristen'), "We dont have any toys for this child!")

    def test_children_with_impending_gifts(self):

        bag = Bag()
        bag.add_child_toy("kite", "suzy")
        bag.add_child_toy("kite", "bob")
        bag.add_child_toy("kite", "joseph")
        bag.add_child_toy("kite", "mary")

        children = bag.kids_to_get_toys()

        self.assertEqual(children, ["suzy", "bob", "joseph", "mary"])

    def test_child_is_getting(self):

        bag = Bag()
        bag.add_child_toy("kite", "suzy")
        bag.add_child_toy("mop", "suzy")
        bag.add_child_toy("jumprope", "suzy")

        self.assertEqual(bag.child_is_getting("suzy"), ["kite", "mop", "jumprope"])
        self.assertEqual(bag.child_is_getting("joe"), "joe has no toys in this bag.")





if __name__ == '__main__':
    unittest.main()        