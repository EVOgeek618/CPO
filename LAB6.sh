#!/bin/bash

gnome-terminal --window -- roscore
sleep 2

gnome-terminal --tab -- rosrun turtlesim turtlesim_node
sleep 2
#2
rosservice call /kill turtle1
rosservice call /spawn -- 0 7.125 1.57 'tr1'
rosservice call /tr1/set_pen -- 255 255 255 1 off
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.7475,0.0,0.0]' '[0.0,0.0,-3.14]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,-0.401]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[4.48,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.971]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[1.75,0.0,0.0]' '[0.0,0.0,0.0]'
#4
rosservice call /tr1/set_pen -- 69 89 255 1 off
rosservice call /tr1/teleport_absolute -- 1.85 8 -1.57
rosservice call /tr1/set_pen -- 255 255 255 1 off
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.5,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.57]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[1.75,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.57]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.5,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,-3.14]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[5,0.0,0.0]' '[0.0,0.0,0.0]'
#3
rosservice call /tr1/set_pen -- 69 89 255 3 off
rosservice call /tr1/teleport_absolute -- 4 8 0
rosservice call /tr1/set_pen -- 255 255 255 1 off
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[3.927,0.0,0.0]' '[0.0,0.0,-3.14]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,3.14]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[3.927,0.0,0.0]' '[0.0,0.0,-3.14]'
#9
rosservice call /tr1/set_pen -- 69 89 255 3 off
rosservice call /tr1/teleport_absolute -- 7.1 7.125 -1.57
rosservice call /tr1/set_pen -- 255 255 255 1 off
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[5.498,0.0,0.0]' '[0.0,0.0,-6.28]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[3.25,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.749,0.0,0.0]' '[0.0,0.0,-3.14]'
#5
rosservice call /tr1/set_pen -- 69 89 255 3 off
rosservice call /tr1/teleport_absolute -- 8.95 8 -3.14
rosservice call /tr1/set_pen -- 255 255 255 1 off
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[1.75,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.57]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.5,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.57]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[3.927,0.0,0.0]' '[0.0,0.0,-3.14]'
#4_2
rosservice call /tr1/set_pen -- 69 89 255 3 off
rosservice call /tr1/teleport_absolute -- 9.25 8 -1.57
rosservice call /tr1/set_pen -- 255 255 255 1 off
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.5,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.57]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[1.75,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,1.57]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[2.5,0.0,0.0]' '[0.0,0.0,0.0]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[0.0,0.0,-3.14]'
rostopic pub -1 /tr1/cmd_vel geometry_msgs/Twist -- '[5,0.0,0.0]' '[0.0,0.0,0.0]'

