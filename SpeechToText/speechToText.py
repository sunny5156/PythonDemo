import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print "say:"
    audio = r.listen(source)
    
words=r.recognize_bing(audio, "1a7b3acb57684dc58592d17f1194295d", "zh-CN",False)
print "you said :"+ words
    
