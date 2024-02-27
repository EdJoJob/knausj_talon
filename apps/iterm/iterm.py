from talon import Context, Module, actions

ctx = Context()
mod = Module()

mod.apps.iterm2 = """
os: mac
and app.bundle: com.googlecode.iterm2
"""
ctx.matches = r"""
app: iterm2
"""

directories_to_remap = {}
directories_to_exclude = {}


@ctx.action_class("edit")
class EditActions:
    def line_start():
        actions.key("home")

    def line_end():
        actions.key("end")


@ctx.action_class("win")
class win_actions:
    def filename():
        title = actions.win.title()
        result = ""
        if "VIM" in title:
            result = title.split()[-1]

        if "." in result:
            return result

        return ""


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")

    def terminal_clear_screen():
        """Clear screen"""
        actions.key("ctrl-l")

    def split_maximize():
        actions.key("cmd-shift-enter")

    def split_window_horizontally():
        actions.key("cmd-shift-d")

    def split_window_vertically():
        actions.key("cmd-d")

    def split_window_up():
        actions.key("cmd-alt-up")

    def split_window_down():
        actions.key("cmd-alt-down")

    def split_window_left():
        actions.key("cmd-alt-left")

    def split_window_right():
        actions.key("cmd-alt-right")
