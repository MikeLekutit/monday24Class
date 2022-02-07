print("Enter the subject")
math= int(input("math"))
eng= int(input("eng"))
hist= int(input("hist"))
phyc = int(input("phyc"))
sci= int(input("sci"))
avg_marks = (math+eng+hist+phyc+sci)/5
print(avg_marks)
avg_grade =""
if marks>=100:
    print('A')
elif marks>=60 and marks<=69:
    print('B')
elif marks>=50 and marks<=59:
    print('C')
elif marks>=40 and marks<=49:
    print('D')
elif marks>=0 and marks<=39:
    print('Fail')
    print("avg_grade")
