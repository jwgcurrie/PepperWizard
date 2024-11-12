def Launcher(wizard_command):
    if wizard_command in  ['W', 'Wake']:
        print("Launch Wake")
    elif wizard_command in ['S', 'S BR', 'S WB', 'S MC']:
        print("Launch SocialState")
    elif wizard_command in ['R', 'Rest']:
        print("Launch Rest")
    elif wizard_command == 'F':
        print("Launch Find")
    elif wizard_command == 'J':
        print("Launch Joystick")    
    elif wizard_command == 'T':
        print("Launch PepperTalk")
    elif wizard_command == 'AT':
        print("Launch PepperTalk - Animated")
    elif wizard_command == 'Bat':
        print("Launch Battery")
    elif wizard_command in ['H', 'Help', 'help']:
        Helper()
    else:
        print("Command not recognised. Try: \n help")
    return

def UserInput(mode):
    if mode == 'Command':
        user_input = raw_input("Enter Command: ")
    elif mode == 'TTS':
        user_input = raw_input("Pepper: ")
    return user_input

def Helper():
    print("\n PepperWizard is a command line interface for teleoperating the Pepper robot. \n")
    print("commands: ")
    print("--------------------------")
    print("| Wake            | W     | Wakes robot and activates SocialState")
    print("| Rest            | R     | Robot assumes resting posture and motor stiffness set to zero")
    print("| Joystick        | J     | Control robot location with joystick")
    print("| Social          | S     | Turns on social state")
    print("| Find Landmark   | F     | Find predefined Naomark")
    print("| Talk            | T     | Send TTS commands to the robot")
    print("| Animate Talk    | AT    | Send TTS commands to the robot with gestures and launch animations")
    print("| Battery         | Bat   | Display battery charge in percent")
    print("--------------------------")

def main():
    #Helper()
    while True:
        wizard_command = UserInput(mode = 'Command')
        Launcher(wizard_command)

main()
    