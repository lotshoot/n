from playsound import playsound
# import required for text to speech conversion
from gtts import gTTS

mytext = "Kaate nahi katte din ye rat"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("D:\\M.sc. IT\\Second Year\\my7.mp3")
playsound("D:\\M.sc. IT\\Second Year\\my7.mp3")
'''


playsound("D:\\M.sc. IT\\Second Year\\my1.mp3")

playsound("D:\\M.sc. IT\\Second Year\\my2.mp3")

playsound("D:\\M.sc. IT\\Second Year\\my3.mp3")

playsound("D:\\M.sc. IT\\Second Year\\my4.mp3")

playsound("D:\\M.sc. IT\\Second Year\\my5.mp3")

'''
