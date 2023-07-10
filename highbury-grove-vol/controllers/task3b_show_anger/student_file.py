


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
