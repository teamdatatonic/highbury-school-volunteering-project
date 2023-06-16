"""braitenberg_vehicle controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

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
     
    #Enable sensors
    distance_sensors = []
    distance_sensor_names = ['ds_left', 'ds_right']

    light_sensors = []
    light_sensor_names = ['ls_left', 'ls_right']

    for i in range(2):
        #append sensor names to sensor list using the getDevice method
        distance_sensors.append(robot.getDevice(distance_sensor_names[i]))
        light_sensors.append(robot.getDevice(light_sensor_names[i]))
        #for each sensor enable timestep
        distance_sensors[i].enable(timestep)
        light_sensors[i].enable(timestep)   
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    prev_left_light = 0
    prev_right_light = 0
    while robot.step(timestep) != -1:

        left_distance_sensor_val = distance_sensors[0].getValue()/100
        right_distance_sensor_val = distance_sensors[1].getValue()/100

        left_light_sensor_val = light_sensors[0].getValue()/100
        right_light_sensor_val = light_sensors[1].getValue()/100


        #Below is where you should write your answer
        #--------------------------
        
        #Set variables

        
        
        if left_light_sensor_val < prev_left_light or left_distance_sensor_val + right_distance_sensor_val < 15:
            # spin
            left_speed = -10
            right_speed = 10
        elif right_light_sensor_val < prev_right_light:
            left_speed = 10
            right_speed = -10
        else:
            left_speed = 7
            right_speed = 7
        
        prev_left_light = left_light_sensor_val
        prev_right_light = right_light_sensor_val

    
        # Change the speeds of each wheel. We change them to the values stored above
        wheels[0].setVelocity(left_speed)
        wheels[2].setVelocity(left_speed)

        wheels[1].setVelocity(right_speed)
        wheels[3].setVelocity(right_speed)

        print("-----------------------")
        print(" left_distance_sensor_val: {}".format(left_distance_sensor_val))
        print(" right_distance_sensor_val: {}".format(right_distance_sensor_val))
        print(" left_light_sensor_val: {}".format(left_light_sensor_val))
        print(" right_light_sensor_val: {}".format(right_light_sensor_val))
        print(" left_speed : {}".format(left_speed))
        print(" right_speed: {}".format(right_speed))
        
        #--------------------------

    
    # Enter here exit cleanup code.
if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    run_robot(robot)
