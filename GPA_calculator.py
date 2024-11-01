#Start from here
#Message for welcome to our students
print("Hello in GPA calculator ")

# 7 subjects >> college
#150 * 7 = 1050 Degree
# important value (25%)

# Please enter your 1st subject marks:
x1 = input("please enter your 1st subject marks : ")

x2 = input("please enter your 2st subject marks : ")

x3 = input("please enter your 3st subject marks : ")

x4 = input("please enter your 4st subject marks : ")

x5 = input("please enter your 5st subject marks : ")

x6 = input("please enter your 6st subject marks : ")

x7 = input("please enter your 7st subject marks : ")

# Variable for (sum) :
sum = x1 + x2 + x3  + x4 + x5 + x6 + x7

# Variable for  (%) :
percentage = float(sum) / 1050

# Varaiale of (GPA) :
GPA = percentage / .25

if GPA >= 3.7 :
    print("your grade is 'A'  and your GPS is: " + str(GPA))

elif GPA >= 2.7 :
    print("your grade is 'B'  and your GPS is: " + str(GPA))

elif GPA >= 1.7 :
    print("your grade is 'C'  and your GPS is: " + str(GPA))

elif GPA >= 1 :
    print("your grade is 'D'  and your GPS is: " + str(GPA))

else  :
    print("your grade is 'F'  and your GPS is: " + str(GPA))

print("Thank you for use our application")