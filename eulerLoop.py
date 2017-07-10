import numpy as np
import matplotlib.pyplot as plt

# Euler method function
def eulerLoop(data):
   # Extract data for initial conditions
   angle   = data['angle']   # Initial angle [deg]
   v0      = data['v0']      # Initial (r) velocity [m/s]
   vx0     = v0 * np.cos(np.deg2rad(angle)) # Initial x velocity [m/s]
   vy0     = v0 * np.sin(np.deg2rad(angle)) # Initial y velocity [m/s]
   x0      = data['x0']      # Initial x position [m]
   y0      = data['y0']      # Initial y position [m]
   D       = data['D']       # Drag coefficient
   rho     = data['rho']     # Density of air [kg/m^3]
   m       = data['m']       # Mass of projectile [kg]
   g       = data['g']       # Acceleration due to gravity [m/s^2]
   A       = data['A']       # Cross-sectional area of projectile [m^2]
   delta_t = data['delta_t'] # Change in time per iteration [sec]
   t0      = data['t0']      # Initial time [sec]
   
   '''
   t_max   = data['t_max']   # Final time in seconds
   # Calculate the number of time steps we need to make
   N = (t_max - t0) / delta_t

   # Making N an integer
   N = int(N)
   '''

   # Define array of data used for looping
   v       = [v0]            # Array of velocities
   ay      = []              # Array of y-accelerations
   ax      = []              # Array of x-accelerations
   vx      = [vx0]           # Array of x-velocities
   vy      = [vy0]           # Array of y-velocities
   x       = [x0]            # Array of x-positions
   y       = [y0]            # Array of y-positions
   t       = [t0]            # Array of times
   
   # Begin the Euler loop
   while y[-1] > 0:
      # Increment velocity
      v  = np.sqrt(vx[-1] ** 2 + vy[-1] ** 2)
      # Find the current y-acceleration
      ay = g - (1/2 * D * rho * A * vy[-1] ** 2) / m
      # Find the current x-acceleration
      ax = (-1/2 * D * rho * A * vx[-1] ** 2) / m
      
      # Find the next y-velocity
      vy.append(vy[-1] + ay * delta_t)
      # Find the next x-velocity
      vx.append(vx[-1] + ax * delta_t)
      # Find the next y-position
      y.append(y[-1] + vy[-1] * delta_t)
      # Find the next x-position
      x.append(x[-1] + vx[-1] * delta_t)
      # Increment time
      t.append(t[-1] + delta_t)

   # End of Euler loop
   
   # Print the results
   print('time', '%.2f' % t[-1])
   # print ('horizontal velocity', "%.2f" % vx[-1]) 
   print('vertical velocity', '%.2f' % vy[-1])
   # print ('magnitude of velocity', "%.2f" % v)
   # print ('horizontal position', "%.4f: %  x[-1]) 
   print('vertical position', '%.4f' % y[-1])
   
   '''
   # Plot the results
   plt.plot(x, y, linewidth = 2, color = 'red')
   plt.xlabel('Horizontal Position (m)')
   plt.ylabel('Vertical Position (m)')
   plt.title('Position of a projectile w/ drag')

   # Save the plot
   plt.savefig('Lab_7_plot_drag.pdf')
   '''

# End of Euler function
