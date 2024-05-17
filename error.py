#error handling
# while True:
#     try:
#         age = int(input('wHAT OS YPUR AGE'))
#         10/0
#         print(age)
#     except ValueError:
#          print('please enter a number')
#     except ValueError:
#          print('!!!!!')
#     except ZeroDivisionError:
#          print('please enter age higher than o')
#     else:
#           print('Thank you')
#           break
    
def sum(num1,num2):
    try:
        return num1/num2
    except (TypeError,ZeroDivisionError) as err:
        print(err)
     
print(sum(1,'2'))
