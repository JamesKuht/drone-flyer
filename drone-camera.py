###### This script is to initialise the drone (once you've connected to it by wifi)
###### then to turn on it's camera

from djitellopy import Tello
import cv2
import time

##########################################
width = 640  # width of the image
height = 480
startCounter = 1  # if you don't want drone to fly then put 1, if you do, put 0
##########################################

# Connect to tello & initialise all of the velocities to zero, for obvious reasons
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

# Check batter level to ensure ready for flight
print(me.get_battery())

# Get the camera on
me.streamoff()
me.streamon()

# Main loop for flying
while True:

    # Get the image from tello
    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    # Show the image
    cv2.imshow("MyResult", img)

    # Wait for the q button to stop (of note, you need to have waitKety defined before imshow will work)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break

