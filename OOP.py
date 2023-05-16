# ================ Constractor ======================

class User:
    name = 'sina'
    family = 'pirzadeh'

    def __init__(self, name, family):
        self.name = name
        self.family = family


FullName = User('sian','pirzadeh')



# ================ private  ======================

_ـname = 'sina pirzadeh'
print(_ـname)

# ================ repr  ======================
# this 'repr' for use object 
class User_3:
    
    def __init__(self,name,famly,age):
        self.name = name
        self.family = famly
        self.age = age

    def __repr__(self) -> str:
        return f"name is {self.name} family is {self.family} and age is {self.age}"
    

me = User_3('sina','pirzadeh',18)  
print(me)


# ================ Property ======================

class User_4:
    
    def __init__(self,fullName,age) -> None:
        self.FullName = fullName
        self._age = age

    @property
    def age(self):
        return f'age is {self._age}'
    
    @age.setter
    def age(self,value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('age con not by negative')
        

me = User_4('sinapirzadeh',12)
me.age = 23
print(me.age)


# ================ Inheritance ======================

class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    @property
    def fullName(self):
        return f'{self.name} as {self.model}'
    

class Sherkat_BMW(Car):
    pass


BMW = Sherkat_BMW('ford',12)
print(BMW.fullName)


# ================ Polymorphic ======================

class Dog:
    
    def Sond(voic):
        print('dog sey ',voic)

class Cat:

    def Sond(voic):
        print('dog sey ',voic)
    

Cat.Sond('hop hop')
Cat.Sond('meo meo')


# ================ del ======================


person1 = Dog.Sond('fii')


def __del__(sef):
    print("End....")

del(person1)

# ================ END For Now ======================