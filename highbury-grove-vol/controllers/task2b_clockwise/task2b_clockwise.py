"""braitenberg_vehicle controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import sys
rep1, rep2 = sys.path[0].split("/")[-2:]
print(rep1)
sys.path.insert(1, sys.path[0].replace(rep1+'/'+rep2, ""))
from student_file import task2b_clockwise

timestep = 64
maxspeed = 10

def run_robot(robot):
    
    #Enable motors
    wheels = []
    wheel_names = ['wheel1', 'wheel2', 'wheel3','wheel4']
    
    for i in range(4):
       #append robot wheel names to wheel list
        wheels.append(robot.getDevice(wheel_names[i]))
        #set position of each value in the wheels list 
        wheels[i].setPosition(float('inf'))
        #set velocity of each value in the wheels list 
        wheels[i].setVelocity(0.0)
     
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:

        #Below is where you should write your answer
        #--------------------------

        #Explore
        left_speed, right_speed = task2b_clockwise()
            
        # Change the speeds of each wheel. We change them to the values stored above
        wheels[0].setVelocity(left_speed)
        wheels[2].setVelocity(left_speed)

        wheels[1].setVelocity(right_speed)
        wheels[3].setVelocity(right_speed)

    
    # Enter here exit cleanup code.
if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    run_robot(robot)
