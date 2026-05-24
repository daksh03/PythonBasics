from random import randint
gallons=randint(10,25)
miles=randint(200,400)
print("The car can travel " + str(miles // gallons) + " miles per gallon.")
print("The car's fuel tank can hold " + str(gallons) + " gallons.")
print("The car can travel " + str(miles) + " miles on a full tank.")

