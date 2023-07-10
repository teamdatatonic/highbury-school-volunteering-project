


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
    