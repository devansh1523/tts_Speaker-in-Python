# This code will work only in Windows.
# For mac:
#     1. import os
#     2. change line 16 to f"say {text}"
#     3. change line 17 to os.system(text)


import win32com.client as win

if __name__ == '__main__':
    print("Welcome to Speaker for Windows created by Devansh Cokerey")
    while True:
        text = input("Enter the text to speak: ")
        if text == "exit":
            break
        tts = win.Dispatch("SAPI.SpVoice")
        tts.Speak(text)
