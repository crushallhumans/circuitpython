#solcube - 20230306
board_is_rp2040 = True

import random
import board
import displayio
import framebufferio
import rgbmatrix
import digitalio
import math
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.pwmout import PWMOut

# For most boards.
i2c = board.I2C()
arcade_qt = Seesaw(i2c, addr=0x3A)

# Button pins in order (1, 2, 3, 4)
button_pins = (18, 19, 20, 2)
buttons = []
buttons_raw = []
for button_pin in button_pins:
    button = DigitalIO(arcade_qt, button_pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons_raw.append(button)

# LED pins in order (1, 2, 3, 4)
led_pins = (12, 13, 0, 1)
leds = []
for led_pin in led_pins:
    led = PWMOut(arcade_qt, led_pin)
    leds.append(led)
    
displayio.release_displays()

bit_depth_set = 2
matrix = False

if board_is_rp2040:
    #RP2040
    matrix = rgbmatrix.RGBMatrix(
        width=64, height=64, bit_depth=bit_depth_set,
        rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
        addr_pins=[board.D25, board.D24, board.A3, board.A2],
        clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1,
        doublebuffer=True,
        tile = 2,
        serpentine = True
    )
else:
    #M4
    matrix = rgbmatrix.RGBMatrix(
        width=64, height=64, bit_depth=bit_depth_set,
        rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
        addr_pins=[board.A5, board.A4, board.A3, board.A2],
        clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1,
        tile = 2,
        serpentine = True
    )

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

# pawpatrol = [
# b'                                                                ',
# b'            ++++++++++++++++++++++++++++++++++++++++++          ',
# b'            ++++++++++++++++++++++++++++++++++++++++++          ',
# b'            ++++++++++++++++++++++++++++++++++++++++++          ',
# b'            ++++++++++++++++++++++++++++++++++++++++++          ',
# b'            ++++                                  ++++          ',
# b'            ++++                                  ++++          ',
# b'            ++++                                  ++++          ',
# b'            ++++                                  ++++          ',
# b'      ++++++++++           ++++++++++             ++++++++++    ',
# b'      +++++++              ++++++++++                +++++++    ',
# b'      +++++++              ++++++++++                +++++++    ',
# b'      +++++++           +++++++++++++++  +++++++     +++++++    ',
# b'      ++++              ++++        +++  +++++++        ++++    ',
# b'      ++++              ++++        +++  +++++++        ++++    ',
# b'      ++++              ++++        +++++++++++++++     ++++    ',
# b'      ++++              ++++        ++++++     ++++     ++++    ',
# b'      ++++              ++++        ++++++     ++++     ++++    ',
# b'      ++++     +++++++++++++        ++++++     +++++++  ++++    ',
# b'      ++++     +++++++++++++        +++           ++++  ++++    ',
# b'      ++++     +++++++++++++        +++           ++++  ++++    ',
# b'      ++++  +++++++++++++++++++     +++           ++++  ++++    ',
# b'      ++++  ++++           ++++     +++           ++++  ++++    ',
# b'      ++++  ++++           ++++     +++           ++++  ++++    ',
# b'      ++++  ++++           ++++++++++++     ++++++++++  ++++    ',
# b'      ++++  ++++              +++++++++     +++++++     ++++    ',
# b'      ++++  ++++              +++++++++     +++++++     ++++    ',
# b'      ++++  +++++++        ++++++++++++++++++++++++     ++++    ',
# b'      ++++     ++++        ++++       +++++++           ++++    ',
# b'      ++++     ++++        ++++       +++++++           ++++    ',
# b'      +++++++  +++++++  +++++++       ++++++++++     +++++++    ',
# b'         ++++     ++++  ++++                ++++     ++++       ',
# b'         ++++     ++++  ++++                ++++     ++++       ',
# b'         ++++     ++++++++++                ++++     ++++       ',
# b'         ++++        ++++                   ++++     ++++       ',
# b'         ++++        ++++                   ++++     ++++       ',
# b'         ++++        ++++                   ++++     ++++       ',
# b'         ++++        ++++                   ++++     ++++       ',
# b'         +++++++     ++++                   ++++  +++++++       ',
# b'            ++++     ++++                   ++++  ++++          ',
# b'            ++++     ++++                   ++++  ++++          ',
# b'            ++++     +++++++     +++++++++++++++  ++++          ',
# b'            ++++        ++++     ++++++++++++     ++++          ',
# b'            ++++        ++++     ++++++++++++     ++++          ',
# b'            +++++++     +++++++++++++++++++++  +++++++          ',
# b'               ++++        +++++++             ++++             ',
# b'               ++++        +++++++             ++++             ',
# b'               +++++++     +++++++          +++++++             ',
# b'                  ++++                      ++++                ',
# b'                  ++++                      ++++                ',
# b'                  +++++++                +++++++                ',
# b'                     ++++                ++++                   ',
# b'                     ++++                ++++                   ',
# b'                     +++++++          +++++++                   ',
# b'                        ++++          ++++                      ',
# b'                        ++++          ++++                      ',
# b'                        +++++++     ++++++                      ',
# b'                           ++++     +++                         ',
# b'                           ++++     +++                         ',
# b'                           ++++++++++++                         ',
# b'                              +++++++                           ',
# b'                              +++++++                           ',
# b'                              +++++++                           ',
# b'                                                                ',
# ]

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
            n[row][col] = j
            row += 1
        col -= 1
    nn = []
    for i in n:
        nn.append(''.join(i))
    return nn

unrotated_gliders = [weekender,lobster,loafer,glider,spider,g30p5h2v0,g64p2h1v0,copperhead,conway]
rotated_gliders = []
all_gliders = []

# add 3 copies of each glider, each rotated +90deg
for i in unrotated_gliders:
    n = i.copy()
    rotated_gliders.append(n)
    nn = n.copy()
    for j in range(3):
        nn = rotate_bitmatrix(nn.copy())
        rotated_gliders.append(nn)
    i = []

for i in rotated_gliders:
    # pad all gliders with 12 extra spaces and 8 extra lines
    # add a box around them too
    padded = []
    padded_width = 0
    alternate = True
    for j in i:
        jj = '       ' + j
        jj = jj + '       '
        box = ' '
        if alternate:
            box = '+'
            alternate = False
        else:
            alternate = True
        jj = box + jj + box
        padded_width = len(jj)
        padded.append(str.encode(jj))

    vertical_spacer =   (' ' * (padded_width - 2))
    vertical_box =      (' +' * (padded_width//2))

    b = ' '
    padded.insert(0,str.encode(b + vertical_spacer + b))
    b = '+'
    padded.insert(0,str.encode(b + vertical_spacer + b))
    b = ' '
    padded.insert(0,str.encode(b + vertical_spacer + b))
    b = '+'
    padded.insert(0,str.encode(b + vertical_spacer + b))
    b = ' '
    padded.insert(0,str.encode(b + vertical_spacer + b))
    padded.insert(0,str.encode(vertical_box))

    b = '+'
    padded.append(str.encode(b + vertical_spacer + b))
    b = ' '
    padded.append(str.encode(b + vertical_spacer + b))
    b = '+'
    padded.append(str.encode(b + vertical_spacer + b))
    b = ' '
    padded.append(str.encode(b + vertical_spacer + b))
    b = '+'
    padded.append(str.encode(b + vertical_spacer + b))
    padded.append(str.encode(vertical_box))

    all_gliders.append(padded.copy())
    i = []

del(unrotated_gliders)
del(rotated_gliders)


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
duty_cycle_ceiling = 65535
duty_cycle_step = 8000

b1 = displayio.Bitmap(display.width, display.height, 2)
b2 = displayio.Bitmap(display.width, display.height, 2)
palette = displayio.Palette(2)
tg1 = displayio.TileGrid(b1, pixel_shader=palette)
tg2 = displayio.TileGrid(b2, pixel_shader=palette)
g1 = displayio.Group()
g1.append(tg1)
display.show(g1)
g2 = displayio.Group()
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
    for c_y in range(height):
        yyy = c_y * width
        ym1 = ((c_y + height - 1) % height) * width
        yp1 = ((c_y + 1) % height) * width
        xm1 = width - 1
        for c_x in range(width):
            xp1 = (c_x + 1) % width
            neighbors = (
                old[xm1 + ym1]      + old[xm1 + yyy]    + old[xm1 + yp1] +
                old[c_x + ym1]      +                     old[c_x + yp1] +
                old[xp1 + ym1]      + old[xp1 + yyy]    + old[xp1 + yp1])
            new[c_x+yyy] = neighbors == 3 or (neighbors == 2 and old[c_x+yyy])
            xm1 = c_x

# Fill 'fraction' out of all the cells.
def randomize(output, fraction=0.33):
    for i in range(output.height * output.width):
        output[i] = random.random() < fraction

def clear_output(output):
    for i in range(output.height * output.width):
        output[i] = 0

# Fill the grid with a bitmap
def gridmap(output,bitst,rando=False):
    x_offset = 0 #(output.width - len(bitst[0]))//2
    y_offset = 0
    if rando:
        x_offset = math.floor(random.random() * (output.width  - len(bitst[0])))
        y_offset = math.floor(random.random() * (output.height - len(bitst)))
    for i, si in enumerate(bitst):
        y = output.height - len(bitst) - y_offset + i
        for j, cj in enumerate(si):
            x = x_offset + j
            try:
                output[x, y] = cj & 1
            except IndexError as e:
                print(x,y,x_offset,y_offset,output.width,output.height,e)

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

def nonblack_randomcolor():
    r = 0
    g = 0
    b = 0
    while not (r or g or b):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
    return (r,g,b)

def button_off(btn):
    leds[btn].duty_cycle = 0



clear_output(b1)
go = True
sparse = True
palette[1] = 0xff0000
up = True

while True:
    if cube_map == 0 or cube_map == 2:
        if not buttons_raw[0].value:
            cube_map = 1
            palette[1] = nonblack_randomcolor()
            button_off(0)
        else:
            button_off(2)
            button_light_pulse(0, True)
            
            gridmap(b1,solcube)
            #gridmap(b1,solcube if cube_map == 0 else pawpatrol)
            display.auto_refresh = True
            
            go = True
            advance = False

    elif cube_map == 1:
        # run 2*n generations.
        # For the Conway tribute on 64x32, 80 frames is appropriate.  For random
        # values, 400 frames seems like a good number.  Working in this way, with
        # two bitmaps, reduces copying data and makes the animation a bit faster

        if n < life_iterations:
            if not buttons_raw[0].value: # drop a random glider on the board
                if up:
                    gridmap(b1,random.choice(all_gliders),True)
                else:
                    gridmap(b2,random.choice(all_gliders),True)
                n = 0
            if not buttons_raw[1].value: # restart continuous playback
                go = True
                advance = False
            if not buttons_raw[2].value: # halt playback and advance 1
                go = False
                advance = True
            if not buttons_raw[3].value: # 0: new rando board. 1: PAW Patrol, flipflop
                n = 0
                if sparse:
                    clear_output(b1)
                    palette[1] = 0xff0000
                    display.show(g1)

                    gridmap(b1,solcube)
                    # gridmap(b1,pawpatrol)
                    cube_map = 2 # go back to initial phase

                    go = False
                    advance = False
                    sparse = False
                else:
                    clear_output(b1)
                    randomize(b1,0.33)
                    palette[1] = nonblack_randomcolor()
                    go = True
                    advance = False
                    sparse = True

            if not go:
                dc,state = button_light_pulse(2, True)
            else:
                button_off(2)


            if go or advance:
                advance = False
                if (n > 0) and ((n % 35) == 0):
                    if up:
                        display.show(g1)
                        gridmap(b1,random.choice(all_gliders),True)
                    else:
                        display.show(g2)
                        gridmap(b2,random.choice(all_gliders),True)
                else:
                    if up:
                        display.show(g1)
                        apply_life_rule(b1, b2)
                        up = False
                    else:
                        display.show(g2)
                        apply_life_rule(b2, b1)
                        up = True

                n += 1
        else:
            # After 2*n generations, fill the board with random values and
            # start over with a new color.
            clear_output(b1)
            randomize(b1)

            # Pick a random color out of all.    
            palette[1] = nonblack_randomcolor()

            n = 0


# gliders = """
# !Name: Glider
# !Author: Richard K. Guy
# !The smallest, most common, and first discovered spaceship.
# !www.conwaylife.com/wiki/index.php?title=Glider
# .O.
# ..O
# OOO

# !Name: 64P2H1V0
# !Author: Dean Hickerson
# !The smallest period 2 spaceship, discovered on July 28, 1989
# !www.conwaylife.com/wiki/index.php?title=64P2H1V0
# .....OOO...............OOO.....
# ....O...O.............O...O....
# ...OO....O...........O....OO...
# ..O.O.OO.OO...OOO...OO.OO.O.O..
# .OO.O....O.OO.OOO.OO.O....O.OO.
# O....O...O....O.O....O...O....O
# ............O.....O............
# OO.......OO.........OO.......OO

# !Name: 30P5H2V0
# !Author: Paul Tooke
# !An orthogonal spaceship with period 5. The smallest known 2c/5 spaceship.
# !www.conwaylife.com/wiki/index.php?title=30P5H2V0
# ....O........
# ...OOO.......
# ..OO.OO......
# .............
# .O.O.O.O..O..
# OO...O...OOO.
# OO...O......O
# ..........O.O
# ........O.O..
# .........O..O
# ............O

# ! lobster.cells
# ! Matthias Merzenich, 2011
# ! https://conwaylife.com/wiki/Lobster_(spaceship)
# ! https://www.conwaylife.com/patterns/lobster.cells
# ............OOO...........
# ............O.............
# .............O..OO........
# ................OO........
# ............OO............
# .............OO...........
# ............O..O..........
# ..........................
# ..............O..O........
# ..............O...O.......
# ...............OOO.O......
# ....................O.....
# OO..O.O.............O.....
# O.O.OO.............O......
# O....O..OO.............OO.
# ......O...O......OO..OO..O
# ..OO......O......O..O.....
# ..OO....O.O....OO.........
# .........O.....O...O...O..
# ..........O..O....OO......
# ...........OO...O.....O.O.
# ...............O........OO
# ...............O....O.....
# ..............O...O.......
# ..............O.....OO....
# ...............O.....O....

# !Name: Spider
# !Author: David Bell
# !A c/5 period 5 orthogonal spaceship found in April 1997. It is the smallest known c/5 spaceship.
# !www.conwaylife.com/wiki/index.php?title=Spider
# .........O.......O.........
# ...OO.O.O.OO...OO.O.O.OO...
# OOO.O.OOO.........OOO.O.OOO
# O...O.O.....O.O.....O.O...O
# ....OO......O.O......OO....
# .OO.........O.O.........OO.
# .OO.OO...............OO.OO.
# .....O...............O.....

# ! loafer.cells
# ! Josh Ball
# ! small c/7 orthogonal spaceship found 17 February 2013
# ! https://www.conwaylife.com/forums/viewtopic.php?f=2&t=1031#p7450
# ! https://conwaylife.com/wiki/Loafer
# .OO..O.OO
# O..O..OO.
# .O.O.....
# ..O......
# ........O
# ......OOO
# .....O...
# ......O..
# .......OO

# ! Copperhead
# ! 'zdr'
# ! An c/10 orthogonal spaceship found on March 5, 2016.
# ! https://www.conwaylife.com/wiki/Copperhead
# .OO..OO.
# ...OO...
# ...OO...
# O.O..O.O
# O......O
# ........
# O......O
# .OO..OO.
# ..OOOO..
# ........
# ...OO...
# ...OO...

# !Name: Weekender
# !Author: David Eppstein
# !A period 7 spaceship with speed 2c/7.
# !www.conwaylife.com/wiki/index.php?title=Weekender
# .O............O.
# .O............O.
# O.O..........O.O
# .O............O.
# .O............O.
# ..O...OOOO...O..
# ......OOOO......
# ..OOOO....OOOO..
# ................
# ....O......O....
# .....OO..OO.....
# """