# py projects from sina pirzadeh for learning Python >> mysite : sinapirzadeh.com


# user_input = int(input('Etner your number :'))

# result = chr(user_input)
# ord_result = ord(result)
# print(result,ord_result, sep='  ->  ')

# -------------------------------------------------

# if 3 > 2: print('yes')

# print('yes') if 3 > 2 else print('no')

# x = 333 if 3 > 2 else 999
# print(X)

# -------------------------------------------------

# while True:
        
#     m = int(input('Enter the mon :'))
#     d = int(input('Enter the day :'))\
#     if 1 <= m and m <= 6:
#         print((m - 1) * 31 + d)
#     elif 7 <= m and m <= 12:
#         print((m - 1) * 30 + 6 + d) 

# -------------------------------------------------

# a = int(input('Enter the mon :'))
# b = int(input('Enter the day :'))

# for i in range(a, b+1):
#     print(a * i)

# ------------------------------------------------
# num = int(input('enter the star number :'))

# for i in range(num):
#     for a in range(i):    
#         print('*', end='')
#     print('')

# for i in range(31):
#     if i%5==0:
#         continue
#     print(i)

# ------------------------------------------------

# str1 = 'sian pirzadeh is good boy'
# print(len(str1))

# for i in str1:
#     print(i)

# list = [21,23,53,664,2334,'sana','amir','mahdi',True,21.34,22.45,'pirzadeh']

# for i in list:
#     if type(i) == int:
#         print(i)


# numbers = [21,23,45,6543,34,413,5314,6543,5432,753]

# for i in numbers:
#     if i > 9 and i < 100:
#         print(i)


# name = input('enter your first name :')

# name = list(name)
# name[0] = (name[0].upper())
# name = ''.join(name)
# print(name)


# list3 = [21,323,412,434123,2,3,2,3,3,3,3,2,2,1,2,4,21]
# list4 = []
# for item in list3:
#     if item not in list4:
#         list4.append(item)

# print(list4)

# tuple1 = (21,332,'sian',324,233,True,322241)

# temp = list(tuple1)
# print(temp)
# temp.remove(21)
# temp.append('pirzadeh')

# tuple1 = tuple(temp)
# print(tuple1)


# tuple2 = ([23,32,432],[213,(231,'sian pirzadeh ',532),321])

# print(tuple2)
# print(tuple2[1])
# print(tuple2[1][1])
# print(tuple2[1][1][1])



# set1 = {21,'sina',312,432,533222,544552,544,3,6,3,5,4,3,3,}

# print(set1)

# set1.add('sian pirzadeh')

# for i in set1:
#     print(i)


# list6 = [123,432,6,42,54,32,2,1,2,2,2,2,2,2,2,2,21,1,11,1,1]
# print(list6)
# list6 = list(set(list6))

# print(list6)



# dect1 = {'id':1,
#     'name':'sina',
#     'family':'pirzadeh',
#     'age':18,
#     'avg':54.33}


# print(dect1.get(1))

# for i in dect1.values():
#     print(i)

    
# for i in dect1.keys():
#     print(i)

    
# for i in dect1.items():
#     print(i)


# -----------------------------------------



# def pack(*args):
#     for i in args:
#         print(i)

# pack(21,432,'sina',231,321,51,23,123,213,'sinta pirzadeh',32)


# fun = lambda x: x * 100

# print(fun(2))


# listfunc = [
#     {'name':'sina','age':18},
#     {'name':'sin','age':13},
#     {'name':'sia','age':15},
#     {'name':'ina','age':17}
# ]

# print(sorted(listfunc,key=lambda dect:dect['age']))



# ----------------------------------------------------

# list1 = [231,321,23,4,1,3,5,23,3]
# print(ord('+'))
# print(sum(list1))
# print(max(list1))
# print(min(list1))
# print(pow(2,30))
# print(abs(-30))
# print(range(1,100))


# -----------------------------------------------------

# list = ['sian','pirzadeh','is','good','boy']

# print('sina'.title())
# print(len('sina'))
# print('sina'.upper())
# print('sina'.lower())
# print('sina pirzadeh is good boy'.split(' '))
# print('-'.join(list))
# print('sina'.startswith('s'))
# print('sina'.endswith('s'))
# print('sina-pirzad  eh is go od boy'.strip())
# print('sina'.ljust(3,'@')+'*')
# print('sina'.rjust(3,'@')+'*')
# print('sina'.center(4,'@')+'*')


# -----------------------------------------------------

# set1 = {12,321,42,421,42,23,0,7,9,5,3,76,5,678,78,9,4}
# set2 = {12,321,4332,41,6,8,4,22,65,96,347,6,43433,948,545,658,75435,644}

# print(set1.difference(set2))
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.issubset(set2))


# -----------------------------------------------------


# dic = {'id':1, 'name':'sina', 'age':18}


# print(dic.get('color'))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.setdefault('color','rad'))


# text1 = 'sian pirzadeh is good boy bot not my lover'
# dicCountChar = {}
# for i in text1:
#     dicCountChar.setdefault(i,0)
#     dicCountChar[i]+=1
# print(dicCountChar)



# -----------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f'{self.name}\n{str(self.age)}'

# per = Person('sina',23)
# print(per)



# import enum 

# class Color(enum.Enum):
#     rad = 1
#     green = 2
#     yellow = 3

# print(Color.green.value)
# print(Color.rad.name)


# -----------------------------------------------------

# file = open('C:/doc/text.txt ','w')
# file.write('sina pirzadeh is good boy')
# file.close()



# numbers = []
# sum_in = 0
# mul = 1

# chos = int(input('enter your numbers of :'))

# for i in range(chos):
#     number = int(input('enter your number :'))
#     numbers.append(number)
#     sum_in += number
#     mul *= number

# print(sum(numbers))
# print(sum_in)
# print(mul)

# ===============================================

# from random import randint

# start = int(input('enter your row number :'))
# matrix = randint(0,1)
# for i in range(start):
#     print(start*f'\t{matrix}\t')
#     start -= 1

# ===============================================

# from random import random,randint


# for i in range(10000):
#     x = randint(1,99999999)
#     tepm = 8 - len(str(x))
#     print(tepm*'0',end='')
#     print(x)

# ===============================================

# names = ['sian','reza','amir','mahdi']
# sortedlist = sorted(names, reverse=True)
# print(sortedlist)

# ===============================================

# list1 = [20,31,42,5,63,7,8,3,2,5,7,5,1,2,2,1,1,2,20,31]
# list2 = []

# for item in list1:
#     if item not in list2:
#         list2.append(item)

# print(list2)

# ===============================================

# num_list = []
# str_list = []

# while user >= 0 or user < 9:
#     user = int(input('Enter the list numbers:'))
#     num_list.append(user)
#     if user != 0:
#         str_list.append(user*'*')

# print(num_list)
# print(str_list)

# ===============================================

# dict1 = {'s':12,'b':13}
# dict2 = {'a':True,'c':False}
# dict3 = dict1 | dict2
# print(dict3) 

# =============================================
# def showStr(text):
#     for i in text:
#         print(i)

# showStr('sina')

# ===============================================

# class Product:
#     def __init__(self, id, name, price) -> None:
#         self.id = id
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         print(f'{self.id}\n{self.name}\n{self.price}')


# class Customer:
#     def __init__(self, id, name, phoneNumber) -> None:
#         self.id = id
#         self.name = name
#         self.phoneNumber = phoneNumber

#     def __str__(self) -> str:
#         print(f'{self.id}\n{self.name}\n{self.phoneNumber}')


# c1 = Customer(1,'sian pirzadeh','09364733583')
# p1 = Product(1,'iphone 14',1000)

# ===============================================



# ============= python bass form sina pirzadeh =================