smartlight.py: Run as the main file. The raspberry pi get the weather condition through internet and read the color-weather patter through a database table to determine which color should the bulb light. The ultrasonic sensor and bluetooth dongle give the reading to Pi to determine the location of user and umbrella. Raspberry Pi control the bulb according to the information provided by sensor.

webserver.py: Run as the web server. User can set the color of the bulb. User can watch surveillance through the camera connected to the Pi. HTML file controlnew.html is in the fold templates

blescan.py: Scan ble device around and return the ID and signal strength to pi.

bulb.py:  Get the IP address of the smart bulb and control the light

flux_led.py: Communicate with the smart bulb through Wifi.

sensor.py: Read the input from ultrasonic sensor.

weather.py: Get weather information from a weather api “wunderground”


Reference Code File:

blescan.py from https://github.com/switchdoclabs/iBeacon-Scanner-
flux_led.py from https://github.com/beville/flux_led
video player plugin in controlnew.html: http://bbs.csdn.net/topics/390922539

