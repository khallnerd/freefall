# This code will calculate the exact solution for Felix Baumgarter
# in free fall from 100,00 ft using Euler's method including drag.

from eulerLoop import eulerLoop

# Initial conditions and physical setup constants
# r = .75 # Radius of sphere [m]
data = {
   'angle'  :     90, # Initial angle [deg]
   'v0'     :      0, # Initial (r) velocity [m/s]
   'x0'     :      0, # Initial x position [m]
   'y0'     :  30480, # Initial y position [m]
   'D'      :    1.5, # Drag coefficient
   'rho'    :   1.29, # Density of air [kg/m^3]
   'm'      :  118.0, # Mass of projectile [kg]
   'g'      :   -9.8, # Acceleration due to gravity [m/s^2]
   'A'      :   0.25, # Area of projectile [m^2]
   'delta_t':    0.1, # Change in time per iteration [sec]
   't0'     :      0  # Initial time [sec]
   # 't_max':  445.8  # Final time in seconds
   }
   
# Run euler loop
eulerLoop(data)
