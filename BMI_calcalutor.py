weight = float(input("Enter your weight(kg): "))
hight = float(input("Enter your hight in (cm): "))
BMI =int( weight/((hight/100)**2))
if BMI < 18.5:
    print("BMI = ",BMI,"Underweight")
elif 18.5 <= BMI < 25.0:
    print("BMI = ",BMI,"Normal")
elif 25.0 <= BMI < 30.0:
    print("BMI = ",BMI,"Overweight")
elif 30.5 <= BMI:
    print("BMI = ",BMI,"Obese")
