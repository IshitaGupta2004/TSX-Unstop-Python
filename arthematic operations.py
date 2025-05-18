num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2 if num2 != 0 else "Cannot divide by zero")
print("Modulus        :", num1 % num2 if num2 != 0 else "Undefined")
print("Exponentiation :", num1 ** num2)
