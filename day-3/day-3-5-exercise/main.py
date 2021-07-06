# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name3 = name1 +name2
partner_name = name3.lower()
# partner1_name = name1.lower()
# partner2_name = name2.lower()

l = int(partner_name.count("l"))
o = int(partner_name.count("o"))
v = int(partner_name.count("v"))
e = int(partner_name.count("e"))
num1 = l+o+v+e
# print(num1)
# print(type(num1))
num3 = str(num1)
# print(type(num3))
t = int(partner_name.count("t"))
r = int(partner_name.count("r"))
u = int(partner_name.count("u"))
e = int(partner_name.count("e"))
num2 = t+r+u+e
num4 = str(num2)

num5 = num4+num3
print(type(num5))
print(num5)
num6 = int(num5)

if num6<10 or num6>90:
  print(f"Your love score is {num6} , You go together like coke and mentos.")
elif num6>=40 and num6<=50:
  print(f"Your love score is {num6} , You are alright together")
else:
  print(f"Your love score is {num6} and a Perfect Partner.")


