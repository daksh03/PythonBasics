c=int(input("Enter celsius "))

def fahrenheit(celsius):
    return round((1.8 * celsius + 32),1)

print ("The Fahrenheit equivalent of " + str(c) + " degrees Celsius is " + str(fahrenheit(c)) + ".")