# Intro to the folders
Every task has its own function and world.
At the start of each task, you should load the world for that task. 
To do this, in the Webots program, do:

`File -> Open World -> [pick the world with the right task number]`

If you don't see the worlds, they should be in the following folder:
highbury-school-volunteering-project -> highbury-grove-vol -> worlds

*Note: change this path if we rename the folders :)*

On the right hand side of the program is where the code is kept. This code is what moves the robot and will be what you should change to complete the tasks. If this file isnt there, or you acceidently close it, you can reopen it by doing:

`Tools -> Text Editor`

The file is located in this location:

`highbury-school-volunteering-project -> highbury-grove-vol -> student_file.py`

If you accidently change the view of the camera in the world, you can easily get it back by doing: 

`Control + Shift + V`

Or by hitting the button on the program with arrows circling an eye.

*Note: Maybe add image?*

*Note: Write about where to change the code, ie only change the code inside the functions, dont mess with the function names or returns.*

Finally, make sure not to hit 'Save World' as this will overwrite the world that you are using. To make sure this doesnt happen, make a copy of the folder and store it somewhere else and then you can replace it if you change anything accidently.

# Install packages
`pip install controller`


# Task 1 - Moving
- Get the robot to move in a straight line.
- How could you get it to go at a different speed?


# Task 2a - Turning
- Get the robot to move in a circle
- Is there a way that you can change the size of the circle?
- How about making it go the other way around?

# Task 2b - Turning clockwise
- Now can you make the robot turn clockwise whilst staying on the rounabout road?

# Task 2c - Turning anticlockwise
- How about turning on the roundabout in an anticlockwise circle?


# Task 3a - Collision Detection
- Now we introduce a type of sensor onto the robot. They are called distance sensors and there are two located on the front face of the robot. They are named 'ds_left' and 'ds_right'. When printing out the values of these sensors they will always output 10 until they get close to an obstacle. Then the values will start to decrease.

- Can you get the robot to stop before it hits the crash barrier?
(you may need to use an if statement)
- How would you get it to stop at a different point to the barrier? (i.e. closer or farther away)
- Think about how this could be applied to real-life

# Task 3b - Show anger
- There is a new sensor! Now we are introducing a light sensor. This is similar to the distance sensor, there are two of them (i.e a left and right) in the same location as the distance sensors and their values range between 0 and 10. The more light they detect the higher the value the sensor outputs. 
- There are now lights on the robot arena. They have no physical presence, so the distance sensors will not be able to detect them.
- Here is the code we came up with for the robot to use the light and show anger
- How might you have done differently?
- Can you see how the robot is using the light sensors?

# Task 3c - show fear
- Now we give out interpretation of how a robot might display fear
- What would you do, would you do it similarly or in a different way to us?

# Task 4 - Show love
- Now it is your turn.
- Use the light sensors and try and get the robot to show love


# Task 5 - Research and Present Your Findings
1. Research the applications of this technology
a) One interesting fact about automated vehicles
b) Any pro’s and con’s - think about the environment, accessibility for everyone in society, costs, road accidents

2. Near future applications on this type of technology (add video on Artificial Intelligence and Robotics) - how do you think this technology will change our world? Do you think it will have a positive or negative impact on society?  

3. What can you imagine we could use this type of technology for in 100 years - think about how it’s being used now, how it’s planned on being in the future, and what you would do differently. How could it improve the world we live in?  
