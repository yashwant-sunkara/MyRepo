import random
num = int(input("Enter number of employees "))
empList = []
# input from employees
for i in range(num):
    emp = []
    first_name = input("Enter your first name: ")
    emp.append(first_name)
    last_name = input("Enter your last name: ")
    emp.append(last_name)
    print("Select 1st# (1 thru 69): ")
    number = int(input())
    while number in emp or number not in range(1, 70):
        print("Please enter a unique number between 1 to 69 ")
        number = int(input())
    emp.append(number)
    print("Select 2nd# (1 thru 69 excluding ", emp[2], "): ")
    number = int(input())
    while number in emp or number not in range(1, 70):
        print("Please enter a unique number between 1 to 69 ")
        number = int(input())
    emp.append(number)
    print("Select 3rd# (1 thru 69 excluding ", emp[2], " and ", emp[3], "): ")
    number = int(input())
    while number in emp or number not in range(1, 70):
        print("Please enter a unique number between 1 to 69 ")
        number = int(input())
    emp.append(number)
    print("Select 4th# (1 thru 69 excluding ", emp[2], " and ", emp[3], " and ", emp[4], "): ")
    number = int(input())
    while number in emp or number not in range(1, 70):
        print("Please enter a unique number between 1 to 69 ")
        number = int(input())
    emp.append(number)
    print("Select 5th# (1 thru 69 excluding ", emp[2], " and ", emp[3], " and ", emp[4], " and ", emp[5], "): ")
    number = int(input())
    while number in emp or number not in range(1, 70):
        print("Please enter a unique number between 1 to 69 ")
        number = int(input())
    emp.append(number)
    print("select Power Ball # (1 thru 26): ")
    number = int(input())
    while number not in range(1, 27):
        print("Please enter a number between 1 to 26 ")
        number = int(input())
    emp.append(number)
    empList.append(emp)
#finding count of individual number
frequency = []
powerball = []
for i in range(2, 8):
    c = []
    for val in empList:
        c.append(val[i])
    counter = {x: c.count(x) for x in c}

    frequency.append(counter)
# choosing random number if max counts tied for powerball
maxcounts = []
for y in frequency:
   maxcounts.append([key for key, val in y.items() if val == max(y.values())])
for k in maxcounts:
    powerball.append(random.choice(k))

for it in empList:
    for n in range(0, 7):
        print(it[n], " ", end='')
    print("Powerball: ", it[7])

print("Powerball winning number:")
for val in range(0, 5):
    print(powerball[val], " ", end='')
print("Powerball: ", powerball[5])
