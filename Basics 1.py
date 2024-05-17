'''Fundamentel Data types
int
float
bool:can either be true or false
str
list
tuple
dist
set

print(22* 44) 
print(type(6)) #checking the datatype
print(type(0.8888)) 
math functions

print(round(3.2))#rounds off
print(abs(-20))# removes negative
print(bin(5))

print('hello' + '', "there") # strings concantenation

print(type(str(100))) #type conversion
print(type(int(str(1000)))) #you converted the number to str,then to converted it back
'''
'''Escape Sequence adding \n(new line),\t(new tab)
formatted strings
name = 'Karen'
age = 24
#print('hi' + '', name +'.You are' + '',str(age) + '','years old' )
print(f'hi{name}. You are {age} years old')  #formatted string

print('hi{}. You are {} years old'.format('Karen','24'))
selfish = 'me me me'
#print(selfish[0:8])
print(selfish[-3])
greet = 'hellloooo'
print(greet[0:9])# slicing

name = 'Karen Mwaura'
age = 50
relationship_status = 'single'
relationship_status='it\'s complicated'
print(relationship_status)'''

#Q1.Write a code that asks for your name,year of birth and prints your age
'''name = input('What is your name')
birth_year = input ('What year were you born?')
birth_year = int(birth_year)
import datetime
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"Hello,{name}!,you are {age} years old.")

#another method to solve this

name = input('What is your name')
birth_year = input ('What year were you born?')
current_year = 2024
age = current_year- int(birth_year) # birth_year input is converted to string so you have to change it back to interger
print(f'{name}! you are{age} years old.')

username = input('What is your username')
password= input('What is your password?')
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password {hidden_password} is{password_length}letters long')
 '''
#lists ordered sequence of objects that can be of any type
'''amazon_cart =['notebooks','sunglasses','toys','grapes']
amazon_cart [0] ='crips'
print(amazon_cart[0:3]) #list slicing
matrix = [
    [1,2,3],
    [3,4,5],
    [7,8,9]
]
print(matrix[2][1]) 
basket = [1,2,3,4,5]
print(len(basket))

#adding methods
basket =[1,2,3,4,5]
new_list = basket.append(100) # adds a 100 to basket list
basket.insert(3,100)  inserts 100 at index four
new_list = basket.extend([100,101])
new_list = basket
print(basket)
print(new_list)

#removing methods
basket =[1,2,3,4,5]
new_list = basket.remove(4)
basket.pop(0) # removes the item in this index 
new_list = basket.clear()
print(basket)'
#basket =[1,2,3,4,5]
#print(basket.index(3))checks for index

basket = ['a','b','c','d']
print('b' in basket)checks if b is in basket

basket = ['a','y','b','c','d']
#print(basket.count('c'))  returns 1.it checks the number of occurences
#basket.sort() takes y to the end
print(sorted(basket))
basket.reverse()
print(basket[:])

basket = ['a','y','b','c','d']
print(sorted(basket))
basket.reverse()

print(list(range(1,100)))

new_sentence = ''.join(['hi','my','name','is','Karen'])
print(new_sentence)

#list unpacking
a,b,c,*other,d =[1,2,3,7,8,9,10]
print(a)
print(b)
print(c)
print(other)
print(d)

#Dictionaries it has keys
dictionary = {
    5:[1,2,3,4],
    'a':'Helloo',
    'x':True,
    'age':20
}
#print(dictionary.get('z')) returns None
print(dictionary.get('age',24))

#Another method of creating dictionaries
user2 = dict(name='Karen')
print(user2)

#Looking for items in dictionaries
dictionary = {
    5:[1,2,3,4],
    'a':'Helloo',
    'x':True,
    'age':20
}

#print('size'in dictionary)  returns false
print('age' in dictionary.keys())
print('Helloo' in dictionary.values())
print(dictionary.items()) #grabs the entire items
print(dictionary.clear())
print(dictionary.copy())

#Tuple
my_tuple = (1,2,3,4,5)
print(5 in my_tuple)

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]
print(new_tuple)'''

#my_set = {1,2,3,4,5,5} only returns the unique values,no duplicates
my_set = {4,5} 
your_set ={4,5,6,7,8,9}
#my_set.add(100) adds 100
#print(1 in my_set) checks if 1 is in the set
 
print(my_set.difference(your_set))
print(my_set.intersection(your_set))
#print(my_set.isdisjoint(your_set)) nothing similar
print(my_set.union(your_set))#removes duplicates
print (my_set.issubset(your_set))
print (my_set.issuperset(your_set))














#Classes -> custom types
#Specialized data types
#None absence of value

