init python:
    import unittest
    
    class TestWeather(unittest.TestCase):
        def test_temp_diff_morning_noon(self):
            calendar = Weather(2020, 1, 20, 9, 0, 0, 1)
            temp1 = int(calendar.temp)
            calendar.add(hours=3)
            temp2 = int(calendar.temp)
            self.assertEqual(temp2-temp1, 6)


    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestWeather)
    unittest.TextTestRunner().run(suite)    
