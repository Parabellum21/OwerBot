#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gtts import gTTS # 
#from pygame import mixer
import time
#mixer.init()


def get_spech(msg, mova):
    print(msg)
    tts=gTTS(text=msg, lang=mova)
    tts.save('hello.mp3')
    return 'hello.mp3'

def play(fl):
  # Проигрываем полученный mp3 файл
    mixer.music.load(fl)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)
    mixer.stop
    mixer.quit

if __name__ == "__main__":
    #fl = get_spech("Привет Андрей")
    fl = get_spech("Привіт денис, як твої справию. Чому ти не на дворі")
    play(fl)