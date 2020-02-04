init python:
    import unittest
    
    class TestInventory(unittest.TestCase):
        def test_container_init(self):
            bag = Container(max_size=1, max_volume=1, max_weight=1, spiece='bags', info='', image='bag.png')
            lefts_ok = bag.left_volume == bag.max_volume and bag.left_weight == bag.max_weight
            self.assertTrue(lefts_ok)

        def test_container_add(self):
            bag = Container(max_size=1, max_volume=5, max_weight=10, spiece='bags', info='', image='bag.png')
            item = Item(name='arrow', quantity=2, volume=1, size=1, weight=1, spiece='ammo', info='', price=10, craft='', thumb='', image='', value='')
            added, msg = bag.add(item)
            if not added:
                print (added, ",", msg)
            self.assertTrue(added)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestInventory)
    unittest.TextTestRunner().run(suite)    
