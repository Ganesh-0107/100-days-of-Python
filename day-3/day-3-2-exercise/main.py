# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi  = float(round((weight/(height*height)),1))
print(bmi)
print(type(bmi))
if bmi<18.5:
  print(f"your BMI is {bmi} , You are underweight")

elif bmi<25:
  print(f"Your bmi is {bmi} , You weight is normal")

elif bmi<30:
  print(f"Your BMI is {round(bmi)} , You are slightly overweight")

elif bmi<35:
  print(f"Your bmi is {bmi} , You are obese")

elif bmi>=35:
  print(f"Your bmi is {bmi} , You are critically obese")


