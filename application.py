amount = float(input("Enter amount:"))
discount = 0.05 * amount
if (amount >= 1000):
  print("discount is ", discount)
else:
  print("no discount")





citizen = str(input("Enter citizen:"))
age = int(input("Enter age:"))
if (age >= 18 and citizen == 'kenyan'):
  print("eligible to vote")
else:
  print("no eligible")
