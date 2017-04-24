import os
import sys
import signal

def signal_handler(signal, frame):
	print("You pressed Ctrl+C!")
	sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)
signal.pause()