import neopixel
import time 
import Color

LED_COUNT      = 40      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW


class Strip:
  strip = 0
  
  __init__(
    LED_COUNT, LED_PIN = 18 , LED_FREQ_HZ = 800000, 
    LED_DMA = 10, LED_INVERT = False, LED_BRIGHTNESS = 255, 
    LED_CHANNEL = 0, LED_STRIP = ws.SK6812_STRIP_RGBW
    ):
    
    strip = neopixel.Adafruit_NeoPixel(
      LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, 
      LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

  def turnOn(i, color):
    strip.setPixelColor(i, color)
    strip.show()

  def turnOff(i, color):
    strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

  

  if __name__ == '__main__':
    s = Strip(61)
    c = Color()
    s.turnOn(1,c.Red)
    time.sleep(1)
    s.turnOn(2, c.Blue) 

    while(1):
      g = raw_input("Enter Command:")
      eval(g)
