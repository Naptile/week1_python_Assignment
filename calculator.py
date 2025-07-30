print("Welcom to the Calculator App")
num1 = int(input("Enter the first Number: ")) #first number
num2 = int(input("Enter the second number: "))#second number
operator =str( input("Input the operation : "))
if operator == '+':
 answer =(num1 + num2)
elif operator == '-' :
 answer = (num1-num2 )
elif operator == '/' :
  if num2 !=0:
    answer =  (num1/num2)
  else :
    answer = "Division by zero is not allowed"
elif operator == '*':
 answer =(num1 * num2)
elif operator == '**':
 answer = (num1 ** num2)
elif operator == '%':
 answer =(num1 % num2)
elif operator == '//' :
 answer =(num1 // num2)
else :
 print("Invalid Operator")
print(answer)