import neopixel
from neopixel import Color
import time 


class Strip:
  
    def __init__(self, led_count, led_pin=18 , led_freq_hz=800000, led_dma=10,
                 led_invert=False, led_brightness=255, led_channel=0):
        self.strip = neopixel.Adafruit_NeoPixel(led_count, led_pin, led_freq_hz, led_dma,
                                                led_invert, led_brightness, led_channel)
        self.strip.begin()

    def __del__(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0,0,0))
            self.strip.show()

    def turn_on(self, num, color):
        self.strip.setPixelColor(num, color)
        self.strip.show()

    def turn_off(self, i):
        self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()


if __name__ == '__main__':
    s = Strip(61)
    s.turnOn(1, Color(0, 255, 0))

    for i in range(60):
        s.turn_on(i, Color(0, 0, 255))
        time.sleep(1)
        s.turn_off(i)
