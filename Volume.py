length=int(input("Enter length "))
width=int(input("Enter width "))
height=int(input("Enter height "))

def volume(l,w,h):
    return l*w*h

print("The volume of the rectangular prism is " + str(volume(length,width,height)) + " cubic feet.")