import math
import random

npoints = 16

points_in = 0
points_out = 0

x_in = []
x_out = []
y_in = []
y_out = []

for i in range(npoints):

    x = random.random()
    y = random.random()

    if y > math.pi*(0.5*x)**2 and y < math.pi*(1*x)**2:
        points_in += 1
        x_in.append(x)
        y_in.append(y)

    else:
        points_out += 1
        x_in.append(x)
        y_in.append(y)

area_computed = (points_in/npoints)*4

area_actual = math.pi*1**2-math.pi*0.5**2

print("The computed area of the donut is", area_computed)

print("The actual area of the donut is", area_actual)

print("The calculated error is", abs(area_computed-area_actual)/area_actual)
