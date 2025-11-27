#FASOLA OMOGBOLAHAN GODSFAVOUR BHU/25/04/05/0020
print("Welcome to the physics calculator")
print("formula a; Speed = Distance / Time")
print("formula b; Force = Mass * Acceleration")
print("formula c; Pressure = Force / Area")
print("formula d; Work done = Force * Distance")
print("formula e; Density = Mass / Volume")
print() #in order to make blank line 
print("in order to use the formulea, input using alphabets such as: a, b, c....")
print() #in order to create blank line
z = input("what formula do you want to use?: ")
if z == ("a"):
    print("Speed = Distance / Time")
    a = float(input("Input Distance: "))
    b = float(input("Input Time: "))
    print(str(a / b) + str(" m/s"))

elif z == ("b"):
    print("Force = Mass * Acceleration")
    c = float(input("Input Mass: "))
    d = float(input("Input Acceleration: "))
    print(str(c * d) + str(" N"))

elif z == ("c"):
    print("Pressure = Force / Area")
    e = float(input("Input Force: "))
    f = float(input("Input Area: "))
    print(str(e / f) + str(" N/m^2"))

elif z == ("d"):
    print("Work done = Force * Distance")
    g = float(input("Input Force: "))
    h = float(input("Input Distance: "))
    print(str(g * h) + str(" J"))

elif z == ("e"):
    print("Density = Mass / Volume: ")
    i = float(input("Input Mass: "))
    j = float(input("Input VOlume: "))
    print(str(i / j) +  str(" kg/m^3"))

else:
    print("FORMULA IS NOT ON THIS SYSTEM")
