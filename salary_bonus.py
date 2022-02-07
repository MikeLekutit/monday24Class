salary = int (input("Enter your salary"))
year = int(input("Enter year"))
if year>10:
    bonus = salary * 0.01
    print(bonus)
if year>=6 and year<=10:
    bonus = salary * 0.08
    print(bonus)
if year<6:
    bonus = salary * 0.05
    print(bonus)
