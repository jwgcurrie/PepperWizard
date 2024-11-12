import pygame 
import time


def InitialiseController():
    try:
        pygame.init()
        pygame.joystick.init()
        controller = pygame.joystick.Joystick(0)
        controller.init()
        print("SUCCESS: InitialiseController() - Controller Initialised")
        return controller
    except:
        print("WARNING: InitialiseController() - Failed to detect games controller")
        print("WARNING: Please check that games controller is connected via USB or Bluetooth")
        print("WARNING: PepperWizard will have to be restarted to use this functionality")
        return False
    

def JoystickMove(controller, button_state, button_timer):
    button_timeout = 0.1
    joy_command = [0, 0, 0, 0]
    try:
        for event in pygame.event.get():
            Controller_Left_X = controller.get_axis(pygame.CONTROLLER_AXIS_LEFTX)
            Controller_Left_Y = controller.get_axis(pygame.CONTROLLER_AXIS_LEFTY)
            Controller_Right_X = controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTX)
            Controller_Right_Y = controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTY)
            
            joy_command = [Controller_Left_X, Controller_Left_Y, Controller_Right_X, Controller_Right_Y]
            
            for i, command in enumerate(joy_command):
                joy_command[i] = round(command, 1)

            but_X = controller.get_button(0)
            but_C = controller.get_button(1)
            but_S= controller.get_button(2)
            but_T = controller.get_button(3)

            button_pressed = [but_X, but_C, but_S, but_T]

            for i, button in enumerate(button_pressed):
                time_elapsed = time.time() - button_timer[i]
                button_timer[i] = time.time()
                
                if button > 0 and (time_elapsed > button_timeout):
                    button_state[i] = not button_state[i]
            


    except Exception as error:
        print(error)
    
    return joy_command, button_state, button_timer

    


def MotionMapping(joy_command, v_x, v_theta):
    command_x = -joy_command[1] * v_x
    command_y = -joy_command[0] * v_x
    command_theta = joy_command[2] * v_theta
 
    print(command_x, command_y, command_theta)
    

controller = InitialiseController()
button_state = [False, False, False, False]
button_timer = [0, 0, 0, 0]

while True:
    joy_command, button_state, button_timer = JoystickMove(controller, button_state, button_timer)
    
    try:
        MotionMapping(joy_command, v_x = 0.15, v_theta = 0.5)

    except Exception as error:
        print(error)