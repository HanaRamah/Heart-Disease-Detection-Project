from experta import *

class Patient(Fact):
    pass

class HeartDiseaseExpert(KnowledgeEngine):
    def __init__(self):  # FIXED: Correct __init__ method
        super().__init__()
        self.risk_level = 0  # Initialize risk score
        self.risk_assessments = []  # Store all triggered rules

    # Rule 1: High cholesterol and older age
    @Rule(Patient(chol=MATCH.chol, age=MATCH.age),
          TEST(lambda chol, age: chol > 240 and age > 50))
    def rule1(self):
        self.risk_level += 30
        self.risk_assessments.append("High Risk: High Cholesterol (>240) and Age (>50)")

    # Rule 2: High blood pressure and smoking
    @Rule(Patient(bp=MATCH.bp, smoking="Yes"),
          TEST(lambda bp: bp > 140))
    def rule2(self):
        self.risk_level += 25
        self.risk_assessments.append("High Risk: High BP (>140) and Smoker")

    # Rule 3: Regular exercise and healthy BMI
    @Rule(Patient(exercise="Regular", bmi=MATCH.bmi),
          TEST(lambda bmi: bmi < 25))
    def rule3(self):
        self.risk_level -= 20
        self.risk_assessments.append("Low Risk: Regular Exercise and Healthy BMI (<25)")

    # Rule 4: Diabetes and obesity
    @Rule(Patient(diabetes="Yes", bmi=MATCH.bmi),
          TEST(lambda bmi: bmi > 30))
    def rule4(self):
        self.risk_level += 35
        self.risk_assessments.append("High Risk: Diabetes and Obesity (BMI >30)")

    # Rule 5: Family history and high cholesterol
    @Rule(Patient(family_history="Yes", chol=MATCH.chol),
          TEST(lambda chol: chol > 200))
    def rule5(self):
        self.risk_level += 20
        self.risk_assessments.append("Moderate Risk: Family History and High Cholesterol (>200)")

    # Rule 6: Young and active
    @Rule(Patient(age=MATCH.age, exercise="Regular"),
          TEST(lambda age: age < 40))
    def rule6(self):
        self.risk_level -= 15
        self.risk_assessments.append("Low Risk: Young Age (<40) and Regular Exercise")

    # Rule 7: Severe hypertension
    @Rule(Patient(bp=MATCH.bp),
          TEST(lambda bp: bp > 180))
    def rule7(self):
        self.risk_level += 40
        self.risk_assessments.append("Very High Risk: Severe Hypertension (>180)")

    # Rule 8: Healthy lifestyle
    @Rule(Patient(smoking="No", exercise="Regular", chol=MATCH.chol),
          TEST(lambda chol: chol < 200))
    def rule8(self):
        self.risk_level -= 25
        self.risk_assessments.append("Low Risk: Non-smoker, Active, and Good Cholesterol (<200)")

    # Rule 9: Multiple risk factors
    @Rule(Patient(smoking="Yes", diabetes="Yes", bp=MATCH.bp),
          TEST(lambda bp: bp > 140))
    def rule9(self):
        self.risk_level += 45
        self.risk_assessments.append("Very High Risk: Smoking, Diabetes, and High BP (>140)")

    # Rule 10: Optimal health
    @Rule(Patient(bp=MATCH.bp, chol=MATCH.chol, bmi=MATCH.bmi),
          TEST(lambda bp, chol, bmi: bp < 120 and chol < 180 and bmi < 25))
    def rule10(self):
        self.risk_level -= 30
        self.risk_assessments.append("Very Low Risk: Optimal BP (<120), Cholesterol (<180), and BMI (<25)")

    def assess_risk(self):
        """Determine final risk assessment based on score"""
        if self.risk_level >= 60:
            return "Very High Risk"
        elif self.risk_level >= 30:
            return "High Risk"
        elif self.risk_level >= 10:
            return "Moderate Risk"
        elif self.risk_level >= 0:
            return "Low Risk"
        else:
            return "Very Low Risk"





