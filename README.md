<h1 align="center">Office Control Center</h1>

Just a fun project for me to mess around with controlling different physical things in my office.

For now its just WS2812B LED lights.

## Command Line Arguments
 + `-b` `--brightness` : How bright should the pixels show between `0` and `1` inclusive.
 + `-c` `--color` : What color would you like to turn the LEDs? Current options: `white`, `red`, `blue` `purple`.
 + `-k` `--kill` : Use this command to turn off all pixels. If used in conjunction with `-s` it will only turn off that strip.
 + `-rgb` `--rgb` : Enter RGB value as such `"000,000,000"`.
 + `-s` `--strip` : Select strip to affect. Currently 2 options: `monitor` or `shelf`.
 
 ## Available Light Strips
 
 For development purpouses I will be using 2 strips of lights:
 1. `monitor` : 50 WS2812B LED lights.
 2. `shelf` : 500 WS2812B LED lights.
 
