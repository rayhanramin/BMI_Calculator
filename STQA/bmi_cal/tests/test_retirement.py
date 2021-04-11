
import unittest
from bmi_cal.retirement import ret

class test_ret_goal(unittest.TestCase):
    def test_ret_age(self):
        rt=ret()
        self.assertEqual(rt.retirement_cal(0,0,0,0),"Age cannot be zero or negative or greater than 100")
        self.assertEqual(rt.retirement_cal(-1,0,0,0),"Age cannot be zero or negative or greater than 100")
        self.assertEqual(rt.retirement_cal(101,0,0,0),"Age cannot be zero or negative or greater than 100")
        self.assertEqual(rt.retirement_cal(101,65000,10,100000),"Age cannot be zero or negative or greater than 100")

    def test_ret_salary(self):
        rt=ret()
        self.assertEqual(rt.retirement_cal(100,0,0,0),"Salary cannot be zero or negative or greater than 500k")
        self.assertEqual(rt.retirement_cal(30,-1,0,0),"Salary cannot be zero or negative or greater than 500k")
        self.assertEqual(rt.retirement_cal(30,500001,0,0),"Salary cannot be zero or negative or greater than 500k")

    def test_ret_percent(self):
        rt=ret()
        self.assertEqual(rt.retirement_cal(25,65000,0,0),"Percentage cannot be zero or negative or greater than 100")
        self.assertEqual(rt.retirement_cal(25,65000,-1,0),"Percentage cannot be zero or negative or greater than 100")
        self.assertEqual(rt.retirement_cal(25,65000,101,0),"Percentage cannot be zero or negative or greater than 100")

    def test_ret_target(self):
        rt = ret()
        self.assertEqual(rt.retirement_cal(25, 65000, 25, 0), "Target amount can not be zero or negative")
        self.assertEqual(rt.retirement_cal(25, 65000, 25, -1), "Target amount can not be zero or negative")

    def test_ret_valid(self):
        rt=ret()
        self.assertEqual(rt.retirement_cal(25,85000,15,1500000),"The goal will not be met")
        self.assertEqual(rt.retirement_cal(1,85000,15,1500000),"The goal will be met when the age is 89")
        self.assertEqual(rt.retirement_cal(100,85000,15,1500000),"The goal will not be met")
        self.assertEqual(rt.retirement_cal(25,85000,20,1000000),"The goal will be met when the age is 69")
        self.assertEqual(rt.retirement_cal(25,1,20,1000000),"The goal will not be met")
        self.assertEqual(rt.retirement_cal(25,500000,20,1000000),"The goal will be met when the age is 33")
        self.assertEqual(rt.retirement_cal(25,85000,20,1000000),"The goal will be met when the age is 69")
        self.assertEqual(rt.retirement_cal(25,85000,1,1000000),"The goal will not be met")
        self.assertEqual(rt.retirement_cal(25,85000,100,1000000),"The goal will be met when the age is 34")
