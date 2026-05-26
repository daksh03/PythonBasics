str=input("Enter String: ")
reversed=""
for item in range(len(str)-1,-1,-1):
    reversed+=str[item]
print(reversed)