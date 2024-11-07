# SocialState

When Pepper's social state is active, the robot's Background movement and Basic Awareness functionality is enabled.

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