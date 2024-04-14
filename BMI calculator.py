height=float(input("Please enter your height in meters:"))
weight=float(input("Please eneter your weight in kilograms:"))

bmiCalculation=float(weight/(height**2))
bmi=round(bmiCalculation,1)
print("Your BMI is:",bmi)

if bmi<18.5:
    print("Sorry, you are underweight")
elif bmi<25:
    print("Congratulations, you are a healthy weight")
elif bmi<30:
    print("Sorry you are overweight")
else:
    print("You are obese")
    
result=int(input("Please select the option that corresponds to your bmi through options 1-4, [1.(Underweight) 2.(Healthy weight) 3.(Overweight) 4.(Obese)]  :"))

if result==1:
    print("You need to enter into a calorie surplus. This means you need to consume more calories than you burn.")
elif result==2:
    print("Well done! Keep up the good work.")
elif result==3:
    print("You need to enter into a calorie deficit. This means you need to burn more calories than you consume.")
elif result==4:
    print("You need to enter a major calorie deficit. You also need to seek advice from a medical proffesional.")
else:
    print("Please try again")