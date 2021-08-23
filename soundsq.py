########################################################
# CircuitPython soundsq library
#
#

import board
import audioio
import audiocore
import digitalio
import array

class SND:
	"""
	The soundsq library duplicates the sound API in the CPX library with
	sound based on a square wave rather than the built-in sine wave.
	This requires less overhead and results in higher performance
	in most circumstances.
	"""

	def __init__(self):
		self._volume = 14
		self._speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
		self._speaker_enable.switch_to_output(value=False)
		self._sound = audioio.AudioOut(board.SPEAKER, quiescent_value = 0)
		self._wave = array.array("H", [(1<<self._volume)-1, 0])
		self._wave_sample = audiocore.RawSample(self._wave)

	def play_tone(self, frequency, duration):
		self.start_tone(frequency)
		time.sleep(duration)
		self.stop_tone()

	def start_tone(self, frequency):
		if not self._sound.playing:
			self._wave_sample.sample_rate = round(frequency * 2)
			self._sound.play(self._wave_sample, loop=True)
			self._speaker_enable.value = True

	def stop_tone(self):
		self._speaker_enable.value = False
		self._sound.stop()

	def play_file(self, file_name):
		self.stop_tone()
		self._speaker_enable.value = True
		with self._audio_out(board.SPEAKER) as audio:  # pylint: disable=not-callable
			wavefile = audiocore.WaveFile(open(file_name, "rb"))
			audio.play(wavefile)
			while audio.playing:
				pass
		self._speaker_enable.value = False

