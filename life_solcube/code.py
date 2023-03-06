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
import time
import math
from adafruit_debouncer import Debouncer
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
    buttons.append(Debouncer(button, interval = 0.005))

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

#RP2040
matrix = rgbmatrix.RGBMatrix(
    width=64, height=64, bit_depth=6,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.D25, board.D24, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1,
    doublebuffer=True,
    tile = 2,
    serpentine = True
)



#M4
# matrix = rgbmatrix.RGBMatrix(
#     width=64, height=64, bit_depth=6,
#     rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
#     addr_pins=[board.A5, board.A4, board.A3, board.A2],
#     clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1,
#     tile = 2,
#     serpentine = True
# )

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)



solcube = [
b'         ++++++++++++++++              ++++++++++++++++         ',
b'         ++++++++++++++++              ++++++++++++++++         ',
b'         ++++++++++++++++              ++++++++++++++++         ',
b'         ++++++++++++++++              ++++++++++++++++         ',
b'         ++++++++++++++++              ++++++++++++++++         ',
b'     +++++              ++++++    ++++++              +++++     ',
b'     +++++              ++++++    ++++++              +++++     ',
b'     +++++              ++++++    ++++++              +++++     ',
b'     +++++              ++++++    ++++++              +++++     ',
b'     +++++               +++++    +++++               +++++     ',
b'+++++                    ++++++++++++++               ++++++++++',
b'+++++                        +++++                         +++++',
b'+++++                        +++++                         +++++',
b'+++++                        +++++                         +++++',
b'+++++                        +++++                         +++++',
b'+++++                        +++++                         +++++',
b'+++++                                                      +++++',
b'+++++   ++++++  ++++++  +     ++++  +    +  +++++   ++++   +++++',
b'+++++   +    +  +    +  +     +  +  +    +  +    +  +  +   +++++',
b'+++++   +       +    +  +     +     +    +  +    +  +      +++++',
b'+++++   +       +    +  +     +     +    +  +    +  +      +++++',
b'+++++   +       +    +  +     +     +    +  +    +  +      +++++',
b'+++++   +       +    +  +     +     +    +  +    +  +      +++++',
b'+++++   ++++++  +    +  +     +     +    +  +++++   +++    +++++',
b'+++++        +  +    +  +     +     +    +  +    +  +      +++++',
b'+++++        +  +    +  +     +     +    +  +    +  +      +++++',
b'+++++        +  +    +  +     +     +    +  +    +  +      +++++',
b'+++++        +  +    +  +     +     +    +  +    +  +      +++++',
b'+++++        +  +    +  +     +     +    +  +    +  +      +++++',
b'+++++   +    +  +    +  +  +  +  +  +    +  +    +  +  +   +++++',
b'+++++   ++++++  ++++++  ++++  ++++  ++++++  +++++   ++++   +++++',
b'+++++                                                     ++++++',
b'     +++++                                            +++++     ',
b'     +++++                                            +++++     ',
b'     +++++                                            +++++     ',
b'     +++++                                            +++++     ',
b'     +++++                                           ++++++     ',
b'     ++++++++++                                  ++++++++++     ',
b'         ++++++                                  ++++++         ',
b'         ++++++                                  ++++++         ',
b'         ++++++                                  ++++++         ',
b'         ++++++                                  ++++++         ',
b'          +++++                             ++++++++++          ',
b'              ++++++                        ++++++              ',
b'              ++++++                        ++++++              ',
b'              ++++++                        ++++++              ',
b'              ++++++                        ++++++              ',
b'              ++++++                   +++++++++++              ',
b'                   ++++++              ++++++                   ',
b'                   ++++++              ++++++                   ',
b'                   ++++++              ++++++                   ',
b'                   ++++++              ++++++                   ',
b'                   ++++++              ++++++                   ',
b'                    +++++++++      +++++++++                    ',
b'                        ++++++    ++++++                        ',
b'                        ++++++    ++++++                        ',
b'                        ++++++    ++++++                        ',
b'                        ++++++    ++++++                        ',
b'                        ++++++++++++++++                        ',
b'                             ++++++                             ',
b'                             ++++++                             ',
b'                             ++++++                             ',
b'                             ++++++                             ',
b'                             ++++++                             ',
]

pawpatrol = [
b'                                                                ',
b'            ++++++++++++++++++++++++++++++++++++++++++          ',
b'            ++++++++++++++++++++++++++++++++++++++++++          ',
b'            ++++++++++++++++++++++++++++++++++++++++++          ',
b'            ++++++++++++++++++++++++++++++++++++++++++          ',
b'            ++++                                  ++++          ',
b'            ++++                                  ++++          ',
b'            ++++                                  ++++          ',
b'            ++++                                  ++++          ',
b'      ++++++++++           ++++++++++             ++++++++++    ',
b'      +++++++              ++++++++++                +++++++    ',
b'      +++++++              ++++++++++                +++++++    ',
b'      +++++++           +++++++++++++++  +++++++     +++++++    ',
b'      ++++              ++++        +++  +++++++        ++++    ',
b'      ++++              ++++        +++  +++++++        ++++    ',
b'      ++++              ++++        +++++++++++++++     ++++    ',
b'      ++++              ++++        ++++++     ++++     ++++    ',
b'      ++++              ++++        ++++++     ++++     ++++    ',
b'      ++++     +++++++++++++        ++++++     +++++++  ++++    ',
b'      ++++     +++++++++++++        +++           ++++  ++++    ',
b'      ++++     +++++++++++++        +++           ++++  ++++    ',
b'      ++++  +++++++++++++++++++     +++           ++++  ++++    ',
b'      ++++  ++++           ++++     +++           ++++  ++++    ',
b'      ++++  ++++           ++++     +++           ++++  ++++    ',
b'      ++++  ++++           ++++++++++++     ++++++++++  ++++    ',
b'      ++++  ++++              +++++++++     +++++++     ++++    ',
b'      ++++  ++++              +++++++++     +++++++     ++++    ',
b'      ++++  +++++++        ++++++++++++++++++++++++     ++++    ',
b'      ++++     ++++        ++++       +++++++           ++++    ',
b'      ++++     ++++        ++++       +++++++           ++++    ',
b'      +++++++  +++++++  +++++++       ++++++++++     +++++++    ',
b'         ++++     ++++  ++++                ++++     ++++       ',
b'         ++++     ++++  ++++                ++++     ++++       ',
b'         ++++     ++++++++++                ++++     ++++       ',
b'         ++++        ++++                   ++++     ++++       ',
b'         ++++        ++++                   ++++     ++++       ',
b'         ++++        ++++                   ++++     ++++       ',
b'         ++++        ++++                   ++++     ++++       ',
b'         +++++++     ++++                   ++++  +++++++       ',
b'            ++++     ++++                   ++++  ++++          ',
b'            ++++     ++++                   ++++  ++++          ',
b'            ++++     +++++++     +++++++++++++++  ++++          ',
b'            ++++        ++++     ++++++++++++     ++++          ',
b'            ++++        ++++     ++++++++++++     ++++          ',
b'            +++++++     +++++++++++++++++++++  +++++++          ',
b'               ++++        +++++++             ++++             ',
b'               ++++        +++++++             ++++             ',
b'               +++++++     +++++++          +++++++             ',
b'                  ++++                      ++++                ',
b'                  ++++                      ++++                ',
b'                  +++++++                +++++++                ',
b'                     ++++                ++++                   ',
b'                     ++++                ++++                   ',
b'                     +++++++          +++++++                   ',
b'                        ++++          ++++                      ',
b'                        ++++          ++++                      ',
b'                        +++++++     ++++++                      ',
b'                           ++++     +++                         ',
b'                           ++++     +++                         ',
b'                           ++++++++++++                         ',
b'                              +++++++                           ',
b'                              +++++++                           ',
b'                              +++++++                           ',
b'                                                                ',
]

conway = [
'  +++   ',
'  + +   ',
'  + +   ',
'   +    ',
'+ +++   ',
' + + +  ',
'   +  + ',
'  + +   ',
'  + +   ',
]


solcube_2 = [
'                                                  ',
' ++++++  ++++++  +     ++++  ++  ++  +++++   ++++ ',
' +    +  +    +  +     +  +  +    +  +    +  +    ',
' +       +    +  +     +     +    +  +    +  +    ',
' ++++++  +    +  +     +     +    +  +++++   ++++ ',
'      +  +    +  +     +     +    +  +    +  +    ',
' +    +  +    +  +  +  +  +  +    +  +    +  +    ',
' ++++++  ++++++  ++++  ++++  ++++++  +++++   ++++ ',
'                                                  '
]

glider = [
' + ',
'  +',
'+++',
]

g64p2h1v0 = [
'     +++               +++     ',
'    +   +             +   +    ',
'   ++    +           +    ++   ',
'  + + ++ ++   +++   ++ ++ + +  ',
' ++ +    + ++ +++ ++ +    + ++ ',
'+    +   +    + +    +   +    +',
'            +     +            ',
'++       ++         ++       ++',
]

g30p5h2v0 = [
'    +        ',
'   +++       ',
'  ++ ++      ',
'             ',
' + + + +  +  ',
'++   +   +++ ',
'++   +      +',
'          + +',
'        + +  ',
'         +  +',
'            +',
]

lobster = [
'            +++           ',
'            +             ',
'             +  ++        ',
'                ++        ',
'            ++            ',
'             ++           ',
'            +  +          ',
'                          ',
'              +  +        ',
'              +   +       ',
'               +++ +      ',
'                    +     ',
'++  + +             +     ',
'+ + ++             +      ',
'+    +  ++             ++ ',
'      +   +      ++  ++  +',
'  ++      +      +  +     ',
'  ++    + +    ++         ',
'         +     +   +   +  ',
'          +  +    ++      ',
'           ++   +     + + ',
'               +        ++',
'               +    +     ',
'              +   +       ',
'              +     ++    ',
'               +     +    ',
]

spider = [
'         +       +         ',
'   ++ + + ++   ++ + + ++   ',
'+++ + +++         +++ + +++',
'+   + +     + +     + +   +',
'    ++      + +      ++    ',
' ++         + +         ++ ',
' ++ ++               ++ ++ ',
'     +               +     ',
]

loafer = [
' ++  + ++',
'+  +  ++ ',
' + +     ',
'  +      ',
'        +',
'      +++',
'     +   ',
'      +  ',
'       ++',
]

copperhead = [
' ++  ++ ',
'   ++   ',
'   ++   ',
'+ +  + +',
'+      +',
'        ',
'+      +',
' ++  ++ ',
'  ++++  ',
'        ',
'   ++   ',
'   ++   ',
]

weekender = [
' +            + ',
' +            + ',
'+ +          + +',
' +            + ',
' +            + ',
'  +   ++++   +  ',
'      ++++      ',
'  ++++    ++++  ',
'                ',
'    +      +    ',
'     ++  ++     ',
]


def rotate_bitmatrix(g):
    col = len(g)
    row = len(g[0])
    n = [[' ' for i in range(col)] for j in range(row)]
    col -= 1
    for i in g:
        row = 0
        for j in i:
            n[row][col] = chr(j)
            row += 1
        col -= 1
    nn = []
    for i in n:
        nn.append(str.encode(''.join(i)))
    return nn

unrotated_gliders = [weekender,lobster,loafer,glider,spider,g30p5h2v0,g64p2h1v0,copperhead,conway,solcube_2]
all_gliders = []

for i in unrotated_gliders:
    # pad all gliders with 12 extra spaces and 8 extra lines, and a box
    padded = []
    padded_width = 0
    for j in i:
        j = '      ' + j
        j = j + '      '
        padded_width = len(j)
        padded.append(str.encode(j))
    vertical_spacer = str.encode(' ' * padded_width)
    padded.insert(0,vertical_spacer)
    padded.insert(0,vertical_spacer)
    padded.insert(0,vertical_spacer)
    padded.insert(0,vertical_spacer)
    padded.append(vertical_spacer)
    padded.append(vertical_spacer)
    padded.append(vertical_spacer)
    padded.append(vertical_spacer)
#    vertical_spacer_x = str.encode('+' * padded_width)
#    padded.insert(0,vertical_spacer_x)
#    padded.append(vertical_spacer_x)

    all_gliders.append(padded.copy())

    # add 3 copies of each glider, each rotated +90deg
    n = padded
    for j in range(3):
        n = rotate_bitmatrix(n.copy())
        all_gliders.append(n.copy())



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
n = 0
cube_map = 0

life_iterations = 300
button_led_timeouts=[0,0,0,0]
button_led_direction=[0,0,0,0]
button_debounce_timeout = [0,0,0,0]
debounce_threshold = 1
duty_cycle_ceiling = 65535
duty_cycle_step = 8000

button_down_step_timing = 250 #ms
button_down_fast_step = 100 #ms



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
    for i in range(output.height * output.width):
        output[i] = 0

# Fill the grid with a bitmap
def gridmap(output,bitst,rando=False):
    x_offset = (output.width - len(bitst[0]))//2
    y_offset = 0
    if rando:
        x_offset = math.floor(random.random() * (output.width  - len(bitst[0])))
        y_offset = math.floor(random.random() * (output.height - len(bitst)))
        #print("x_offset,y_offset",x_offset,y_offset) 
    for i, si in enumerate(bitst):
        y = output.height - len(bitst) - y_offset + i
        #print("row " + str(i) + " at " + str(y) + ", " + str(output.height) + ", " +  str(len(bitst)))
        for j, cj in enumerate(si):
            x = x_offset + j
#            print("col " + str(j) + " at " + str(x))
            output[x, y] = cj & 1

def button_light_pulse(btn, without_press = False):
    state = -1
    if without_press or not buttons[btn].value:
        if button_led_direction[btn] == 0: # up
            if button_led_timeouts[btn] >= duty_cycle_ceiling:
                button_led_direction[btn] = 1 # switch to down
                state = 3
            elif button_led_timeouts[btn] >= 0:
                button_led_timeouts[btn] += duty_cycle_step
                leds[btn].duty_cycle = button_led_timeouts[btn] if button_led_timeouts[btn] < duty_cycle_ceiling else duty_cycle_ceiling
                state = 2
        else: # down
            if button_led_timeouts[btn] > 0:
                button_led_timeouts[btn] -= duty_cycle_step
                leds[btn].duty_cycle = button_led_timeouts[btn] if button_led_timeouts[btn] > 0 else 0
                state = 1
            else:
                button_led_timeouts[btn] = 0
                button_led_direction[btn] = 0 # switch to up
                state = 0

    return button_led_timeouts[btn], state

def button_off(btn):
    leds[btn].duty_cycle = 0

def button_pushed(btn):
    buttons[btn].update()
    if buttons[btn].fell:
        leds[btn].duty_cycle = duty_cycle_ceiling
        return True 
        if button_debounce_timeout[btn] > debounce_threshold:
            button_led_timeouts[btn] = duty_cycle_ceiling
            leds[btn].duty_cycle = button_led_timeouts[btn] if button_led_timeouts[btn] < duty_cycle_ceiling else duty_cycle_ceiling
            button_debounce_timeout[btn] = 0
            return True 
        else:
            button_debounce_timeout[btn] += 1
            return False
    elif buttons[btn].rose:
        leds[btn].duty_cycle = 0
        return False
        if button_debounce_timeout[btn] > 0:
            button_led_timeouts[btn] = 0
            leds[btn].duty_cycle = button_led_timeouts[btn]
            button_debounce_timeout[btn] = 0

ticks = 0
start_time = supervisor.ticks_ms()
flash = 0
clear_output(b1)
last_flash_time = start_time
go = True
sparse = True
palette[1] = 0xff0000

while True:
    buttons_down = [
        button_pushed(0),
        button_pushed(1),
        button_pushed(2),
        button_pushed(3),
    ]
    if cube_map == 0 or cube_map == 2:
        if buttons_down[0]:
            cube_map = 1
            palette[1] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            button_off(0)
#            clear_output(b1)
#            randomize(b1)
        else:
            #print(str(flash))
            dc = -1
            if flash > 2000:  #every 2sec flash the leftmost button
                dc,state = button_light_pulse(0, True)
                #print(str(flash) + " dc " + str(dc) + ', state: ' + str(state))
            if flash > 0 and dc == 0:
                last_flash_time = supervisor.ticks_ms()
                flash = 0

            gridmap(b1,solcube if cube_map == 0 else pawpatrol)
            display.auto_refresh = True
            
            ticks = supervisor.ticks_ms()
            flash += ticks - last_flash_time
            go = True
            advance = False

    elif cube_map == 1:
        # run 2*n generations.
        # For the Conway tribute on 64x32, 80 frames is appropriate.  For random
        # values, 400 frames seems like a good number.  Working in this way, with
        # two bitmaps, reduces copying data and makes the animation a bit faster

        if n < life_iterations:
            if buttons_down[0]: # drop a random glider on the board
                gridmap(b1,random.choice(all_gliders),True)
            if buttons_down[1]: # restart continuous playback
                go = True
                advance = False
            if buttons_down[2]: # halt playback and advance 1
                go = False
                advance = True
            if buttons_down[3]: # 0: new rando board. 1: PAW Patrol, flipflop
                n = 0
                if sparse:
                    clear_output(b1)
                    palette[1] = 0xff0000
                    display.show(g1)
                    print('display.show(g1)')
                    gridmap(b1,pawpatrol)
                    print('gridmap(b1,pawpatrol)')
                    #display.show(g2)
                    #print('display.show(g2)')
                    cube_map = 2 # go back to initial phase
                    go = False
                    advance = False
                    sparse = False
                else:
                    clear_output(b1)
                    randomize(b1,0.33)
                    palette[1] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    go = True
                    advance = False
                    sparse = True

            if go or advance:
                advance = False
                if (n > 0) and ((n % 20) == 0):
                    display.show(g1)
                    gridmap(b1,random.choice(all_gliders),True)
                    display.show(g2)
                else:
                    display.show(g1)
                    apply_life_rule(b1, b2)
                    display.show(g2)
                    apply_life_rule(b2, b1)

                n += 1
        else:
            # After 2*n generations, fill the board with random values and
            # start over with a new color.
            clear_output(b1)
            randomize(b1)

            # Pick a random color out of all.    
            palette[1] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

            n = 0


gliders = """
!Name: Glider
!Author: Richard K. Guy
!The smallest, most common, and first discovered spaceship.
!www.conwaylife.com/wiki/index.php?title=Glider
.O.
..O
OOO

!Name: 64P2H1V0
!Author: Dean Hickerson
!The smallest period 2 spaceship, discovered on July 28, 1989
!www.conwaylife.com/wiki/index.php?title=64P2H1V0
.....OOO...............OOO.....
....O...O.............O...O....
...OO....O...........O....OO...
..O.O.OO.OO...OOO...OO.OO.O.O..
.OO.O....O.OO.OOO.OO.O....O.OO.
O....O...O....O.O....O...O....O
............O.....O............
OO.......OO.........OO.......OO

!Name: 30P5H2V0
!Author: Paul Tooke
!An orthogonal spaceship with period 5. The smallest known 2c/5 spaceship.
!www.conwaylife.com/wiki/index.php?title=30P5H2V0
....O........
...OOO.......
..OO.OO......
.............
.O.O.O.O..O..
OO...O...OOO.
OO...O......O
..........O.O
........O.O..
.........O..O
............O

! lobster.cells
! Matthias Merzenich, 2011
! https://conwaylife.com/wiki/Lobster_(spaceship)
! https://www.conwaylife.com/patterns/lobster.cells
............OOO...........
............O.............
.............O..OO........
................OO........
............OO............
.............OO...........
............O..O..........
..........................
..............O..O........
..............O...O.......
...............OOO.O......
....................O.....
OO..O.O.............O.....
O.O.OO.............O......
O....O..OO.............OO.
......O...O......OO..OO..O
..OO......O......O..O.....
..OO....O.O....OO.........
.........O.....O...O...O..
..........O..O....OO......
...........OO...O.....O.O.
...............O........OO
...............O....O.....
..............O...O.......
..............O.....OO....
...............O.....O....

!Name: Spider
!Author: David Bell
!A c/5 period 5 orthogonal spaceship found in April 1997. It is the smallest known c/5 spaceship.
!www.conwaylife.com/wiki/index.php?title=Spider
.........O.......O.........
...OO.O.O.OO...OO.O.O.OO...
OOO.O.OOO.........OOO.O.OOO
O...O.O.....O.O.....O.O...O
....OO......O.O......OO....
.OO.........O.O.........OO.
.OO.OO...............OO.OO.
.....O...............O.....

! loafer.cells
! Josh Ball
! small c/7 orthogonal spaceship found 17 February 2013
! https://www.conwaylife.com/forums/viewtopic.php?f=2&t=1031#p7450
! https://conwaylife.com/wiki/Loafer
.OO..O.OO
O..O..OO.
.O.O.....
..O......
........O
......OOO
.....O...
......O..
.......OO

! Copperhead
! 'zdr'
! An c/10 orthogonal spaceship found on March 5, 2016.
! https://www.conwaylife.com/wiki/Copperhead
.OO..OO.
...OO...
...OO...
O.O..O.O
O......O
........
O......O
.OO..OO.
..OOOO..
........
...OO...
...OO...

!Name: Weekender
!Author: David Eppstein
!A period 7 spaceship with speed 2c/7.
!www.conwaylife.com/wiki/index.php?title=Weekender
.O............O.
.O............O.
O.O..........O.O
.O............O.
.O............O.
..O...OOOO...O..
......OOOO......
..OOOO....OOOO..
................
....O......O....
.....OO..OO.....
"""