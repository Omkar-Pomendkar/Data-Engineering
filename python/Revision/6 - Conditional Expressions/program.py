# WAP to find out whetehr a student is pass or fail , if it requires total 40% and atleast 33% in each subject to pass Assume 3 Subject and take marks as an inout from user
english = int(input("Enter marks you got in English"))
science = int(input("Enter marks you got in science"))
maths = int(input("Enter marks you got in Maths"))

total = english+science+maths
# print(total)

if(english > 33 and science > 33 and maths >33 and total > 120):
    
    print(total ," Student is pass")
else:
    print(total ," Student is Fails")
    