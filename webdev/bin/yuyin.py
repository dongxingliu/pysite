import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
str1 = """
好好做饭 我准时下班哦
"""
speaker.Speak(str1)
# for i in range(1, 6):
#     speaker.Speak("呵呵第" + str(i) + "次")