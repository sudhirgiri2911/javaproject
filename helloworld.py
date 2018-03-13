class Plant():
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
        

class Water_Plant(Plant):
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

a=input('Sudhir, welcome!')
print(a)

