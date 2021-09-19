#what is a car
cars = 100
#how much space does a car have
space_in_a_car = 4.0
#how many drivers and passengers
drivers = 30
passengers = 90
#how many cars are NOT driven
cars_not_driven = cars - drivers
#each driver has to have a car
cars_driven = drivers
#how much space do we have?
carpool_capacity = cars_driven * space_in_a_car
#about how many passengers per car?
average_passengers_per_car = passengers / cars_driven

#tells user how many cars and drivers are available
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
 #tell user How many cars will be empty
print("There will be", cars_not_driven, "empty cars today.")
#tells user how many people can be transported
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
