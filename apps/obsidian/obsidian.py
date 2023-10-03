from talon import Context, Module, actions, app

is_mac = app.platform == "mac"

ctx = Context()
mac_ctx = Context()
mod = Module()

mod.apps.obsidian = """
os: mac
and app.bundle: md.obsidian
"""

mac_ctx.matches = r"""
os: mac
app: obsidian
"""
