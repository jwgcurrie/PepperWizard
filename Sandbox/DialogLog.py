#   Goal:
#   Generate dataset containing the dialog spoken by the robot and performed animations.
#---------------------------------------------------------------------------------------
#   Format: .csv
#   Headings: | datetime | dialog | animations | 

import numpy as np
from datetime import datetime
import csv


def UserInput(mode):
    if mode == 'Command':
        user_input = raw_input("Enter Command: ")
    elif mode == 'TTS':
        user_input = raw_input("Pepper: ")
    elif mode == 'Look':
        user_input = raw_input("Enter Direction: ")
    return user_input

#def PepperTalk(tts, animation_service, animate):    
def PepperTalk(animate):    

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
            print(out)
            AppendToArray(dialog_log, out)
            AppendToArray(datetime_log, GetDateTime())


            #tts.say(out)

        elif input in animations and animate:
            i = np.where(animations == input)[1][0]
            tag = animations[1,i]
            #animation_service.runTag(str(tag)) 
            out = str(tag)
            print(out)
            AppendToArray(dialog_log, out)
            AppendToArray(datetime_log, GetDateTime())



        else:
            #tts.say(input)
            out = input
            print(out)
            AppendToArray(dialog_log, out)
            AppendToArray(datetime_log, GetDateTime())

    out =  "--- Exiting PepperTalk --- "
    AppendToArray(dialog_log, out)
    AppendToArray(datetime_log, GetDateTime())

    print(out)

def AppendToArray(array, new_string):
    array.append(new_string)
    return array   

def GetDateTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string



dialog_log = ["start"]
datetime_log = [GetDateTime()]
print(PepperTalk(animate = False))
print(dialog_log)
print(str(datetime_log))

filename = "test_dataset.csv"

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["datetime", "dialog"])
    
    for i in range(len(dialog_log)):
        csvwriter.writerow([datetime_log[i], dialog_log[i]])

print("dialog written to: " + str(filename))



