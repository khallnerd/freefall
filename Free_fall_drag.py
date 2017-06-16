#Two Dimensional projectile Euler Code
#PH 150
#Kaleb Hall
#This code will calculate the exact solution for a projectile
#having been shot from a cannon using Euler's method including drag.

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
A=0.25 #Area of the projectile

#Set up the time steps and number of calculations
delta_t=0.1 #time step in seconds
t0=0 #start time in seconds
t_max = 445.8 #final time in seconds

#Calculate the number of time steps we need to make
N=(t_max-t0)/delta_t

#Making N an integer
N=int(N)

#Make lists to hold positions, velocities, and time
x=[x0]
y=[y0]
vx=[vx0]
vy=[vy0]
t=[t0]
v=[v0]

#Now perform an Euler's method calculation
for i in range(N):

	#increment velocity
	v=np.sqrt(vx[i]**2+vy[i]**2)
	#find the current vertical acceleration
	ay=g-(1/2*D*p*A*v*vy[i])/m
	#The current horizontal acceleration
	ax=(-1/2*D*p*A*v*vx[i])/m
	
	#Find the next vertical velocity
	vy.append(vy[i]+ay*delta_t)
	#the next horizontal velocity
	vx.append(vx[i]+ax*delta_t)
	#Find the next vertical position
	y.append(y[i]+vy[i]*delta_t)
	#The next horizontal position
	x.append(x[i]+vx[i]*delta_t)
	
	#increment time
	t.append(t[i]+delta_t)
	
#End of Euler Loop

#Print the results
print ('time', "%.2f" % t[-1])
#print ('horizontal velocity', "%.2f" % vx[-1]) 
print ('vertical velocity', "%.2f" % vy[-1]) 
print ('magnitude of velocity', "%.2f" % v)
#print ('horizontal position', "%.4f: %  x[-1]) 
print ('vertical position', "%.4f" % y[-1]) 


#Plot the results
plt.plot(x,y,linewidth=2, color='red')
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.title('Position of a projectile w/ drag')

#Save the plot
#plt.savefig('Lab_7_plot_drag.pdf')
