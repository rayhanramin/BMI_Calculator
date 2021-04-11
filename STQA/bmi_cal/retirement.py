import math


class ret:
    def retirement_cal(self,age,salary,percent,target):
        self.age=age
        self.salary=salary
        self.percent=percent
        self.target=target
        age_limit = 100 

        if self.age <=0 or self.age > 100:
            return ("Age cannot be zero or negative or greater than 100")
        elif self.salary <=0 or self.salary > 500000:
            return("Salary cannot be zero or negative or greater than 500k")
        elif self.percent <= 0 or self.percent >100:
            return("Percentage cannot be zero or negative or greater than 100")
        elif self.target <=0:
            return("Target amount can not be zero or negative")
        else:
            saving_per_season = (float(salary)*(self.percent/100))*1.35
            years_till_goal = math.ceil(self.target/saving_per_season)
            final_age = self.age+years_till_goal
            if final_age <= age_limit:
                return("The goal will be met when the age is {}".format(final_age))
            else:
                return("The goal will not be met")
        