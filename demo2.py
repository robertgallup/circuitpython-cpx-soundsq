########################################################
# CircuitPython
#
# Program that calculates musical scale frequencies, then
# sweeps the scale, and finally playing random notes from
# the scale
#
import time
from random import randint

from soundsq import SND

# Half- and whole step frequency multipliers
half_step = 2**(1./12.)
whole_step = half_step * half_step

# Scales intervals
penta_intervals     = [whole_step, whole_step, whole_step*half_step, whole_step]
major_intervals     = [whole_step, whole_step, half_step, whole_step, whole_step, whole_step]
minor_intervals     = [whole_step, half_step, whole_step, whole_step, half_step, whole_step]
chromatic_intervals = [half_step] * 11

# Create the sound object
snd = SND()

########################################################
# Generate scale frequencies
#
# interval_list	: List of intervals in scale
#
def generate_scale_frequencies(interval_list, reps=1, base_frequency=440):
	scale = []
	for r in range(reps):
		scale += [base_frequency]
		frequency = base_frequency
		for interval in interval_list:
			frequency *= interval
			scale += [frequency]
		base_frequency *= 2
	return scale

########################################################
# Play a scale from beginning to end
#
# scale		: list of scale frequecies
# tempo		: beats per minute for quarter notes
# note_type : 1=whole notes, 2=half, etc. Default is quarter notes
def play_scale(scale, tempo=100, note_type=4):
	duration = (240/tempo) / note_type
	for note in scale:
#		cpx.play_tone(note, duration)
		snd.play_tone(note, duration)

########################################################
# Play random notes from scale
#
# scale		: list of scale frequecies
# tempo		: beats per minute for quarter notes
# note_type : 1=whole notes, 2=half, etc. Default is quarter notes
# notes		: Number of notes to play. 0=infinite
def play_scale_random(scale, tempo=100, note_type=4, notes=0):
	duration = (240/tempo) / note_type
	l = len(scale)
	infinite = True if notes==0 else False
	while infinite or (notes != 0):
		notes -= 1
#		cpx.play_tone(scale[randint(0,l-1)], duration)
		snd.play_tone(scale[randint(0,l-1)], duration)

# Set the scale to use
scale_intervals = penta_intervals
# scale_intervals = minor_intervals
# scale_intervals = chromatic_intervals
# scale_intervals = major_intervals

# Generate scale frequencies
scale_frequencies = generate_scale_frequencies(scale_intervals, reps=2)
for i in range (3):
	# Play the scale
	play_scale(scale_frequencies, note_type=8)
	# Wait for a dramatic second
	time.sleep(1)
	# Perform a score of random notes
	play_scale_random(scale_frequencies, note_type=32, tempo=100, notes=100)

# Get props
print("Humble Bow.")
