# some_list = ['a','b','b','c','d','m','n','n']

# duplicates = []
# for x in some_list:
#     if  some_list.count(x) > 1:
#         if x not in duplicates:
#             duplicates.append(x)
# print(duplicates)

#A compression that prints duplicates
my_list ={'a','b','b','c','d','m','n','n'}
duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))
print(duplicates)


