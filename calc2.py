#adding the numbers
def add(y,z):
  return y + z
# substracting
def substract(y,z):
  return y-z

def multiply(y,z):
  return y * z

def divide(y,z):
  return y/z

print("Please choose the operation")
print("a.Add")
print("b.Substract")
print("c.Multiply")
print("d.Divide")

choice = input("Please enter your choice one a/b/c/d:")

num1 = int(input("please enter the first number"))
num2 = int(input("Enter the second number "))

if choice =="a":
  print(num1 + num2)

elif choice =="b":
  print(num1 - num2)
elif choice =="c":
  print(num1 * num2)
elif choice == "d":
   print(num1/num2)
else:
  print("invalid")