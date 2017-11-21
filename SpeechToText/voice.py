#-*- coding: UTF-8 -*-
import speech_recognition as sr
import speech
import win32api
import os
import sys
import time
import win32con
import pbs
import pygame

command1 = {
             u'关闭计算机。': 'shutdown -s -t 1',
             u'重启计算机。': 'shutdown -r',
             u'打开浏览器。': '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"',
             u'关闭浏览器。': 'taskkill /F /IM chrome.exe',
             u'百度一下。': 'start http://www.baidu.com',
             u'关闭音乐。': 'taskkill /F /IM cloudmusic.exe',
             u'打开音乐。': '"D:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe"',
             u'放首歌。': '"D:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe"',
             u'下一首。': '"D:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe"',
              }
speech.say('语音识别已开启'.decode('utf-8'))
# print command1
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:               # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    phrase=r.recognize_bing(audio,"1a7b3acb57684dc58592d17f1194295d","zh-CN",False)
    speech.say(phrase)
    if phrase in command1.keys():
        speech.say('即将为您%s'.decode('utf-8') %phrase)

        print phrase.find(u'关闭')
        print type(phrase.find(u'关闭'))

        if phrase.find(u'关闭') == -1 :
            win32api.ShellExecute(0,'open',command1[phrase],'','',0)
        else:
            os.system(command1[phrase])

        speech.say('任务已完成！'.decode('utf-8'))
        if phrase == u'放首歌。':
            speech.say('马上播放音乐！'.decode('utf-8'))
            time.sleep(5)
            win32api.keybd_event(17, 0, 0, 0)
            win32api.keybd_event(80, 0, 0, 0)
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(80, 0, win32con.KEYEVENTF_KEYUP, 0)
        if phrase == u'下一首。':
            speech.say('马上播放音乐！'.decode('utf-8'))
            time.sleep(5)
            win32api.keybd_event(17, 0, 0, 0)
            win32api.keybd_event(39, 0, 0, 0)
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
    if phrase == u'大象怎么叫。':
         pygame.mixer.init()
         track1=pygame.mixer.music.load("daxiang.mp3")
         pygame.mixer.music.play()
    if phrase == u'退出程序。':
         speech.say('已退出程序，感谢使用！'.decode('utf-8'))
         sys.exit()
