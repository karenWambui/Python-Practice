#Conditional logic
#if
#if else
#elif
''''is_old = True
is_licenced = True
if is_old :
    print('you are old enough to drive')

else:
    print('You can\'t drive')


is_old = False
is_licenced = False

if is_old :
    print('you are old enough to drive')
elif is_licenced:
    print('Its okay to drive')
else:
    print('You can\'t drive ')


is_old = True
is_licenced = True  
if is_old and is_licenced:
     print('You are old enough to drive,and you have a licence!')
else:
     print('you are not of age')
#Truthy and Falsy
is_old = bool('hello')
is_licenced = bool(5)

print(bool(''))
print(bool(5))#true
print(bool(0))# gives false
if is_old and is_licenced:
     print('You are old enough to drive,and you have a licence!')
else:
     print('you are not of age')


#Ternary Operator
#condition_if_true if condition else condition_if_else

is_smart = True
can_message = "Text me" if is_smart else "Do not text me"
print(can_message)

tall = True
can_call ="Call me" if tall else "Do not text me"
print(can_call)


#Short Circuiting
is_Friend = False
is_User = False

if is_Friend and is_User:
    print('best friends forever')

#Logical operators >,<,==,,!=,not
print(4>5)
print('a' > 'b')
print('a' > 'A')
print(1<2<3<4<5)
print(0<=0)
print (0 != 0)
print(not(True))
print(not(1==1))'''


#Exercise 1
#is_magician = True
#is_expert = False
#Check if magician and expert :"you are a master magician"
#Check if magician but not expert:"at least you're getting there"
#if youre not a magician:you need magic powers


'''is_magician = False
is_expert = True
if is_magician and is_expert:
  print('you are a master magician')
elif is_magician and not is_expert:
   print ("at least you\'re getting there")
elif not is_magician:
    print("you need magic powers")

print(True == 1)
print(''== 1)
print([] == 1)
print(10 == 10.0)
print([]==[])'''


#Loops
#for item in [1,2,3,3,4,4,5,6,6,9]: 
    #print(item)
   
'''user = {
       'name':'Karen',
       'age': 24,
       'can_swim':False
 }
#for item in user:
#print(item)
for item in user.values():
     print(item)

for item in user.keys():
     print(item)

for key,value in user.items():
     print(key,value)

#Excercise one,using looping and sum up the values in the list
my_list =[1,2,3,4,5,6,7,8,9,10]
total =0

for item in my_list:
    total = total + item
    print(total)
  
#range 
for num in range(100):
  print(num)
for num in range(10):
   print('email email list')

for _ in range(0,10,2):
   print(_)
for _ in range(10,0,-1):#goes to opposite direction
   print(_)
#for _ in range(5):
    #print(list(range(10)))

#enumerate checks index,check the indx of 50
for i,char in enumerate('Hellooo'):
    print(i,char)
for i,char in enumerate(list(range(100))):
    if char ==50:
        print(f'index of 50 is:{i}')
# while loop
i=0
while 50 <50:
    print(i)
    i+=1
else:
    print('done all the work')
    
for item in [1,2,3]:
    print(item)
i=0

my_list = [1,2,3,4]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i+=1
while True:
  response = input('say something: ')
  if (response == 'bye'):
    break
#Exercise
picture =[
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
for row in picture:
    for pixel in row:
       if (pixel == 1):
          print('*',end='')
    else:
        print('',end='')
    print('')
#checking duplicated some_list =['a','b','c','b','d','m','n','n']

duplicates =[]
for value in some_list:
 if some_list.count(value) > 1:
     if value not in duplicates:
      duplicates.append(value)
print(duplicates)


#Functions 
def say_hello():
    print('heloo')
say_hello()'''
#parameters
def say_hello(name,emoji):
   print(f'helooo{name}{emoji}') 
   
#arguements
say_hello('Andrei','🤭')
say_hello('Karen','🥴' )

def sum(num1,num2):
   return num1 + num2 
total = sum(10,5)
print(sum(10,total))

#clean code
def is_even(num):
    if num % 2==0:
         return True
    elif num % 2!=0:
        return False
    print(is_even(51))
   
def super_func(args):
    print(args)
    return sum(args)
print(super_func[1,2,3,4,5])
                                                                                                                                                                    






