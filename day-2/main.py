#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to tip calculator!")
bill_amt = float(input("what was the total bill to be paid?"))
tip = int(input("what percent of tip would you like to give 10 , 12 , 15?"))
share = int(input("How many people to split the bill "))
tip_amt = float(bill_amt * (tip/100))
total_tip = float((tip_amt + bill_amt))
ind_bill = float(round((total_tip/share),2))
print(f"Each person should pay: {ind_bill}")