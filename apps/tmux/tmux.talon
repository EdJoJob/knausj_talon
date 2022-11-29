tag: user.tmux
-
tag(): user.splits

# pane management - these commands use the word split to match with the splits
# tag defined in tags/splits/splits.talon
go split <user.arrow_key>: user.tmux_keybind(arrow_key)
#Say a number after this command to switch to pane
go split: user.tmux_execute_command("display-panes -d 0")

go session: user.tmux_keybind(s)

mux rename: user.tmux_keybind($)
mux kill: user.tmux_execute_command_with_confirmation("kill-session -t")
mux rename window: user.tmux_keybind(,)
mux clear history: user.tmux_keybind(alt-c)
