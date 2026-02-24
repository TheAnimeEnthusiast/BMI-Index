print("This test is only suitable for those above age 19.")

weight = float(input("What is your weight in kg?"))

height = float(input("What is your height in meters?"))

bmi = weight/height**2

print(f"Your BMI is {bmi}!")

if bmi < 18.5:

    print("You are underweight.")

elif bmi >= 18.5 and bmi <= 24.9:

    print("You are at a healthy weight.")

elif bmi >= 25 and bmi <= 29.9:

    print("You are overweight.")


else:

    print("You are obese.")

