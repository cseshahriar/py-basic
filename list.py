import re 
# list 
cars = ['honda', 'bmw', 'audi', 1213]
print(cars)

# 2d list 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [0, 0, 0, 0]
]

for x in matrix:
    for y in x:
        print(y, end=' ')
    print()

# sum of list 
list_of_numbers = [1, 2,'Math', 3, 4, 5]
sum = 0
for num in list_of_numbers:
    if type(num) == int:
        sum += num
print("Sumi s: {sum}".format(sum=sum) )

# insert 

# delete 


# string to list
cars = 'toyota, honda, bmw, audi'
car_list = re.split(',', cars)
print(car_list)