#7.1.6
#addition using function

def add_numbers(a, b):
    result = a + b
    return result

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")
