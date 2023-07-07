
#Task 1

#Once this code has run it will go back to the beginning and rerun continously

# Open the world called task1_move.wbt
def task1_move(): 

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    left_speed = 0 # Try changing these numbers
    right_speed = 0

    #Print the wheel speeds
    print("-----------------------")
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    #Give these speeds to the robot 
    return left_speed, right_speed


# Task 2 

# Open the world called task2a_turning.wbt
def task2a_turning():

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    left_speed = 0
    right_speed = 0

    #Print the wheel speeds
    print("-----------------------")
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------
    return left_speed, right_speed



# Open the world called task2b_clockwise.wbt
def task2b_clockwise():

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    left_speed = 0
    right_speed = 0

    #Print the wheel speeds
    print("-----------------------")
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------
    return left_speed, right_speed




# Open the world called task2c_anticlockwise.wbt
def task2c_anticlockwise():

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    left_speed = 0
    right_speed = 0

    #Print the wheel speeds
    print("-----------------------")
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed
    
# Task 3

# Open the world called task3a_collision_detection.wbt
def task3a_collision_detection(left_distance_sensor, right_distance_sensor):

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    if left_distance_sensor<10 and right_distance_sensor<10:
        # This will run when the robot senses something close
        left_speed = 0
        right_speed = 0
    else:
        # This will run when the robot doesn't sense anything close
        left_speed = 0
        right_speed = 0

    #Print the wheel speeds and the distance sensor values
    print("-----------------------")
    print(" left_distance_sensor : ", left_distance_sensor)
    print(" right_distance_sensor : ", right_distance_sensor)
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed


# Open the world called task3b_show_anger.wbt
def task3b_show_anger(left_light_sensor, right_light_sensor):

    #--------------WRITE-ANSWER-BELOW----------------------

    left_speed = right_light_sensor
    right_speed = left_light_sensor
    # We want the left wheels to get faster when there is more light on the right side
    # (i.e. curving the wheel towards the light)
    # And vice versa for the right wheel speed - we want it to speed up
    # if there is light on the left hand side
        

    #Print the wheel speeds
    print("-----------------------")
    print(" left_light_sensor : ", left_light_sensor)
    print(" right_light_sensor : ", right_light_sensor)
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed

    # Open the world called task3c_show_fear.wbt
def task3c_show_fear(left_light_sensor, right_light_sensor):

    #--------------WRITE-ANSWER-BELOW----------------------

    left_speed = 10-right_light_sensor
    right_speed = 10-left_light_sensor

    # We wanted the opposite of what was happening for anger.
    # We wanted the robot to move away from the light
    # To do this we inverted the values from the anger code by 
    # taking them away from 10. Then a high number for anger meant
    # a low number for fear, and vice versa.

    # If there was lots of light on the right, we want the left wheels
    # to slow down so it turns left - away from the light.
    # Similarly for light on the left of the robot, we wanted the right
    # wheels to slow down.
    
    #Print the wheel speeds
    print("-----------------------")
    print(" left_light_sensor : ", left_light_sensor)
    print(" right_light_sensor : ", right_light_sensor)
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed
    
    
    
# Task 4
    
# Open the world called task4_show_love.wbt
def task4_show_love(left_light_sensor, right_light_sensor):

    #--------------WRITE-ANSWER-BELOW----------------------

        
    left_speed = 0
    right_speed = 0
    
    #Print the wheel speeds
    print("-----------------------")
    print(" left_light_sensor : ", left_light_sensor)
    print(" right_light_sensor : ", right_light_sensor)
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed