os: linux
app: firefox
-
# Self-signed SSL
accept warning:
    key(tab space)
    sleep(100ms)
    key(tab tab tab space)

toggle dark: key(alt-shift-a)
toggle global dark: key(alt-shift-d)


dev console:
	key(ctrl-shift-J)
dev network:
	key(ctrl-shift-E)
dev tool (right|next):
	key(ctrl-])
dev tool (left|last):
	key(ctrl-[)
