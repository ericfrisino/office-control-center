#!/usr/bin/env python3

import argparse
import sys
import board
import time
import neopixel

# Process Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--strip', type=str, help='Select strip to affect.\nCurrently 2 options: `monitor` or `shelf`')
parser.add_argument('-c', '--color', type=str, help='What color would you like to turn the LEDs?\nCurrent options: `white`, `red`, `blue` `purple`')
parser.add_argument('-rgb', '--rgb', type=str, help="Enter RGB value as such `000,000,000`")
parser.add_argument('-k', '--kill', action='store_true', help="Use this command to turn off all pixels.\nIf used in conjunction with -s it will only turn off that strip.")
parser.add_argument('-b', '--brightness', type=float, help="How bright should the pixels show between 0 and 1")
args = parser.parse_args()

brightness = 1

if args.brightness:
	if 0 <= args.brightness <= 1:
		brightness = args.brightness
	else:
		sys.exit("Brightness must be a decimal number between 0 and 1 inclusive.")

# Initialize monitor pixels.
monitorPixels = neopixel.NeoPixel(board.D18, 50, brightness=brightness)

# Initialize shelf pixels.
shelfPixels = neopixel.NeoPixel(board.D21, 580, brightness=brightness)

if __name__ == '__main__':
	if args.color:
		if args.rgb:
			print("You can not use -c (--color) and -r (--rgb) together.\nYou must use one or the other.")
			exit()

	if args.rgb:
		color = tuple(map(int, args.rgb.split(',')))
	else:
		color = (255, 255, 255)

	if args.kill:
		color = (0, 0, 0)

	if args.strip == 'monitor':
		# DO SOMETHING
		monitorPixels.fill(color)
		print("Monitor pixels have been set to " + str(color))
		exit()
	elif args.strip == 'shelf':
		# DO SOMETHING
		shelfPixels.fill(color)
	elif args.kill:
		monitorPixels.fill(color)
		shelfPixels.fill(color)
	else:
		sys.exit("Please select `-s monitor` or `-s shelf` ")
