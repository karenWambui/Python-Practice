class SuperList(list):
    def __len__(self):
        return 1000
x = SuperList()
print(len(x))
x.append(6)
print(x)
print(issubclass(SuperList,list))

