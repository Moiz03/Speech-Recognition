# import library
import pyautogui as pyt
import webbrowser as web
import speech_recognition as sr
import os
# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    while(True):
        audio_text = r.listen(source,phrase_time_limit=4)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            string = r.recognize_google(audio_text,language='en-US')

            if string == "up":
                pyt.press("up")
            elif string == "down":
                pyt.press("down")
            elif string == "left" or string == "previous":
                pyt.press("left")
            elif string == "right" or string == "next":
                pyt.press("right")
            elif string == "volume up":
                pyt.press("volumeup")
            elif string == "volume down":
                pyt.press("volumedown")
            elif string == "mute":
                pyt.press("volumemute")
            elif string == "pause":
                pyt.press("space")
            elif string == "select all":
                pyt.hotkey('ctrl', 'a')
            elif string == "cut":
                pyt.hotkey('ctrl', 'x')
            elif string == "copy":
                pyt.hotkey('ctrl', 'c')
            elif string == "paste":
                pyt.hotkey('ctrl', 'v')
            elif string == "open browser":
                os.startfile(r'C:\Program Files\Mozilla Firefox\firefox.exe')


        except:
            print("Sorry, I did not get that")
