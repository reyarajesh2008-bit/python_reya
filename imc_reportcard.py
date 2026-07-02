print("REPORT CARD OF STUDENT")
a = int(input("Enter STUDENT registration_number:"))
b = (input("Enter STUDENT name:"))
c = input("Enter STUDENT class (eg: 11 B):")
print("ENTER YOUR MARKS OUT OF 100")
maths = int(input("Enter maths marks:"))
physics = int(input("Enter physics marks:"))
chemistry = int(input("Enter chemistry marks:"))
biology = int(input("Enter biology marks:"))
english = int(input("Enter english marks:"))
avg = (maths+physics+biology+chemistry+english)/5
if avg>90:
    grade ="A1"
elif avg>80 and avg<=90:
    grade = "A"
elif avg>70 and avg<=80:
    grade = "B1"
elif avg>60 and avg<=70:
    grade = "B"
elif avg>50 and avg<=60:
    grade = "C"
else:
    grade = "F"

print("-------------------------------------------------------------")
print("REPORT_CARD")
print("-------------------------------------------------------------")
print("1.Registration_no     :",a)
print("-------------------------------------------------------------")
print("2.Name of student     :",b.upper())
print("-------------------------------------------------------------")
print("3.Class/Division      :",c)
print("-------------------------------------------------------------")
print("4.Total marks on 500  :",maths+physics+biology+chemistry+english)
print("-------------------------------------------------------------")
print("5.Grade of the student:",grade)
print("-------------------------------------------------------------")

if grade == "A1" or "A" or "B" or "B1" or "C":
    print(b.upper(),"Passed!!!")
else:
    print(b.upper,"Failed")
