myCars = [ 'tata', 'maruti', 'bmw', 'toyota', 'kai', 'audi', 'lamorghini', 'bugati', 'mercedes', 'ferrari', 'porsche', 'bentley']

# print(type(myCars))

# myCars = 5
# print(type(myCars))
#
# myCars = 'Debajyoti'
# print(type(myCars))
#
# myCars = False
# print(type(myCars))
#
# myCars = { 
#         'name': 'Debajyoti', 
#         'age' : 16
#         }
# print(type(myCars))

available_cars = [ 'tata', 'maruti']



# print(myCars[1])

# your_car = input("Enter your car brand :")
#
# if your_car == myCars[1]:
#     print("Available ! ")
# else:
#     print("Not Available")


# print(len(myCars))

# print(myCars[-1])

# print(myCars[:7])

# new_list = myCars[:7]
#
# print(myCars)
# print(new_list)



# print(myCars)

myCars.append('honda')


# print(myCars)

myCars.insert(2, 'suzuki')

# print(myCars)

# print(len(myCars))

available_cars.append(myCars[-1])
available_cars.append(myCars[2])
available_cars.append(myCars[9])

# print(available_cars)
# print(available_cars[0].upper())

available_cars.remove("tata")
available_cars.pop()

# print(available_cars)
#
# print(available_cars[0].upper())

your_car = input("Enter your car brand :")

for car in myCars:
    if your_car.lower() == car.lower():
        print("Available ! ")
    else:
        print("Not Available")



# l = myCars.index("mercedes")
# print(l)





