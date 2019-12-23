#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

 
import math


side  = {
    'left': 10,
    'front': 10,
    'right':10
    }

def calc_range(msg):
    global side
    side = {
        'left':  min(msg.ranges[180:360]),
        'front':  min(msg.ranges[361:720]),
	'right':  min(msg.ranges[721:900])
    
    }
    
    

def state():
     global side
     dist1=1.2
     dist2=0.75
     if (min(side['left'],side['right']) <= dist2) and (side['left']<side['right']) :
          return 0
     if (min(side['left'],side['right']) <= dist2) and (side['left']>=side['right']) :
          return 1
     elif (min(side['left'],side['right']) > dist2) and (side['left']<side['right'])  and side['front'] <= dist1 :
          return 2
     elif (min(side['left'],side['right']) > dist2) and (side['left']>=side['right'])  and side['front'] <= dist1 :
          return 3
     elif (min(side['left'],side['right']) > dist2) and side['front'] > dist1 :
          return 4

if __name__ == '__main__':
    global vel_msg

    rospy.init_node('base_node')

    vel_msg = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    sub = rospy.Subscriber('/base_scan', LaserScan, calc_range)

    rate = rospy.Rate(500)

    while not rospy.is_shutdown():

       msg = Twist()
       if state() == 0:
            msg.linear.x = 0.3
            msg.angular.z = 0.24

       if state() == 1:
            msg.linear.x = 0.3
            msg.angular.z = -0.24
           
       elif state() == 2:
            msg.angular.z = 1.5
            msg.linear.x = 0.3
       
       elif state() == 3:
            msg.angular.z = -1.5
            msg.linear.x = 0.3
           
       elif state() == 4:
            msg.linear.x = 3
            msg.angular.z = -0.1
            pass

       vel_msg.publish(msg)

       rate.sleep()
