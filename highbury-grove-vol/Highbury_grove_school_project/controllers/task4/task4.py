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
    

    distance_sensors = []
    distance_sensor_names = ['ds_left', 'ds_right']

    for i in range(2):
        #append light sensor names to light sensor list using the getlightsensor method
        #light_sensors.append(robot.getDevice(light_sensor_names[i]))
        distance_sensors.append(robot.getDevice(distance_sensor_names[i]))
        #for each light sensor enable timestep
        #light_sensors[i].enable(timestep)   
        distance_sensors[i].enable(timestep)
    # get the time step of the current world.
    # timestep = int(robot.getBasicTimeStep())
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
     # motor = robot.getDevice('motorname')
     # ds = robot.getDevice('dsname')
     # ds.enable(timestep)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        left_distance_sensor_val = distance_sensors[0].getValue()/100
        right_distance_sensor_val = distance_sensors[1].getValue()/100
        
        stop = False

        if left_distance_sensor_val<10 and right_distance_sensor_val<10:
            left_speed = 0
            right_speed = 0
            stop = True
        elif stop == True:
            left_speed = 0
            right_speed = 0
        else:
            left_speed = 10
            right_speed = 10


    
            
 
        
        print("-----------------------")
        print(" left_sensor_val: {}".format(left_distance_sensor_val))
        print(" right_sensor_val: {}".format(right_distance_sensor_val))
        print(" left_speed : {}".format(left_speed))
        print(" right_speed: {}".format(right_speed))
        print(" stop (True/False): {}".format(stop))
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        wheels[0].setVelocity(left_speed)
        wheels[2].setVelocity(left_speed)
        wheels[1].setVelocity(right_speed)
        wheels[3].setVelocity(right_speed)
        
    
    # Enter here exit cleanup code.
if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    run_robot(robot)
