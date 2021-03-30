import sensor, image, time,lcd, video,os
from modules import hub75e
from fpioa_manager import fm
from machine import Timer
print(os.listdir("/"))
width = 192
height = 128
latch = fm.register(13, fm.fpioa.GPIOHS10, force = True)
a = fm.register(8, fm.fpioa.GPIOHS11, force=True)
b = fm.register(9, fm.fpioa.GPIOHS12, force=True)
c = fm.register(10, fm.fpioa.GPIOHS13, force=True)
d = fm.register(11, fm.fpioa.GPIOHS14, force=True)
e = fm.register(7, fm.fpioa.GPIOHS15, force=True)
oe = fm.register(14, fm.fpioa.GPIOHS17, force=True)
latch_gpio = fm.fpioa.GPIOHS10
a_gpio = fm.fpioa.GPIOHS11
b_gpio = fm.fpioa.GPIOHS12
c_gpio = fm.fpioa.GPIOHS13
d_gpio = fm.fpioa.GPIOHS14
e_gpio = fm.fpioa.GPIOHS15
oe_gpio = fm.fpioa.GPIOHS17
# spi, chip_select, r1_pin, g1_pin, b1_pin, r2_pin, g2_pin, b2_pin, a_gpio, b_gpio, c_gpio, d_gpio, e_gpio, oe_gpio, latch_gpio, clk_pin, dma_channel, height, width
parameter = [0, 17, 0, 2, 1, 4, 6, 5, a_gpio, b_gpio, c_gpio, d_gpio, e_gpio, oe_gpio, latch_gpio, 12, 3, width, height]
show  = hub75e(parameter)
#lcd.init()
img = image.Image("imgs/img1.jpg")
show.display(img)
time.sleep(2)
v = video.open("badapple_320_240_15fps.avi")
while True:
    s = v.capture(img)
    print(s)
    show.display(img.resize(width, height))
    if s != 3:
        show.stop()
        break
