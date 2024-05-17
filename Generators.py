#Generator functions
# def generator_function(num):
#     for i in  range(num):
#         yield i*2

# g = generator_function(100)
# next(g)
# print(next(g))
# for i in generator_function(1000):
#     print(i)


def gen_func(num):
    for item in range(num):
        yield item *4
for item in gen_func(100):
        print(item)


#def make_list(num):
    # result = []
    # for i in range(num):
    #     result.append(i*2)
    # return result