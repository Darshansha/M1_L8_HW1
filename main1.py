num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


org_result = num1 - num2 + num3
print("Original expression (", num1, "-", num2, "+", num3,") =", org_result)

mod_result = num3 - num1 + num2
print("Modified expression (", num3, "-", num1, "+", num2,") =", mod_result)