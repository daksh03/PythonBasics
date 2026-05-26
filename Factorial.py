# num=int(input("Enter number "))

def fact_number(number):
    returned=1
    
    for item in range(number,1,-1):
        returned*=item
    
    return returned

print(fact_number(3))
print(fact_number(4))
print(fact_number(5))