########################################################
# CircuitPython soundsq demo
#
# Plays 30 tones at random frequencies
#
import time
from random import randint
from soundsq import SND

snd = SND()

for i in range (30):
	snd.play_tone(randint(1,40)*100, .1)
	time.sleep(.0001)
