#pure functions
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*3)
#     return new_list
# print(multiply_by2([1,2,3]))

#map,filter,zip and reduce

# def multiply_2(item):
#     return item * 2
# my_list = [1,2,3]
# print(list(map(multiply_2,my_list)))
# print(my_list)


# def  double(x):
#     return x * 3
     
# numbers =[1,2,3,4]
# doubled_numbers =map(double,numbers)

# doubled_numbers_list = list(doubled_numbers)
# print(doubled_numbers_list)


#filters

# def multiplt_2(item):
#     return item*2

# my_list =[1,2,3,4]

# def only_odd(item):
#     return item %2 ==0
# print(list(filter(only_odd,my_list)))
# print(my_list)

#zip ()
# my_list = [1,2,3,4]
# your_list = [5,6,7,8]
# their_list =[9,10,11,12]
# def multiply_2(item):
#     return item*2

# def only_odd(item):
#     return item % 2 !=0
# print(list(zip(my_list,your_list,their_list)))


#reduce()
# from functools import reduce
# my_list = [1,2,3,4]

# def multiply_2(item):
#     return item*2

# def only_odd(item):
#      return item % 2 !=0
# def accumulator(acc,item):
#      print(acc,item)
#      return acc+ item
                                                                                                                                                                                               
# print(reduce(accumulator,my_list,10))
# print(my_list)

#lambda
# from functools import reduce
# my_list =[1,2,3]

# def only_odd(item):
#     return item %2 !=0
# def accumulator(acc,item):
#       print(acc,item)
#       return acc+ item
                                                                                                                                                                                               
# print(list(map(lambda item:item*2,my_list)))
# print(my_list)

 

#list,set,dictionary
# my_list =[char for char in 'hello']
# print(my_list)
# my_list1= [num**2 for num in  range(0,100)]
# print(my_list1)
# my_list4= [num**2 for num in  range(0,100)
#           if num % 2 ==0]
# print(my_list4)


#set comperehension

# my_list1= {num**2 for num in  range(0,100)}
# print(my_list1)


#dictionary comprehension
# simple_dict ={
#     'a':1,
#     'b':2
# }
# my_dict ={key:value**2 for key,value in simple_dict.items()}

# print(my_dict)


# our_dict = {num:num*2 for num in [1,2,3]}
# print(our_dict)

# my_dict = {char:char for char in 'hello'}
# print(my_dict)



