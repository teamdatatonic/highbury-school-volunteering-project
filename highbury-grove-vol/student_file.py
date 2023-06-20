
#Task 1
#Ignore the top line
#Once this code has run it will go back to the beginning and rerun continously

# Open the world called task1_move.wbt
def task1_move(): 

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    left_speed = 10
    right_speed = 10

    #Print the wheel speeds
    print("-----------------------")
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    #Give these speeds to the robot 
    return left_speed, right_speed


# Open the world called task2a_turning.wbt
def task2a_turning():

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    left_speed = 10
    right_speed = -10

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
    left_speed = 10
    right_speed = 8.9

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
    left_speed = 8.9
    right_speed = 10

    #Print the wheel speeds
    print("-----------------------")
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed
    
    
   # Open the world called task3a_collision_detection.wbt
def task3a_collision_detection(left_distance_sensor, right_distance_sensor):

    #--------------WRITE-ANSWER-BELOW----------------------

    #Set the wheel speeds
    if left_distance_sensor<10 and right_distance_sensor<10:
        left_speed = 0
        right_speed = 0
    else:
        left_speed = 10
        right_speed = 10

    #Print the wheel speeds
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
    
    #Print the wheel speeds
    print("-----------------------")
    print(" left_light_sensor : ", left_light_sensor)
    print(" right_light_sensor : ", right_light_sensor)
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed
    
    
    
    
    
    # Open the world called task4_show_love.wbt
def task4_show_love(left_light_sensor, right_light_sensor):

    #--------------WRITE-ANSWER-BELOW----------------------

        
    left_speed = 10-left_light_sensor
    right_speed = 10-right_light_sensor
    
    #Print the wheel speeds
    print("-----------------------")
    print(" left_light_sensor : ", left_light_sensor)
    print(" right_light_sensor : ", right_light_sensor)
    print(" left_speed : ", left_speed)
    print(" right_speed: ", right_speed)

    #-------------WRITE-ANSWER-ABOVE----------------------

    return left_speed, right_speed