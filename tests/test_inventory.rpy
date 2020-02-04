init python:
    import unittest
    
    class TestInventory(unittest.TestCase):
        def test_container_init(self):
            bag = Container(max_size=1, max_volume=1, max_weight=1, spiece='bags', info='', image='bag.png')
            lefts_ok = bag.left_volume == bag.max_volume and bag.left_weight == bag.max_weight
            self.assertTrue(lefts_ok)

        def test_container_add_status_ok(self):
            bag = Container(max_size=1, max_volume=5, max_weight=10, spiece='bags', info='', image='bag.png')
            item = Item(name='arrow', quantity=2, volume=1, size=1, weight=1, spiece='ammo', info='', price=10, craft='', thumb='', image='', value='')
            status = bag.add(item)
            if not status[0]:
                print (added, ",", msg)
            self.assertEqual(status, (True, "ok"))

        def test_container_add_bad_size(self):
            bag = Container(max_size=0, max_volume=5, max_weight=10, spiece='bags', info='', image='bag.png')
            item = Item(name='arrow', quantity=2, volume=1, size=1, weight=1, spiece='ammo', info='', price=10, craft='', thumb='', image='', value='')
            status = bag.add(item)
            self.assertEqual(status, (False, "This will not fit"))

        def test_container_add_bad_volume(self):
            bag = Container(max_size=1, max_volume=1, max_weight=10, spiece='bags', info='', image='bag.png')
            item = Item(name='arrow', quantity=2, volume=1, size=1, weight=1, spiece='ammo', info='', price=10, craft='', thumb='', image='', value='')
            status = bag.add(item)
            self.assertEqual(status, (False, "This is too big"))

        def test_container_add_bad_weight(self):
            bag = Container(max_size=1, max_volume=5, max_weight=1, spiece='bags', info='', image='bag.png')
            item = Item(name='arrow', quantity=2, volume=1, size=1, weight=1, spiece='ammo', info='', price=10, craft='', thumb='', image='', value='')
            status = bag.add(item)
            self.assertEqual(status, (False, "This is too heavy"))
            
        def test_container_remove(self):
            bag = Container(max_size=1, max_volume=5, max_weight=10, spiece='bags', info='', image='bag.png')
            item = Item(name='arrow', quantity=1, volume=1, size=1, weight=1, spiece='ammo', info='', price=10, craft='', thumb='', image='', value='')
            bag.add(item)
            bag.remove(item)
            self.assertEqual(len(bag), 0)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestInventory)
    unittest.TextTestRunner().run(suite)    
