from art import logo
print(logo)

def operation(a, b, oper):
  solution = {
    '+':a+b,
    '-':a-b,
    '*':a*b,
    '/':a/b
  }
  return round(solution[oper],2)
  

operations = ['+','-','*','/']


first_number = float(input("Enter your first number: "))

for operator in operations:
  print(operator)


calculator_on = True
while calculator_on:
  what_to_do = input('Choose an operation: ').strip()
  next_number = float(input("Enter your next number: "))
  if what_to_do ==  '/' and next_number == 0:
    print('Division by zero is not possible,enter a different number')
    next_number = float(input("Enter your next number: "))
  answer = operation(first_number,next_number,what_to_do)
  print(f"{first_number} {what_to_do} {next_number} = {answer}")
  to_continue = input(f'Type "y" to continue calculation with {answer}, or type "n" to start a new calculation. To turn off type "o": ').strip().lower()
  if to_continue == 'y':
    first_number = answer
  elif to_continue == 'n':
    first_number = float(input("Enter your first number: "))
  elif to_continue == 'o':
    calculator_on = False 
    

