#This code will calculate the exact solution for Felix Baumgarter
#in free fall from 100,00 ft using Euler's method including drag.

#Import numerical and plotting packages
import numpy as np
import matplotlib.pyplot as plt


#Initial conditions and physical setup constants
angle=90
v0=0
vx0=v0*np.cos(np.deg2rad(angle)) #initial x velocity in m/s
vy0=v0*np.sin(np.deg2rad(angle)) #initial x velocity in m/s
x0=0 #Initial x position in m
y0=30480 #initial y position in m
D=1.5 #Drag coefficient
#r=.75 #radius of sphere in m
p=1.29 #density of air in kg/m^3
m=118.0 #mass of projectile in kg
g=-9.8 #acceleration caused by gravity in m/s^2
A=0.25 #Area of the projectile in m^2

#Set up the time steps and number of calculations
delta_t=0.1 #time step in seconds
t0=0 #start time in seconds
'''t_max = 445.8 #final time in seconds

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

	#increment velocity
	v=np.sqrt(vx[-1]**2+vy[-1]**2)
	#find the current vertical acceleration
	ay=g-(1/2*D*p*A*v*vy[-1])/m
	#The current horizontal acceleration
	ax=(-1/2*D*p*A*v*vx[-1])/m
	
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



"""#Plot the results
plt.plot(t,y,linewidth=2, color='red')
plt.xlabel('Time (s)')
plt.ylabel('Vertical Position (m)')
plt.title('Position of Felix')

#Save the plot
plt.savefig('Felix_drag.pdf')"""
