# MACROPAD Hotkeys example: Consumer Control codes (media keys)

# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
# You can still import Keycode as well if a macro file mixes types!
# See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'FKeys', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xffffff, 'F24', [Keycode.F24]),
        (0xffffff, 'F23', [Keycode.F23]),
        (0xffffff, 'F22', [Keycode.F22]),
        # 2nd row ----------
        (0xffffff, 'F21', [Keycode.F21]),
        (0xffffff, 'F20', [Keycode.F20]),
        (0xffffff, 'F19', [Keycode.F19]),
        # 3rd row ----------
        (0xffffff, 'F18', [Keycode.F18]),
        (0xffffff, 'F17', [Keycode.F17]),
        (0xffffff, 'F16', [Keycode.F16]),
        # 4th row ----------
        (0xffffff, 'F15', [Keycode.F15]),
        (0xffffff, 'F14', [Keycode.F14]),
        (0xffffff, 'F13', [Keycode.F13]),
        # Encoder button ---
        (0xffffff, '', [Keycode.CAPS_LOCK])
    ]
}
