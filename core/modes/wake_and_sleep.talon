#defines the commands that sleep/wake Talon
mode: all
-
^drowse [<phrase>]$:
    user.code_clear_language_mode()
    speech.disable()
^talon wake$: speech.enable()
