import sensor, image, time,lcd
from modules import hub75e
from fpioa_manager import fm
from machine import Timer

latch = fm.register(33, fm.fpioa.GPIOHS10, force = True)
a = fm.register(28, fm.fpioa.GPIOHS11, force=True)
b = fm.register(29, fm.fpioa.GPIOHS12, force=True)
c = fm.register(30, fm.fpioa.GPIOHS13, force=True)
d = fm.register(31, fm.fpioa.GPIOHS14, force=True)
e = fm.register(27, fm.fpioa.GPIOHS15, force=True)
oe = fm.register(34, fm.fpioa.GPIOHS17, force=True)


latch_gpio = fm.fpioa.GPIOHS10
a_gpio = fm.fpioa.GPIOHS11
b_gpio = fm.fpioa.GPIOHS12
c_gpio = fm.fpioa.GPIOHS13
d_gpio = fm.fpioa.GPIOHS14
e_gpio = fm.fpioa.GPIOHS15
oe_gpio = fm.fpioa.GPIOHS17


height = 128
width = 128

# spi, chip_select, r1_pin, g1_pin, b1_pin, r2_pin, g2_pin, b2_pin, a_gpio, b_gpio, c_gpio, d_gpio, e_gpio, oe_gpio, latch_gpio, clk_pin, dma_channel, height, width
parameter = [1, 37, 20, 22, 21, 24, 26, 25, a_gpio, b_gpio, c_gpio, d_gpio, e_gpio, oe_gpio, latch_gpio, 32, 3, height, width]
             
show  = hub75e(parameter)

# img = image.Image()
# img = img.resize(height,width)
# print(img)
# # img.draw_circle(20,20,10,0x00F8)
# # img.draw_rectangle(00,00,30,30,0xE007)
# # img.draw_rectangle(height-25,width- 25,height - 40,height-40,(0,0,255),fill = True)

# # img.draw_rectangle(height-54,width - 54, height,width,0xe007,fill = True)
# img.draw_rectangle(0, 0 , height, width, (0,0,255), fill = True)

sensor.reset()                      # Reset and initialize the sensor. It will
                                    ## run automatically, call sensor.run(0) to stop   
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.

img = sensor.snapshot()
img = img.resize(height,width)


def on_timer(on_timer):
    global img
    img = sensor.snapshot()
    img = img.resize(height,width)

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC,
                    period=30, unit=Timer.UNIT_MS, callback=on_timer, arg = on_timer, start=True, priority=1, div=0)
                    
#lcd.init(freq=15000000)
print(img)
while True:
    # lcd.display(img)                # Display on LCD
    try:
      show.display(img)
    except Exception as e:
        print(e)
    #show.stop()
