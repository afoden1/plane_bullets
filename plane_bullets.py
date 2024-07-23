#This code is being written to answet the question "Why do you need to aim behind a plane moving perpendicular to you?" posed on TIKTOK

import math
import numpy as np
import matplotlib.pyplot as plt

#Set variables

#Generate a linear time variable
time = np.linspace(0,15,500)

Plane_speed = 107 #m/s
Bullet_speed = 340 #m/s
aim_angle = 60 #degrees

#convert to radians
aim_angle_rads = aim_angle*math.pi/180

#Initialise for loop
ii=0
x_aiming= []
x_moving = []
y_dist = []

while ii < len(time):
    x_aiming_temp = Bullet_speed*time[ii]*math.cos(aim_angle_rads)
    x_moving_temp = Bullet_speed*time[ii]*math.cos(aim_angle_rads) + Plane_speed*time[ii]
    y_dist_temp = Bullet_speed*time[ii]*math.sin(aim_angle_rads)

    x_aiming.append(x_aiming_temp)
    x_moving.append(x_moving_temp)
    y_dist.append(y_dist_temp)

    ii += 1

x_aiming = np.array(x_aiming)
x_moving = np.array(x_moving)
y_dist = np.array(y_dist)

plt.plot(x_aiming, y_dist, color = 'red')
plt.plot(x_moving, y_dist, color = 'blue')

plt.show()

