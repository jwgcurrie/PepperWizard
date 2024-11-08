# SocialState

When Pepper's social state is active, the robot's Background movement and Basic Awareness functionality is enabled.

## Launching SocialState:
SocialState can be launched with the **S** key, or in JoystickMove the **◯** button. By default the robot's tracking effector is set to it's *Head*.


## Background Movement:
These are slight movements that the robot makes autonomously. <br> If the robot receives a motion command then background movements are suspended until the motion command is complete. <br> If the robot is standing then *setBreathEnabled* is called.

## Basic Awareness:
The robot's basic awareness module allows the robot to be aware of stimuli in its environment.

### Types of Stimulus:

| **Stimulus**  | **Triggered by**        | **Priority** | **Tracking Mode** |
| -------- | -------           | -------- | -------- |
| People | Human detected by camera | 1 | Head
| Touch - robot | Touch is detected by head/arm/bumper sensors| 2 | Head
| Touch - tablet | Touch is detected on robot's tablet| 3| Head
| Sound | Perceived sound| 5| Head
| Navigation motion | Movement in front of the robot's base | 6| Head

## Advanced:
If the wizard wants to set the robot's tracking effector to something other than the head, then the following hotkeys can be used to launch the SocialState in different settings. 

| **Key**  | **Tracking Effector** | **Description** 
| -------- | -------           | -------- |
| S | Head | Follows stimulus with head | 
| S BR | Body Rotation| Follows stimulus with head and body rotation | 
| S WB | Whole Body | Follows with whole body but no rotation| 
| S MC | Move Contextually |  Follows with head <br> Autonomously approaches tracked person, moves away, rotating, etc.
