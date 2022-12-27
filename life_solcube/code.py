# SPDX-FileCopyrightText: 2020 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# This example implements a simple two line scroller using
# Adafruit_CircuitPython_Display_Text. Each line has its own color
# and it is possible to modify the example to use other fonts and non-standard
# characters.

import random
import board
import displayio
import framebufferio
import rgbmatrix
import digitalio
import supervisor
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.pwmout import PWMOut
#import time
#import terminalio
#import adafruit_display_text.label

# The delay on the PWM cycles. Increase to slow down the LED pulsing, decrease to speed it up.
delay = 0.001

# For most boards.
i2c = board.I2C()

# For the QT Py RP2040, QT Py ESP32-S2, other boards that have SCL1/SDA1 as the STEMMA QT port.
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
arcade_qt = Seesaw(i2c, addr=0x3A)

# Button pins in order (1, 2, 3, 4)
button_pins = (18, 19, 20, 2)
buttons = []
for button_pin in button_pins:
    button = DigitalIO(arcade_qt, button_pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons.append(button)

# LED pins in order (1, 2, 3, 4)
led_pins = (12, 13, 0, 1)
leds = []
for led_pin in led_pins:
    led = PWMOut(arcade_qt, led_pin)
    leds.append(led)
    
    
# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()

# This next call creates the RGB Matrix object itself. It has the given width
# and height. bit_depth can range from 1 to 6; higher numbers allow more color
# shades to be displayed, but increase memory usage and slow down your Python
# code. If you just want to show primary colors plus black and white, use 1.
# Otherwise, try 3, 4 and 5 to see which effect you like best.
#
# These lines are for the Feather M4 Express. If you're using a different board,
# check the guide to find the pins and wiring diagrams for your board.
# If you have a matrix with a different width or height, change that too.
# If you have a 16x32 display, try with just a single line of text.
matrix = rgbmatrix.RGBMatrix(
    width=64, height=64, bit_depth=6,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1,
    tile = 2,
    serpentine = True
)

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)



conway = [
b'  +++   ',
b'  + +   ',
b'  + +   ',
b'   +    ',
b'+ +++   ',
b' + + +  ',
b'   +  + ',
b'  + +   ',
b'  + +   ',
]

solcube = [
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'        ++++++  ++++++  +     ++++  ++  ++  +++++   ++++        ',
b'        +    +  +    +  +     +  +  +    +  +    +  +  +        ',
b'        +       +    +  +     +     +    +  +    +  +           ',
b'        ++++++  +    +  +     +     +    +  +++++   ++++        ',
b'             +  +    +  +     +     +    +  +    +  +           ',
b'        +    +  +    +  +  +  +  +  +    +  +    +  +  +        ',
b'        ++++++  ++++++  ++++  ++++  ++++++  +++++   ++++        ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                ',
b'                                                                '
]

g64p2h1v0 = [
b'    +++               +++    ',
b'   +   +             +   +   ',
b'  ++    +           +    ++  ',
b' + + ++ ++   +++   ++ ++ + + ',
b'++ +    + ++ +++ ++ +    + ++',
b'    +   +    + +    +   +    ',
b'           +     +           ',
b'+       ++         ++       +'
]

g30p5h2v0 = [
b'   +       ',
b'  +++      ',
b' ++ ++     ',
b'           ',
b'+ + + +  + ',
b'+   +   +++',
b'+   +      ',
b'         + ',
b'       + + ',
b'        +  ',
b'           '
]

copperhead = [
b'++  ++',
b'  ++  ',
b'  ++  ',
b' +  + ',
b'      ',
b'      ',
b'      ',
b'++  ++',
b' ++++ ',
b'      ',
b'  ++  ',
b'  ++  '
]

spider = [
b'        +       +        ',
b'  ++ + + ++   ++ + + ++  ',
b'++ + +++         +++ + ++',
b'   + +     + +     + +   ',
b'   ++      + +      ++   ',
b'++         + +         ++',
b'++ ++               ++ ++',
b'    +               +    '
]

glider = [
b'+',
b' ',
b'+'
]

loafer = [
b'++  + +',
b'  +  ++',
b'+ +    ',
b' +     ',
b'       ',
b'     ++',
b'    +  ',
b'     + ',
b'      +'
]

lobster = [
b'           +++          ',
b'           +            ',
b'            +  ++       ',
b'               ++       ',
b'           ++           ',
b'            ++          ',
b'           +  +         ',
b'                        ',
b'             +  +       ',
b'             +   +      ',
b'              +++ +     ',
b'                   +    ',
b'+  + +             +    ',
b' + ++             +     ',
b'    +  ++             ++',
b'     +   +      ++  ++  ',
b' ++      +      +  +    ',
b' ++    + +    ++        ',
b'        +     +   +   + ',
b'         +  +    ++     ',
b'          ++   +     + +',
b'              +        +',
b'              +    +    ',
b'             +   +      ',
b'             +     ++   ',
b'              +     +   '
]

weekender = [
b'+            +',
b'+            +',
b' +          + ',
b'+            +',
b'+            +',
b' +   ++++   + ',
b'     ++++     ',
b' ++++    ++++ ',
b'              ',
b'   +      +   ',
b'    ++  ++    '
]

all_gliders = [weekender,lobster,loafer,glider,spider,g30p5h2v0,g64p2h1v0,copperhead,conway]




# do multiple things timing loop - half second, second, 2 second
# button harness i2c code
# button, when held down, brighten from 10 to 100 over time of _decay
# button method: if held down longer than _decay, trigger action
# button flash on title screen, if held down, cube_map = life
# on title:
# button 1: hold down to start life
# in life:
# button 1: clear screen, show gliders in sequence
# button 2: if glider, place glider. if life, play
# button 3: stop sim and advance 1 step (reset iterations counter n)
# button 4: flipflop: if 0, clear screen and set 1, if 1, reseed life and set 0
# buttons 1 and 4 together: return to title


# You can add more effects in this loop. For instance, maybe you want to set the
# color of each label to a different value.
i = 1
n = 1
cube_map = "title"

life_iterations = 200
button_led_timeouts=[0,0,0,0]
duty_cycle_ceiling = 65535
duty_cycle_step = 8000

button_down_step_timing = 250 #ms
step_time = -1



SCALE = 1
b1 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 2)
b2 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 2)
palette = displayio.Palette(2)
tg1 = displayio.TileGrid(b1, pixel_shader=palette)
tg2 = displayio.TileGrid(b2, pixel_shader=palette)
g1 = displayio.Group(scale=SCALE)
g1.append(tg1)
display.show(g1)
g2 = displayio.Group(scale=SCALE)
g2.append(tg2)




# Conway's "Game of Life" is played on a grid with simple rules, based
# on the number of filled neighbors each cell has and whether the cell itself
# is filled.
#   * If the cell is filled, and 2 or 3 neighbors are filled, the cell stays
#     filled
#   * If the cell is empty, and exactly 3 neighbors are filled, a new cell
#     becomes filled
#   * Otherwise, the cell becomes or remains empty
#
# The complicated way that the "m1" (minus 1) and "p1" (plus one) offsets are
# calculated is due to the way the grid "wraps around", with the left and right
# sides being connected, as well as the top and bottom sides being connected.
#
# This function has been somewhat optimized, so that when it indexes the bitmap
# a single number [x + width * y] is used instead of indexing with [x, y].
# This makes the animation run faster with some loss of clarity. More
# optimizations are probably possible.

def apply_life_rule(old, new):
    width = old.width
    height = old.height
    for y in range(height):
        yyy = y * width
        ym1 = ((y + height - 1) % height) * width
        yp1 = ((y + 1) % height) * width
        xm1 = width - 1
        for x in range(width):
            xp1 = (x + 1) % width
            neighbors = (
                old[xm1 + ym1] + old[xm1 + yyy] + old[xm1 + yp1] +
                old[x   + ym1] +                  old[x   + yp1] +
                old[xp1 + ym1] + old[xp1 + yyy] + old[xp1 + yp1])
            new[x+yyy] = neighbors == 3 or (neighbors == 2 and old[x+yyy])
            xm1 = x

# Fill 'fraction' out of all the cells.
def randomize(output, fraction=0.33):
    for i in range(output.height * output.width):
        output[i] = random.random() < fraction

def clear_output(output):
    randomize(output,-1)

# Fill the grid with a bitmap
def gridmap(output,bitst):
    for i in range(output.height * output.width):
        output[i] = 0
    for i, si in enumerate(bitst):
        y = output.height - len(bitst) - 2 + i
        for j, cj in enumerate(si):
            output[(output.width - 8)//2 + j, y] = cj & 1

def step_timing(n):
    if t > 0 and t % n == 0:
        return True
    return False

def button_held_down(btn, without_press = False, timing = button_down_step_timing):
    if without_press or buttons[btn].value:
        if button_led_timeouts[btn] > duty_cycle_ceiling:
            button_led_timeouts[btn] = 0
            return True
        elif button_led_timeouts[btn] > 0:
            if step_timing(timing):
                button_led_timeouts[btn] += duty_cycle_step
                leds[btn].duty_cycle = button_led_timeouts[btn]
    else:
        if button_led_timeouts[btn] > 0:
            button_led_timeouts[btn] -= duty_cycle_step
            leds[btn].duty_cycle = button_led_timeouts[btn]
        else:
            button_led_timeouts[btn] = 0
    return False

t = 0
while True:
    t = supervisor.ticks_ms()
    buttons_down = [
        button_held_down(0),
        button_held_down(1),
        button_held_down(2),
        button_held_down(3)
    ]
    if cube_map == "title":
        x = 1
        palette[1] = 0xffffff
        gridmap(b1,solcube)
        display.auto_refresh = True
        
        if buttons_down[0]:
            cube_map = "life":
        else:
            if step_timing(2000) and not buttons[0].value  #every 2sec flash the leftmost button
                button_held_down(0, True)

    elif cube_map == "life":
        # run 2*n generations.
        # For the Conway tribute on 64x32, 80 frames is appropriate.  For random
        # values, 400 frames seems like a good number.  Working in this way, with
        # two bitmaps, reduces copying data and makes the animation a bit faster
        while n < life_iterations:
            display.show(g1)
            apply_life_rule(b1, b2)
            display.show(g2)
            apply_life_rule(b2, b1)
            n += 1

        # After 2*n generations, fill the board with random values and
        # start over with a new color.
        randomize(b1)

        # Pick a random color out of all.    
        palette[1] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        n = 200

