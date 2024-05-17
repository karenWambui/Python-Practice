def  add():
    try:
      #Get input from the user
      num1 = float(input("Enter the first number"))
      num2 = float(input("Enter the second number"))

      #Add numbers
      result = num1 + num2
      #display the result
      print(result)
    except ValueError:
      print('Invalid input')
if __name__ == "__main__":
    add()

def substract():
    try:
     num3 = float(input("Enter the third number"))
     num4 = float(input("Enter the fourth number"))
     result1 = num3 - num4
     print(result1)
    except ValueError:
       print("invalid")
if  __name__ == "__main__":
     substract()

def divide():
    try:
     num5 = float(input("Enter the fifth number"))
     num6 = float(input("Enter the sixth number"))
     result7 = num5/num6
     print(result7)
    except ValueError:
        print("Error")
#if  __name__ =="__main__":
divide()

   