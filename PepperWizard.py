import qi
import motion
import argparse
import sys
import time
import pygame
import numpy as np


def main(session):
    PrintTitle()

    alife = session.service("ALAutonomousLife") 
    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")
    tts = session.service("ALTextToSpeech")
    tts_animated = session.service("ALAnimatedSpeech")
    tracker_service = session.service("ALTracker")
    social_perception = session.service("ALPeoplePerception")
    tablet_service = session.service("ALTabletService")
    landmark_service = session.service("ALLandMarkDetection")
    memory_service = session.service("ALMemory")
    awareness_service = session.service("ALBasicAwareness")
    face_service = session.service("ALFaceDetection")
    audio_player_service = session.service("ALAudioPlayer")
    LED_service = session.service("ALLeds")
    animation_service = session.service("ALAnimationPlayer")
    audio_service = session.service("ALAudioDevice")
    battery_service = session.service("ALBattery")

    InitialiseTablet(tablet_service)
    print(" --- Pepper Online ---")
    BatteryStatus(battery_service)
    controller = InitialiseController()
    print(" --- PepperWizard Ready ---")

    while 1:
        wizard_command = UserInput(mode = 'Command')
        Launcher(wizard_command, alife, tracker_service, motion_service, posture_service, tts, tts_animated, landmark_service, 
                     memory_service, awareness_service, face_service, audio_player_service, LED_service, animation_service, audio_service, controller, battery_service, social_perception)

    print(" --- Exiting Pepper Wizard --- ")
    return

def PrintTitle():
    print("__________                                   __      __.__                         .__")
    print("\______   \ ____ ______ ______   ___________/  \    /  \__|____________ _______  __| /")
    print(" |     ___// __  \____  \____ \_/ __ \_  __ \   \/\/   /  \___   /\__  \\_  __ \/ __  | ")
    print(" |    |   \  ___/|  |_> >  |_> >  ___/|  | \/\        /|  |/    /  / __ \|  | \/ /_/ | ")
    print(" |____|    \___  >   __/|   __/ \___  >__|    \ _/\  / |__/_____ \(____  /__|  \____ | ")
    print("                 |__|   |__|                       \/           \/     \/           \/ ")
    print("---------------------------------------------------------------------------------------")
    print(" - jwgcurrie")


def Launcher(wizard_command, alife, tracker_service, motion_service, posture_service, tts, tts_animated, landmark_service, 
                memory_service, awareness_service, face_service, audio_player_service, LED_service, animation_service, audio_service, controller, battery_service, social_perception):
    if wizard_command == "B": 
        LaunchBegin(motion_service, alife, tracker_service, awareness_service, face_service)
    elif wizard_command in ['S', 'S BR', 'S WB', 'S MC']:
        LaunchSocialState(alife, tracker_service, awareness_service, face_service, wizard_command, social_perception)
    elif wizard_command == 'E':
        motion_service.rest()
    elif wizard_command == 'F':
        FindLandmark(tracker_service, motion_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service)
    elif wizard_command == 'J':
        LaunchJoystickMove(controller, motion_service, audio_service, tracker_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service)
    elif wizard_command == 'T':
        PepperTalk(tts, animation_service, animate = False)
    elif wizard_command == 'AT':
        PepperTalk(tts_animated, animation_service, animate = True)
    elif wizard_command == 'Bat':
        BatteryStatus(battery_service)
    elif wizard_command == 'Look':
        Look(tracker_service)
    else:
        print("Command not recognised")
    return

def UserInput(mode):
    if mode == 'Command':
        user_input = raw_input("Enter Command: ")
    elif mode == 'TTS':
        user_input = raw_input("Pepper: ")
    elif mode == 'Look':
        user_input = raw_input("Enter Direction: ")
    return user_input


def Look(tracker_service):
    x_robot = 0.5
    z_robot = 1.21
    speed = 0.2
    direction = UserInput(mode = 'Look')
    if direction == 'L':
        pos = [x_robot, 0.5, z_robot]
        tracker_service.lookAt(pos, 2, speed, False)
    elif direction == 'R':
        pos = [x_robot, -0.5, z_robot]
        tracker_service.lookAt(pos, 2, speed, False)
    elif direction == 'S':
        pos = [x_robot, 0, z_robot]
        tracker_service.lookAt(pos, 2, speed, False)
    elif direction == 'D':
        pos = [0.1, 0, 0]
        tracker_service.lookAt(pos, 2, speed, False)


def BatteryStatus(battery_service):
    battery_charge = battery_service.getBatteryCharge()
    print("Battery Charge: " + str(battery_charge) + "%")

def LaunchBegin(motion_service, alife, tracker_service, awareness_service, face_service):
    print("LaunchBegin")
    motion_service.wakeUp()
    SocialState(alife, tracker_service, awareness_service, face_service, True)

def LaunchSocialState(alife, tracker_service, awareness_service, face_service, wizard_command, social_perception):
    tracker_service.unregisterAllTargets()
    tracker_service.setTimeOut(2000)
    awareness_service.setEngagementMode("FullyEngaged")

    social_perception.setMaximumDetectionRange(2.0)
    social_perception.setTimeBeforePersonDisappears(2)
    social_perception.setFastModeEnabled(True)
    social_perception.setMovementDetectionEnabled(True)

    SocialState(alife, tracker_service, awareness_service, face_service, True)
    if wizard_command == 'S BR':
        tracking_mode = "BodyRotation"
    elif wizard_command == 'S WB':
        tracking_mode = "WholeBody"
    elif wizard_command == 'S MC':
        tracking_mode = "MoveContextually"
    elif wizard_command == 'S':
        tracking_mode = "Head"
    
    tracker_service.setMode(str(tracking_mode))
    print("Tracking Mode: ") + str(tracker_service.getMode())
    #tracker_service::stopTracker()




def LaunchJoystickMove(controller, motion_service, audio_service, tracker_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service):
    print("Entering JoystickMove")
    try:
        landmark_found = False
        while not landmark_found:
            landmark_found = JoystickMove(controller, motion_service, audio_service, tracker_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service)
    except KeyboardInterrupt:
        motion_service.stopMove()
        print("Exiting JoystickMove")
        pass 


def PepperTalk(tts, animation_service, animate):    

    quick_responses = [['T', 't', 'Y', 'N', 'H', 'U'],
                    ['MMM', 'huh', 'yes', 'no', 'hello', 'I am not sure'],
                    ['estimate', 'think', 'affirmative', 'no', 'hi', 'not know'],
                    ["\\rspd=50\\ ", "\\rspd=25\\ ", "\\rspd=100\\ ", "\\rspd=100\\ ", "\\rspd=100\\ ", "\\rspd=100\\ "],
                    ['stopTag', 'stopTag', 'stopTag', 'waitTag', 'waitTag', 'stopTag']]
    
    animations = [['S', 'J', 'I', 'D', 'M', 'P', 'B'],
                ['sad', 'joyful', 'you', 'disappointed', 'myself', 'happy', 'bored']]

    quick_responses = np.array(quick_responses)
    animations = np.array(animations)

    print(" --- Entering PepperTalk as Wizard ---")
    if animate:
        print("Warning: Animation Mode is Active")
        print("Ensure the robot has appropriate space to perform animations")

    while True:
        input = UserInput(mode = 'TTS')
        if input == 'Q':
            break
        elif input in quick_responses:
            i = np.where(quick_responses == input)[1][0]
            say = quick_responses[1,i]
            tag = quick_responses[2,i]
            tuning = quick_responses[3,i]
            stop = quick_responses[4,i]

            if animate:
                out = "^startTag(" + str(tag) + ") " + str(tuning) + str(say) + " ^" + str(stop) + "("+ str(tag) + ")"
            elif not animate:
                out = str(tuning) + str(say)
            tts.say(out)
        elif input in animations and animate:
            i = np.where(animations == input)[1][0]
            tag = animations[1,i]
            animation_service.runTag(str(tag)) 
        else:
            tts.say(input)
    print(" --- Exiting PepperTalk --- ")

    
def SocialState(alife, tracker_service, awareness_service, face_service, interaction_switch):
    alife.setAutonomousAbilityEnabled("BackgroundMovement", interaction_switch)
    alife.setAutonomousAbilityEnabled("BasicAwareness", interaction_switch)
    alife.setAutonomousAbilityEnabled("ListeningMovement", True)
    alife.setAutonomousAbilityEnabled("SpeakingMovement", True)
    alife.setAutonomousAbilityEnabled("AutonomousBlinking", True)
    face_service.setTrackingEnabled(interaction_switch)
    awareness_service.setEnabled(interaction_switch)
    
    basic_AwarenessState = awareness_service.isRunning()

    print("SocialState Status: " + str(basic_AwarenessState))

    return

def InitialiseTablet(tablet_service):
    try:
        tablet_service.turnScreenOn(False)    
        tablet_service.setBrightness(0)
        print("SUCCESS: InitialiseTablet() - Tablet Initialised")
    except:
        print("ERROR: InitialiseTablet() - Failed ")



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
    

def JoystickMove(controller, motion_service, audio_service, tracker_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service):
    effector = 'Move_XY'
    found_table = False

    for event in pygame.event.get():
        # Read joystick axis events
        Controller_Left_X = controller.get_axis(pygame.CONTROLLER_AXIS_LEFTX)
        Controller_Left_Y = controller.get_axis(pygame.CONTROLLER_AXIS_LEFTY)
        Controller_Right_X = controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTX)
        Controller_Right_Y = controller.get_axis(pygame.CONTROLLER_AXIS_RIGHTY)


        MotionMapping(motion_service, audio_service, effector, Controller_Left_X, Controller_Left_Y, Controller_Right_X, Controller_Right_X)
        if(controller.get_button(2)):
            print("FindLandmark() - Active")
            motion_service.stopMove()
            found_table = FindLandmark(tracker_service, motion_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service)
            if found_table:
                print("FindLandmark() - Success: " + str(found_table))
            elif not found_table:
                print("Joystick control resumed")
            return found_table
        if(controller.get_button(1)):
            print("SocialState(): Active")
            tracker_service.removeTarget("LandMark")
            SocialState(alife, tracker_service, awareness_service, face_service, True)
    return found_table


def MotionMapping(motion_service, audio_service, effector, Controller_LX, Controller_LY, Controller_RX, Controller_RY):
    v_x = 0.15
    v_theta = 0.5

    if effector == 'Move':
        command_x = -round(Controller_LY, 1) * v_x
        command_theta = -round(Controller_R, 1) * v_theta
        motion_service.moveToward(command_x, 0, command_theta)
        print()
    elif effector == 'Head':
        command_yaw = -round(Controller_LX, 1) * 2 # Max value: 2.0857
        command_pitch = round(Controller_R, 1) * 0.4 # Max Value: 0.4451
        motion_service.setAngles(['HeadYaw', 'HeadPitch'], [command_yaw, command_pitch], joint_speed_frac) # TODO - bug yaw goes to extreme not obeying speed limits
    elif effector == 'Move_XY':
        command_x = -round(Controller_LY, 1) * v_x
        command_y = -round(Controller_LX, 1) * v_x
        command_theta = -round(Controller_RY, 1) * v_theta
        motion_service.moveToward(command_x, command_y, command_theta)

        
def FindLandmark(tracker_service, motion_service, posture_service, alife, landmark_service, memory_service, awareness_service, face_service):
    t0 = time.time()
    landmark_service.subscribe("Test_LandMark", 500, 0.0 )
    SocialState(alife, tracker_service, awareness_service, face_service, False)
    tracker_service.setEffector("None")
    tracker_service.toggleSearch(False)
    targetName = "LandMark"
    LandMarkID = 119
    LandMarkSize = 0.22
    tracker_service.registerTarget(targetName, [LandMarkSize, LandMarkID])
    mode = "BodyRotation"
    tracker_service.setMode(mode)
    target_position = [2.2753167152404785, 0.17584750056266785, -0.2796962559223175]
    PositionFrame = 2
    FractionalSpeed = 0.05
    UseWholeBody = True
    tracker_service.lookAt(target_position, PositionFrame, FractionalSpeed, UseWholeBody)

    landmark_found = False
    time_elapsed = 0
    while not landmark_found and (time_elapsed < 10):
        t1 = time.time()
        time_elapsed = t1 - t0
        try:
            val = memory_service.getData("LandmarkDetected", 0)
            val = val[1]
            for markInfo in val:
                    markInfo[0]
            tracker_service.registerTarget("LandMark", [0.267, markInfo[1]])
            tracker_service.track("LandMark")
            TaskPosture(motion_service)
            landmark_found = True
            print("Found Landmark: True")
            time.sleep(1)
        except:
            if time_elapsed < 10:
                print("Finding Landmark - " + str(round((10 - time_elapsed),1)) + str("s to timeout"))

    if ((time_elapsed > 10) and (landmark_found == False)):
        print("FindLandmark() - time elapsed greater than 10s")
        print("Exiting FindLandmark()")
    return landmark_found

def TaskPosture(motion_service):
    Breath(motion_service)
    LRArm_position(motion_service, 0.1)

def LRArm_position(motion_service, pFractionMaxSpeed):
    motion_service.setExternalCollisionProtectionEnabled("RArm", False)
    motion_service.setExternalCollisionProtectionEnabled("LArm", False)
    JointNamesLR = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
    
    ShoulderPitch_angle = 45
    ElbowRoll_angle = 36
    WristYaw_angle =  90

    ArmLR1 = [ShoulderPitch_angle, -0.5, 0, ElbowRoll_angle, WristYaw_angle, ShoulderPitch_angle, -0.5, 0, -ElbowRoll_angle, -WristYaw_angle]
    ArmLR1 = [ x * motion.TO_RAD for x in ArmLR1]
    pFractionMaxSpeed = 0.1
    motion_service.angleInterpolationWithSpeed(JointNamesLR, ArmLR1, pFractionMaxSpeed)
    return

def Breath(motion_service):
    pBPM = 15
    pAmplitude = 0.99
    breath_config = [["Bpm", pBPM], ["Amplitude", pAmplitude]]
    motion_service.setBreathConfig(breath_config)
    motion_service.setBreathEnabled("Legs", True)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.4", 
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.0.4'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
            "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    main(session)