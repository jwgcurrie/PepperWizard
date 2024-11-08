# PepperWizard 

PepperWizard is a command line interface for tele-opeating the Pepper robot. 


## Launching PepperWizard:
Pepperwizard can be launched with: **python Pepperwizard.py**

## Hotkeys 
Functionality can be accessed by entering predefined hotkeys. 

| **Key**  | **Launch**        | **Description** |
| -------- | -------           | -------- 
| B        | Begin             | *Wake robot* <br>Motor stiffness active <br>robot assumes standing posture <br> Robot resumes life
| E        | End              | *Robot rests* <br> Robot assumes resting posture <br> Motor stiffness off
| J        | [JoystickMove](https://github.com/jwgcurrie/PepperWizard/blob/main/Documentation/JoystickMove.md)           | Robot motion is controlled via joystick commands
| S        | [SocialState](https://github.com/jwgcurrie/PepperWizard/blob/main/Documentation/SocialState.md) | *Social State Active* <br> Robot is aware of people in its environment and will make eye contact with the tracked person <br> Robot is aware of motion in its environment and will look in the direction of motion <br> Robot is aware of sounds in its environment and will look in the direction of sounds
| F        | Find               | *Find Landmarks* <br> Robot will look for landmarks in its environment, once found the robot will look at the landmark until interrupted by the next PepperWizard command
| T        | [PepperTalk](https://github.com/jwgcurrie/PepperWizard/blob/main/Documentation/PepperTalk.md)               | *PepperTalk - speech mode* <br> The robot will verbalise the text input of the wizard
| AT        | [PepperTalk](https://github.com/jwgcurrie/PepperWizard/blob/main/Documentation/PepperTalk.md)               | *PepperTalk - animation mode* <br> The robot will verbalise the text input of the wizard, while gesturing using the context of the wizard's input | |

