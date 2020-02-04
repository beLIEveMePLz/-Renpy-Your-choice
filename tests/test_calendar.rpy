init python:
    #print (sys.version)    
    import unittest
    
    class TestClock(unittest.TestCase):
        def test_nm_01(self):
            clk = Clock(2020, 1, 20, 9, 0, 0, 1)
            self.assertEqual(clk.nm, 'Jan')
    
        def test_nm_12(self):
            clk = Clock(2020, 12, 20, 9, 0, 0, 1)
            self.assertEqual(clk.nm, 'Dec')
    
        def test_wk_01(self):
            clk = Clock(2020, 1, 20, 9, 0, 0, 1)
            self.assertEqual(clk.wk, 'Monday')
    
        def test_wk_07(self):
            clk = Clock(2020, 1, 26, 9, 0, 0, 1)
            self.assertEqual(clk.wk, 'Sunday')
    
        def test_we_yes(self):
            clk = Clock(2020, 1, 26, 9, 0, 0, 1)
            self.assertEqual(clk.we, "It's weekend")
    
        def test_we_no(self):
            clk = Clock(2020, 1, 24, 9, 0, 0, 1)
            self.assertEqual(clk.we, "It's working day")
    
        def test_sz_01(self):
            clk = Clock(2020, 1, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Winter")
    
        def test_sz_02(self):
            clk = Clock(2020, 2, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Winter")
    
        def test_sz_03(self):
            clk = Clock(2020, 3, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Spring")
    
        def test_sz_04(self):
            clk = Clock(2020, 4, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Spring")
    
        def test_sz_05(self):
            clk = Clock(2020, 5, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Spring")
    
        def test_sz_06(self):
            clk = Clock(2020, 6, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Summer")
    
        def test_sz_07(self):
            clk = Clock(2020, 7, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Summer")
    
        def test_sz_08(self):
            clk = Clock(2020, 8, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Summer")
    
        def test_sz_09(self):
            clk = Clock(2020, 9, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Autumn")
    
        def test_sz_10(self):
            clk = Clock(2020, 10, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Autumn")
    
        def test_sz_11(self):
            clk = Clock(2020, 11, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Autumn")
    
        def test_sz_12(self):
            clk = Clock(2020, 12, 24, 9, 0, 0, 1)
            self.assertEqual(clk.sz, "Winter")
    
        def test_dt_midnight(self):
            clk = Clock(2020, 12, 24, 0, 0, 0, 1)
            self.assertEqual(clk.dt, "Midnight")
    
        def test_dt_noon(self):
            clk = Clock(2020, 12, 24, 12, 0, 0, 1)
            self.assertEqual(clk.dt, "Noon")
    
        def test_dt_dawn_winter(self):
            clk = Clock(2020, 12, 24, 8, 0, 0, 1)
            self.assertEqual(clk.dt, "Dawn")
    
        def test_dt_dawn_spring(self):
            clk = Clock(2020, 3, 24, 6, 0, 0, 1)
            self.assertEqual(clk.dt, "Dawn")
    
        def test_dt_dawn_summer(self):
            clk = Clock(2020, 6, 24, 5, 0, 0, 1)
            self.assertEqual(clk.dt, "Dawn")
    
        def test_dt_dawn_autumn(self):
            clk = Clock(2020, 10, 24, 6, 0, 0, 1)
            self.assertEqual(clk.dt, "Dawn")
    
        def test_dt_dusk_winter(self):
            clk = Clock(2020, 12, 24, 17, 0, 0, 1)
            self.assertEqual(clk.dt, "Dusk")
    
        def test_dt_dusk_spring(self):
            clk = Clock(2020, 3, 24, 19, 0, 0, 1)
            self.assertEqual(clk.dt, "Dusk")
    
        def test_dt_dusk_summer(self):
            clk = Clock(2020, 6, 24, 21, 0, 0, 1)
            self.assertEqual(clk.dt, "Dusk")
    
        def test_dt_dusk_autumn(self):
            clk = Clock(2020, 10, 24, 19, 0, 0, 1)
            self.assertEqual(clk.dt, "Dusk")

        def test_mn_01(self):
            clk = Clock(2020, 01, 24, 19, 0, 0, 1)
            self.assertEqual(len(clk.mn), 2)

        def test_mn_12(self):
            clk = Clock(2020, 01, 24, 19, 0, 0, 1)
            self.assertEqual(len(clk.mn), 2)

        def test_ms_0001(self):
            clk = Clock(2020, 01, 24, 19, 0, 0, 1)
            self.assertEqual(len(clk.ms), 4)

        def test_add(self):
            clk = Clock(2019, 12, 29, 19, 0, 0, 1)
            clk.add(hours=24*3+4) # + 8d 4h 
            date_ok = clk.yy == '2020' and clk.mn == '01' and clk.dd == '01' and clk.hh == '23'
            self.assertTrue(date_ok)


    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClock)
    #unittest.TextTestRunner().run(suite)    
