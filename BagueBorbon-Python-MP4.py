# -*- coding: utf-8 -*-


import math
import numpy as np
import matplotlib.pyplot as plt

yo = float(input('What is the initial height of the projectile above the ground in meters (m)? '))
vo = float(input('What is the magnitude of the velocity in meters per second (m/s)? '))
angle = float(input('The angle (in degrees) with respect to the positive x-axis at which the projectile is fired: '))
ax = float(input('What is the x-component of the acceleration, considering the sign, (in m/s/s)? '))
ay = float(input('What is the y-component of the acceleration, considering the sign, (in m/s/s)? '))
theta = math.radians(angle)

if ay != 0:
  vox = vo*math.cos(theta); 
  voy = vo*math.sin(theta);
  if yo == 0:  #on a level ground
      vy = -voy #since y-component of the final velocity is the same as the initial velocity, but opposite in direction
      t = (vy-voy)/ay
      t = np.linspace(0,t,10)
      y = (voy*t) + (0.5*ay*t**2)
      x = (vox*t) + (0.5*ax*t**2)
      plt.plot(x,y)
      plt.grid()
      plt.xlabel('Range')
      plt.ylabel('Height')
      plt.title('Trajectory of a Projectile')
  else:
      yf = (vo**2*(math.sin(theta))**2)/(2*abs(ay)) #solving for max height
      t = (-voy + math.sqrt((voy**2) - (4*0.5*abs(ay)) * (yo-yf)))/(abs(ay)) #using quadratic formula to find the time
      t = np.linspace(0,t,10) 
      y = yo + (voy*t) + (0.5*ay*t**2)
      x = (vox*t) + (0.5*ax*t**2)
      plt.plot(x,y)
      plt.grid()
      plt.xlabel('Range')
      plt.ylabel('Height')
      plt.title('Trajectory of a Projectile')

else: raise ValueError('If the vertical acceleration is zero, then there would be no free fall!')
    
    

