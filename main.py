import pyautogui, time, threading, subprocess, os, psutil
from pathlib import Path

# get the button location
def the_bot(meeting_id, password):
    # join a meeting
    button_location = pyautogui.locateOnScreen(
        str(Path("images/join-meeting.png")),
        confidence = 0.5
        )
    pyautogui.click(pyautogui.center(button_location))
    
    # meeting ID
    pyautogui.click(668,329)
    pyautogui.write(meeting_id)
    join = pyautogui.locateOnScreen(str(Path("images/join.png")),confidence = 0.8)

    # join the meeting
    pyautogui.click(pyautogui.center(join))

    # enter the password
    time.sleep(3)
    pyautogui.write(password)

    # enter the meet
    join = pyautogui.locateOnScreen(str(Path("images/enter-meet.png")),confidence = 0.5)
    pyautogui.click(pyautogui.center(join)) # click join the meeting

    if(not join):
        print("Could not enter password!")
        exit()

    # # click audio prompt
    # audio = None
    # counter = 0 # count our wait
    # while(audio == None):
    #     # wait until audio prompt shows up
    #     time.sleep(1)
    #     if(counter > 10):
    #         print("Could not enter meeting!") # waited too long/meeting not yet started
    #         exit()
    #     audio = pyautogui.locateOnScreen(
    #         str(Path("images/join-with-computer-audio.png")),
    #         confidence = 0.8
    #     )
    #     counter += 1
    # pyautogui.click(pyautogui.center(audio)) # click the audio button

    # enter the chat
    chat = None
    pos = 1
    while(not chat):
        time.sleep(3)
        # move the mouse to show chat 
        pyautogui.moveTo(int(200*pos),int(500/pos))
        chat = pyautogui.locateOnScreen(str(Path("images/chat.png")),confidence = 0.9)
        pos += 1
    pyautogui.click(pyautogui.center(chat))

    time.sleep(1)
    # type the roll no
    pyautogui.click(1121,722)
    pyautogui.write("Your Message")
    pyautogui.press("enter")

    # leave the meeting
    leave = None
    while(not leave):
        leave = pyautogui.locateOnScreen(str(Path("images/leave.png")),confidence = 0.9)
    pyautogui.click(pyautogui.center(leave))

    time.sleep(0.5)
    # confirm leave
    leave = None
    while(not leave):
        leave = pyautogui.locateOnScreen(str(Path("images/leave-meeting.png")),confidence = 0.9)
    pyautogui.click(pyautogui.center(leave))

if __name__ == "__main__":
    # check if zoom is open or not
    if "zoom" in (p.name() for p in psutil.process_iter()):
        print("Zoom already open")
        exit()
    else:
        lines = list() # storing lines
        with open("meeting.txt","r") as file:
            # open meetings file and read all the lines
            for line in file:
                lines.append(line)

        temp = list() 
        meeting_details = list() # all meeting details with format
        for line in lines:
            temp = line.split(' ') 
            meeting_details.append((temp[0],temp[1],temp[2])) # store the meeting details
            
        print("Select the meeting")
        for meeting in zip(range(0,len(meeting_details)),meeting_details):
            print(meeting) # print the selected meet
            
        while(True): # select meeting 
            try:
                meeting_no = int(input("Enter meeting no.:"))
                print("Selected meeting",meeting_details[meeting_no])
            except IndexError: # invalid meeting no. entered
                print("Enter valid meeting no.")
                continue
            else: # break if correct meeting no. entered
                break
            
        # open zoom
        zoom = subprocess.Popen("zoom",shell = False)
        # wait for zoom to open
        time.sleep(3) 
        # execute the bot function
        the_bot(meeting_details[meeting_no][0],meeting_details[meeting_no][1]) 

        