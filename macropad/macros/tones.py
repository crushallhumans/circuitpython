# MACROPAD Hotkeys example: Tones

# The syntax for Tones in macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse and
# tone further complicate this by adding dicts-within-list. Each tone-related
# item is the key 'tone' with either an integer frequency value, or 0 to stop
# the tone mid-macro (tone is also stopped when key is released).
# Helpful: https://en.wikipedia.org/wiki/Piano_key_frequencies

# This example ONLY shows tones (and delays), but really they can be mixed
# with other elements (keys, codes, mouse) to provide auditory feedback.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Tones', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000110, 'e5', [{'tone':659}]),
        (0x000011, 'f5', [{'tone':698}]),
        (0x010101, 'g5', [{'tone':784}]),
        # 2nd row ----------
        (0x110000, 'b4', [{'tone':494}]),
        (0x011000, 'c5', [{'tone':523}]),
        (0x001100, 'd5', [{'tone':587}]),
        # 3rd row ----------
        (0x000100, 'f4', [{'tone':349}]),
        (0x000010, 'g4', [{'tone':392}]),
        (0x000001, 'a4', [{'tone':440}]),
        # 4th row ----------
        (0x100000, 'c4', [{'tone':262}]),
        (0x010000, 'd4', [{'tone':294}]),
        (0x001000, 'e4', [{'tone':330}]),
        # Encoder button ---
        (0x000000, '', [{'tone':659}, 0.1,  {'tone':698}, 0.1,  {'tone':784}, 0.1,  {'tone':494}, 0.1,  {'tone':523}, 0.1,  {'tone':587}, 0.1,  {'tone':349}, 0.1,  {'tone':392}, 0.1,  {'tone':440}, 0.1,  {'tone':262}, 0.1,  {'tone':294}, 0.1,  {'tone':330}, 0.1])
#        (0x000020, 'Rising', [{'tone':131}, 0.2, {'tone':262}, 0.2, {'tone':523}]),
#        (0x000020, 'Falling', [{'tone':523}, 0.2, {'tone':262}, 0.2, {'tone':131}]),
    ]
}
