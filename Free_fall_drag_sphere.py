#This code will calculate the exact solution for a spherical rock
#having been dropped from 600 m
#Import numerical and plotting packages
import numpy as np
import matplotlib.pyplot as plt


#Initial conditions and physical setup constants
angle=90
v0=0
vx0=v0*np.cos(np.deg2rad(angle)) #initial x velocity in m/s
vy0=v0*np.sin(np.deg2rad(angle)) #initial x velocity in m/s
x0=0 #Initial x position in m
y0=600 #initial y position in m
D=0.47 #Drag coefficient
r=0.042 #radius of sphere in m
p=1.29 #density of air in kg/m^3
m=1.00 #mass of projectile in kg
g=-9.8 #acceleration caused by gravity in m/s^2
A=np.pi*r**2 #Area of the projectile

#Set up the time steps and number of calculations
delta_t=0.1 #time step in seconds
t0=0 #start time in seconds
'''t_max = 13.0 #final time in seconds

#Calculate the number of time steps we need to make
N=(t_max-t0)/delta_t

#Making N an integer
N=int(N)'''

#Make lists to hold positions, velocities, and time
x=[x0]
y=[y0]
vx=[vx0]
vy=[vy0]
t=[t0]
v=[v0]

#Now perform an Euler's method calculation
while y[-1] > 0:

	#find the current vertical acceleration
	ay=g+(1/2*D*p*A*vy[-1]**2)/m
	#The current horizontal acceleration
	ax=(-1/2*D*p*A*vx[-1]**2)/m
	
	#Find the next vertical velocity
	vy.append(vy[-1]+ay*delta_t)
	#the next horizontal velocity
	vx.append(vx[-1]+ax*delta_t)
	#Find the next vertical position
	y.append(y[-1]+vy[-1]*delta_t)
	#The next horizontal position
	x.append(x[-1]+vx[-1]*delta_t)
	
	#increment time
	t.append(t[-1]+delta_t)
	
#End of Euler Loop

#Print the results
print ('time', "%.2f" % t[-1])
#print ('horizontal velocity', "%.2f" % vx[-1]) 
print ('vertical velocity', "%.2f" % vy[-1]) 
#print ('magnitude of velocity', "%.2f" % v)
#print ('horizontal position', "%.4f: %  x[-1]) 
print ('vertical position', "%.4f" % y[-1]) 


'''#Plot the results
plt.plot(x,y,linewidth=2, color='red')
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.title('Position of a projectile w/ drag')

#Save the plot
#plt.savefig('Lab_7_plot_drag.pdf')'''
