import winsound, sys
from msvcrt import getch

Freq = 440
Dur = 440

while True:
	char = getch()
	Freq = 0

	if char == '0':
		break
	if char == 'A': # C2
		Freq = 261.63
	elif char == 'S': # D2
		Freq = 293.66
	elif char == 'D': # E2
		Freq = 329.63
	elif char == 'F': # F2
		Freq = 349.23
	elif char == 'G': # G2
		Freq = 392
	elif char == 'H': # A2
		Freq = 440
	elif char == 'J': # B2
		Freq = 493.88
	elif char == 'K': # C3
		Freq = 523.25
	elif char == 'L': # D3
		Freq = 587.33
	if char == 'a': # C
		Freq = 130.81
	elif char == 's': # D
		Freq = 146.83
	elif char == 'd': # E
		Freq = 164.81
	elif char == 'f': # F
		Freq = 174.61
	elif char == 'g': # G
		Freq = 196
	elif char == 'h': # A
		Freq = 220
	elif char == 'j': # B
		Freq = 246.94
	elif char == 'k': # C2
		Freq = 261.63
	elif char == 'l': # D2
		Freq = 293.66

	if char == 'W': # C#2
		Freq = 277.18
	elif char == 'E': # D#2
		Freq = 311.13
	elif char == 'T': # F#2
		Freq = 369.99
	elif char == 'Y': # G#2
		Freq = 415.30
	elif char == 'U': # A#2
		Freq = 466.16
	elif char == 'O': # C#3
		Freq = 554.37
	if char == 'w': # C#
		Freq = 138.59
	elif char == 'e': # D#
		Freq = 155.56
	elif char == 't': # F#
		Freq = 185
	elif char == 'y': # G#
		Freq = 207.65
	elif char == 'u': # A#
		Freq = 233.08
	elif char == 'o': # C#2
		Freq = 277.18

	Freq = int(round(Freq))

	if Freq != 0:
		# print Freq, Dur
		winsound.Beep(Freq,Dur)