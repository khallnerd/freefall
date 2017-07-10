# This code will calculate the exact solution for a tennis ball
# having been dropped from 600 m

from eulerLoop import eulerLoop

# Initial conditions and physical setup constants
r = 0.033 # Radius of the sphere [m]
data = {
   'angle'  :     90, # Initial angle [deg]
   'v0'     :      0, # Initial (r) velocity [m/s]
   'x0'     :      0, # Initial x position [m]
   'y0'     :    600, # Initial y position [m]
   'D'      :   0.47, # Drag coefficient
   'rho'    :   1.29, # Density of air [kg/m^3]
   'm'      : 0.0585, # Mass of projectile [kg
   'g'      :   -9.8, # Acceleration due to gravity [m/s^2]
   'A'      : np.pi * r ** 2, # Cross-sectional area of projectile [m^2]
   'delta_t':    0.1, # Change in time per iteration [sec]
   't0'     :      0  # Initial time [sec]
   # 't_max':   27.2  # Final time in seconds
   }
   
# Run euler loop
eulerLoop(data)
