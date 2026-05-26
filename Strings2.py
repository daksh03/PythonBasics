the_string="North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
centre_plus=the_string.center(16,"+")
print(centre_plus)
print(the_string.lstrip("North"))
print(centre_plus.rstrip("+"))
print(centre_plus.strip("+"))
print(the_string.replace("North","South"))