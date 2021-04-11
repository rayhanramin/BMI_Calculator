from bmi_cal.bmi import bmi_cal
import unittest

class test_bmi_val(unittest.TestCase):
    def test_bmi_input_height(self):
        bm=bmi_cal()
        self.assertEqual(bm.calculate_bmi(0,0,0),"Height can not be zero")
        self.assertEqual(bm.calculate_bmi(-1,0,0),"Height can not be negative")
        self.assertEqual(bm.calculate_bmi(-1,-1,0),"Height can not be negative")
        self.assertEqual(bm.calculate_bmi(0,0,1501),"Height can not be zero")
        self.assertEqual(bm.calculate_bmi(-1,0,1500),"Height can not be negative")
        self.assertEqual(bm.calculate_bmi(-1,-1,-1),"Height can not be negative")
        self.assertEqual(bm.calculate_bmi(5,-1,0),"Height can not be negative")
        self.assertEqual(bm.calculate_bmi(0,12,0),"Inches value should be in between 0 to 11")
        self.assertEqual(bm.calculate_bmi(6,3,1501),"Weight can not be greater than 1500lbs")
        self.assertEqual(bm.calculate_bmi(10,0,0),"Height can not be 10 feet or more")
        self.assertEqual(bm.calculate_bmi(10,0,-1),"Height can not be 10 feet or more")
        self.assertEqual(bm.calculate_bmi(10,0,140),"Height can not be 10 feet or more")
        self.assertEqual(bm.calculate_bmi(10,0,1500),"Height can not be 10 feet or more")
        self.assertEqual(bm.calculate_bmi(10,0,1501),"Height can not be 10 feet or more")

    def test_bmi_input_weight(self):
        bm = bmi_cal()
        self.assertEqual(bm.calculate_bmi(5,10,0),"Weight can not be zero or negative")
        self.assertEqual(bm.calculate_bmi(5,10,-1),"Weight can not be zero or negative")
        self.assertEqual(bm.calculate_bmi(6,3,1500),"Your bmi is 192.0 and you are obese")

    def test_bmi_valid(self):
        bm=bmi_cal()
        self.assertEqual(bm.calculate_bmi(5,0,140),"Your bmi is 28.0 and you are over weight")
        