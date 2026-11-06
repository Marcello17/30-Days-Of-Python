list = list(['apple','banana','cherry'])

print(list)

# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']

list3 = list1 + list2

print(list3)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

person = {
    "name": 'Marcello',
    "age": 28,
    "Magic Weekends": ['Alex', 'Daniel', 'Brad', 'Dominque', 'Marcello']
}

print(person['name'])
print(person['age'])
print(person['Magic Weekends'][2])