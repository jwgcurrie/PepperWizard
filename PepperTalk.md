# PepperTalk

PepperTalk is a command line interface for using Pepper's ALTextToSpeech and  ALAnimatedSpeech services.

## Launching and Exiting PepperTalk:
### Launch PepperTalk
As with other functionality in the PepperWizard interface, PepperTalk is launched with a keypress. The mode that PepperTalk enters depends on the key pressed. 
* **T** - Launches PepperTalk in *Speech* mode
* **AT**:   - Launches PepperTalk in *Animation* mode

Once launched PepperTalk will show the following message:

*Entering PepperTalk as Wizard*

### Exit PepperTalk:
PepperTalk can be exited by inputting *'Q'* followed by *enter*.

## PepperTalk in *Speech* Mode:
When PepperTalk is launched in *Speech* mode, Pepper will say the text that the Wizard inputs, after the *enter* key is pressed.

### Hotkeys:
PepperTalk makes use of a number of hotkeys that are used to quickly launch responses that are likely to be used frequently. 

| **Key**  | **Response**      | **Conveys** |
| -------- | -------           | -------- | 
| Y        | "Yes"             | Affirm
| N        | "No"              | Disagree
| H        | "Hello"           | Greeting
| U        | "I am not sure"   | Confused
| T        | "mmm" (thinking)  | Thought
| t        | "huh" (thinking ) | Thought

## PepperTalk in *Animation* Mode:
As with *Speech* mode, when in *Animation* mode, inputs from the Wizard will be verbalised by the robot. However in *Animation* mode the robot will perform contextual gestures inferred from the Wizard's speech command. 


**Warning - Before entering Animation mode, ensure the robot has adequate space to perform the animation, otherwise it is likely the robot will hit an obstacle during the gesture and could harm itself or others.**

The following warning will be presented to the Wizard when launching animation mode:

*Warning: Animation Mode is Active - Ensure the robot has appropriate space to perform animations*

### Hotkeys
As with *Speech* mode, hotkeys are available to quickly launch frequent activities. However in *animation* mode, Pepper's speech is supplemented with a contextual annimation, in addition there are hotkeys that a launch non-verbal pseudorandom animation based on the context. 


| **Key**  | **Verbal Response**      | **Conveys** | **Animation**|
| -------- | -------                  | --------    | --------  | 
| Y        | "Yes"                    | Affirm      | Nods
| N        | "No"                     | Disagree    | Shakes head
| H        | "Hello"                  | Greeting    | Waves
| U        | "I am not sure"          | Confused    | Not know
| T        | "mmm" (thinking)         | Thought     | Estimates
| t        | "huh" (thinking )        | Thought     | Thinks
| **Animation Only:**
| **Key**  | **Verbal Response**      | **Conveys** | **Animation**|
| J      | None                       | Joy         | Joyful
| P      | None                       | Happy       | Positivity 
| S      | None                       | Sad         | Sadness
| D      | None                       | Disappointed| Disappointment
| B      | None                       | Bored       | Boredom
| I      | None                       | Indicates to you| Gestures to person
| M      | None                       | Indicates to me| Gestures to Pepper





