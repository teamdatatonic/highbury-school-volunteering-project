

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
