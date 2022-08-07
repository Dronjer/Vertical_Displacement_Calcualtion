# calculating the vertical displacement for a cantilever beam having point load at one end
# The value of E is taken for the steel
# The vertical displacement is calculated for equal 10 points in the given length
E = 190e3
# Calculating the moment of inertia
print("enter the width of the beam")
b = float(input())
print("enter the height of the beam")
h = float(input())
I = (b*(h**3))/12
print("the moment of inertia of the given beam is", I)
print("Enter the length of the fiber in millimeter :")
l = int(input())
L  = int(l/20)
# The length need to be divided into 20 evenly spaced points
P = (5000, 10000, 15000, 20000, 25000, 30000)
for j in P:
    print("The value of load is:", j)
    for i in range (0,l,L):
        print(i)
        # Delefection for the beam
        y = ((j*i**3)/6 + (j*l**3*i)/2 - (j*l**3)/3)*(1/(E*I))
        # The value of E and I also needed to be added
        print("The value for deflection is :", y)



