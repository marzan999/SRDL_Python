'''
number = int(input("Enter a number: "))

count = 1

while count <= 10:
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1




number = int(input("Enter a number: "))

count = 10

while count >= 1:
    product = number * count
    print(number, "x", count, "=", product)
    count = count - 1'''


its_raining = True
while its_raining:
    print("It's raining!")
    answer = input("Or is it? (y=yes, n=no) ")
    if answer == 'y':
        print("Oh well...")
    elif answer == 'n':
        its_raining = False     # end the while loop
    else:
        print("Enter y or n next time.")
print("It's not raining anymore.")