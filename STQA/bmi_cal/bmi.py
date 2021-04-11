


class bmi_cal:

    def calculate_bmi(self, feet, inches, weight):
        self.feet = feet
        self.inches = inches
        self.weight = weight

        #refine alittle bit more
        if self.feet == 0 and self.inches == 0: 
            s = "Height can not be zero"
            return s
        elif self.feet < 0 or self.inches < 0: 
            s = "Height can not be negative"
            return s
        elif self.feet >= 10:
            return("Height can not be 10 feet or more")
        elif self.inches not in range(0,11):
            return ("Inches value should be in between 0 to 11")
        elif self.weight <= 0:
            return ("Weight can not be zero or negative")
        elif self.weight > 1500:
            return ("Weight can not be greater than 1500lbs")
        else:
            leng = float(((self.feet*12)+self.inches)*0.025)
            wt = float(self.weight*0.45)
            bmi = float(wt/(leng*leng))
            if bmi <= 0:
                return ("BMI can not be negative or zero. Sorry there must be something wwrong")
            elif bmi < 18.5:
                return ("Your bmi is {} and you are under weight".format(bmi))
            elif bmi >= 18.5 and bmi <=24.9:
                return ("Your bmi is {} and you are normal weight".format(bmi))
            elif bmi >= 25 and bmi <=29.9:
                return ("Your bmi is {} and you are over weight".format(bmi))
            elif bmi >= 30:
                return ("Your bmi is {} and you are obese".format(bmi))
            