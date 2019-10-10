import neopixel
from neopixel import Color
import time 


LED_COUNT      = 40      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0


class Strip:
  
  def __init__(self, LED_COUNT, LED_PIN = 18 , LED_FREQ_HZ = 800000, LED_DMA = 10, LED_INVERT = False, LED_BRIGHTNESS = 255, LED_CHANNEL = 0):
    self.strip = neopixel.Adafruit_NeoPixel(
      LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, 
      LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    self.strip.begin()

  def __del__(self):
    for i in range(self.strip.numPixels()):
      self.strip.setPixelColor(i, Color(0,0,0))
      self.strip.show()

  def turnOn(self, i, color):
    self.strip.setPixelColor(i, color)
    self.strip.show()

  def turnOff(self, i):
    self.strip.setPixelColor(i, Color(0, 0, 0))
    self.strip.show()

  

if __name__ == '__main__':
    s = Strip(61)
    s.turnOn(1,Color(0,255,0))

    for i in range(60):
    	s.turnOn(i, Color(0,0,255)) 
	time.sleep(1)
	s.turnOff(i)
