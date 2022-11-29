mode: command
mode: dictation
-
^dictation mode$:
    user.dictation_mode()
    user.code_clear_language_mode()
    user.gdb_disable()
^command mode$: user.command_mode()
